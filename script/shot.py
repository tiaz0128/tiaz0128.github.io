"""요약본 문서에서 표지 미리보기와 배포용 PDF를 굽는다.

    uv run shot.py                      # resources/ 전부
    uv run shot.py ec2-ebs-eni          # 하나만

산출물
    assets/img/resources/<slug>-cover.webp   1페이지 그림
    resources/<slug>.pdf                     받기 버튼이 주는 파일
    _data/service_icons.yml                  목록 줄에 쓰는 AWS 서비스 아이콘

표지는 문서마다 걸리지 않는다. 요약본 구역 맨 위에 견본 한 장이
붙을 뿐이고, 그게 어느 것인지는 _data/links.yml 의 sample: 이 정한다.
그러니 여기서 구운 -cover.webp 는 그 견본을 갈 때만 쓴다 — 새 문서마다
굽지 않아도 된다. PDF 는 문서마다 필요하고, 브라우저 인쇄로 뽑아도 된다
(A4 · 여백 없음 · 배경 그래픽 켬).

HTML이 원본이고 PDF는 파생물이다. PDF를 손으로 고치지 말 것 —
문서를 고치고 이걸 다시 돌린다.
문서를 새로 넣거나 내용을 고쳤을 때만 돌리면 된다.
"""
import json
import sys
from io import BytesIO
from pathlib import Path

import yaml
from PIL import Image
from playwright.sync_api import Error, sync_playwright

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "resources"
OUT = ROOT / "assets" / "img" / "resources"

# A4 210x297mm을 96dpi로 본 크기. 문서의 .sheet가 실제로 이 폭이다.
SHEET_W = 794
COVER_W = 620  # 저장할 폭. 카드에서 최대 2배로 쓰인다.


def sync_service_icons(browser) -> int:
    """요약본이 쓰는 AWS 서비스 아이콘만 골라 _data 로 뽑는다.

    aws.json 이 2.5MB라 통째로 _data 에 두면 매 빌드마다 그걸 파싱한다.
    쓰는 것만 옮겨 두면 Liquid 에서 바로 꺼내 쓸 수 있다.

    원본은 뷰박스 안에서 그림이 차지하는 비율이 제각각이다 — 서비스
    아이콘은 색 사각형이 꽉 차고, 리소스 아이콘은 선 그림이 여백을 두고,
    화살표 같은 건 한 귀퉁이만 쓴다. 같은 크기로 걸면 따로 논다.
    그래서 브라우저에 실제로 그려 잉크 경계를 재고, 그 경계를 감싸는
    정사각형으로 뷰박스를 다시 잡는다. 그러면 어떤 아이콘이든 잉크가
    같은 비율로 채운다.
    """
    catalog = yaml.safe_load((ROOT / "_data" / "resources.yml").read_text("utf-8")) or []
    wanted = sorted({k for d in catalog for k in (d.get("services") or [])})

    dst = ROOT / "_data" / "service_icons.yml"
    if not wanted:
        dst.unlink(missing_ok=True)
        return 0

    icons = json.loads((ROOT / "assets" / "json" / "icons" / "aws.json")
                       .read_text("utf-8"))["icons"]
    page = browser.new_page()
    page.set_content("<body></body>")

    picked = {}
    for key in wanted:
        ic = icons.get(key)
        if ic is None:
            raise SystemExit(f"aws.json 에 '{key}' 가 없다")
        box = page.evaluate(
            """([w, h, body]) => {
                 const ns = 'http://www.w3.org/2000/svg';
                 const svg = document.createElementNS(ns, 'svg');
                 svg.setAttribute('viewBox', `0 0 ${w} ${h}`);
                 svg.innerHTML = body;
                 document.body.appendChild(svg);
                 const b = svg.getBBox();
                 svg.remove();
                 return [b.x, b.y, b.width, b.height];
               }""",
            [ic["width"], ic["height"], ic["body"]])
        x, y, w, h = box
        side = max(w, h) * 1.06          # 잉크가 테두리에 닿지 않게 아주 조금만
        cx, cy = x + w / 2, y + h / 2
        view_box = (f"{cx - side / 2:.2f} {cy - side / 2:.2f} "
                    f"{side:.2f} {side:.2f}")
        picked[key] = {"view_box": view_box, "body": ic["body"]}

    page.close()
    dst.write_text(
        "# shot.py 가 만든다. 직접 고치지 말 것.\n"
        "# _data/resources.yml 의 services: 에 적힌 아이콘만 담긴다.\n"
        "# view_box 는 원본 그대로가 아니라 잉크 경계를 감싸는 정사각형이다.\n"
        + yaml.safe_dump(picked, allow_unicode=True, sort_keys=True, width=10**6),
        "utf-8")
    return len(picked)


