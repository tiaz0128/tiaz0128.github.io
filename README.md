## Blog URL

[https://tiaz.dev/](https://tiaz.dev/)

Eat Sleep Coding. Never Never GiveUp.

밥잠코. 절절포

<img src="./assets/img/tiaz.webp" width="200" height="200" alt="tiaz0128"/>

<br/>

## Using Theme

Made with Jekyll using the [Tale](https://github.com/chesterhow/tale) theme.

<br/>

## Use docker

- windows 환경에서는 --livereload(= -l) 옵션이 제대로 동작하지 않을수 있음
- WSL 에서 --livereload 동작 가능

### 1. Gemefile.lock 파일 생성

```bash
$ docker compose up gemfile
```

### 2. docker compose up

```bash
$ docker compose up dev --build

$ docker compose down
```

### 3. WSL서버 접속

```bash
$ ip addr show eth0 | grep 'inet ' | awk '{print $2}'
172.31.176.197/20
```

아래의 URL로 접속
```
http://172.31.176.197:4000
```

## 이미지 -> webp

```bash
$ uv sync

$ python convert-webp.py
```

## 요약본 추가

문서는 `resources/<slug>.html` 에 두는 통짜 HTML 이다. 프런트매터를 붙이면
Jekyll 컬렉션 문서가 되어 jekyll-spaceship 이 달라붙고 빌드가 멈추므로,
프런트매터 없이 정적 파일로 둔다.

```bash
# 1. 문서를 넣는다
$ cp <어딘가>/my-sheet.html resources/my-sheet.html

# 2. 표지 미리보기 + 배포용 PDF + 서비스 아이콘을 굽는다
$ cd script
$ uv run shot.py my-sheet      # 인자 없이 돌리면 resources/ 전부

# 3. _data/resources.yml 맨 위에 항목을 추가한다 (파일 안 주석 참고)
```

`/link` 목록은 `date` 가 가장 최신인 문서만 표지를 크게 보여주고,
나머지는 한 줄로 세운다. PDF 는 파생물이니 손으로 고치지 말고 2번을 다시 돌린다.

## 한영 스위치 (2026-09-30)

상단 메뉴(링크 페이지는 카드 왼쪽 위)의 `EN / 한국어` 버튼이 보이는 말을 바꾼다.
처음 볼 말은 `?lang=en|ko` → 지난번 고른 것 → 브라우저 언어 순으로 정한다.

- **글의 영어판**은 `_en/<카테고리>/<같은 파일 이름>.md` 에 둔다(`_posts/` 와 같은 경로).
  머리말에는 말이 다른 것만 적는다: `title` · `subtitle` · `description` · (있으면) `ref-link`.
  책 글은 영어 제목만 `title` 에 두고 한국어 원제는 `original_title` 에 둔다(책 정보에 괄호로 붙는다).
  나머지(permalink · category · tags …)는 한국어 글에서 물려받는다(`_plugins/en_twin.rb`).
  본문은 한국어와 같은 형식 그대로 — 제목 수준 · 빈 줄 · `{:.orange}` 같은 속성 · include 태그를 지킨다.
  영어판은 따로 페이지가 되지 않고 한국어 글 페이지 안에 함께 실린다(`_layouts/post.html`).
- **두 말을 가진 자리**는 `{% include component/tr.html ko=... en=... %}` 로 쓴다(`.l-ko` / `.l-en` 한 쌍).
  글 속 템플릿(`_includes/template/*`)은 `page.lang == 'en'` 이면 문구를 영어로 낸다.
- **링크 페이지**의 영어 문구는 `_data/links.yml` 의 `*_en` 키, 요약본은 `_data/resources.yml` 의
  `title_en` · `summary_en` · `slug_en`(영어판 `resources/<slug_en>.html` · `.pdf`).
- **카테고리 이름**(글 목록 칩 · 카드)은 `_data/categories.yml`.
- `_plugins/` · `_config.yml` 을 바꿨으면 `docker compose up dev` 서버를 **다시 켠다**
  (둘 다 켤 때 한 번만 읽는다 — 안 그러면 영어 본문이 마크다운 원문으로 보인다).

## 글 목록 (2026-09-30)

메뉴: 소개 · 글 · 태그 · 검색 + 한영 스위치(그래프 뷰와 링크 버튼은 2026-09-30에 뺐다. /link/ 페이지는 그대로).
홈은 카테고리 칩(글 수) + 최신순 카드 한 페이지다(`_layouts/home.html`, `component/post-card.html`).
칩은 페이지 안에서 바로 거르고 `?cat=` 이 주소에 남는다. 페이지 나누기(paginate)는 껐다.