def shoot(browser, path: Path) -> Path:
    page = browser.new_page(viewport={"width": SHEET_W, "height": 1123},
                            device_scale_factor=2)
    page.goto(path.as_uri(), wait_until="load")
    # 웹폰트가 앉기 전에 찍으면 표지 제목이 폴백 폰트로 나온다.
    page.evaluate("document.fonts.ready")
    # 영상은 인쇄 때와 같이 정지 이미지로 대체해 찍는다. 프레임마다
    # 표지가 달라지면 미리보기가 아니라 스냅샷이 된다.
    page.emulate_media(media="print")
    page.wait_for_timeout(600)

    sheet = page.query_selector("article.sheet")
    if sheet is None:
        raise SystemExit(f"{path.name}: article.sheet 를 못 찾음")
    png = sheet.screenshot(type="png")

    # 같은 페이지에서 PDF까지 뽑는다. 문서에 @page A4 와 인쇄용 규칙이
    # 들어 있어서 여백 0으로 두면 화면에서 보던 그대로 나온다.
    pdf_path = path.with_suffix(".pdf")
    page.pdf(path=str(pdf_path), format="A4", print_background=True,
             margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
    page.close()

    img = Image.open(BytesIO(png)).convert("RGB")
    img = img.resize((COVER_W, round(img.height * COVER_W / img.width)),
                     Image.LANCZOS)
    OUT.mkdir(parents=True, exist_ok=True)
    dst = OUT / f"{path.stem}-cover.webp"
    img.save(dst, "WEBP", quality=82, method=6)
    return dst, pdf_path


def launch(p):
    """chromium 을 띄운다. 못 뜨면 고칠 방법을 말해 준다.

    새로 깐 WSL/우분투에는 chromium 이 기대는 시스템 라이브러리가 없다.
    Playwright 가 내는 건 60줄짜리 traceback 이고 정작 무엇이 없는지는
    브라우저 로그 한가운데 묻힌다. 여기서 가로채 한 줄로 바꾼다.
    """
    try:
        return p.chromium.launch()
    except Error as e:
        if "error while loading shared libraries" not in str(e):
            raise
        raise SystemExit(
            "chromium 이 시스템 라이브러리가 없어 못 뜬다. 한 번만 깔면 된다:\n"
            "    sudo apt-get install -y libnss3 libnspr4 libasound2t64"
        ) from None


def main() -> None:
    wanted = sys.argv[1:]
    files = sorted(SRC.glob("*.html"))
    if wanted:
        files = [f for f in files if f.stem in wanted]
    if not files:
        raise SystemExit("찍을 문서가 없다")

    with sync_playwright() as p:
        browser = launch(p)

        n = sync_service_icons(browser)
        print(f"서비스 아이콘 {n}개 -> _data/service_icons.yml")

        for f in files:
            cover, pdf = shoot(browser, f)
            for out in (cover, pdf):
                print(f"{f.name} -> {out.relative_to(ROOT)} "
                      f"({out.stat().st_size // 1024}KB)")
        browser.close()


if __name__ == "__main__":
    main()
