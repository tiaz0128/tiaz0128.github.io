import os
from PIL import Image
from pathlib import Path


def convert_to_webp(source_path, output_path, quality=100):
    """이미지를 WebP 형식으로 변환합니다."""
    try:
        image = Image.open(source_path)
        # 만약에 title 폴더 내 이미지인 경우에는 이미지 크기도 조정
        if "title" in str(source_path):
            # 세로는 100px로 고정하고 가로는 비율에 맞게 조정
            if image.height > 100:
                ratio = image.width / image.height
                new_width = int(200 * ratio)
                image = image.resize((new_width, 200), Image.Resampling.LANCZOS)
                print(f"타이틀 이미지 크기 조정: {source_path} -> {output_path}")

        # RGBA 모드 확인 (투명도가 있는 이미지)
        if image.mode in ("RGBA", "LA"):
            image.save(output_path, "WEBP", quality=quality, lossless=False)
        else:
            # RGB 모드 (투명도가 없는 이미지)
            image.convert("RGB").save(output_path, "WEBP", quality=quality)
        print(f"변환 성공: {source_path} -> {output_path}")
        return True
    except Exception as e:
        print(f"변환 실패: {source_path}, 오류: {e}")
        return False


def process_directory(source_dir):
    """디렉토리 내의 모든 이미지를 WebP로 변환합니다."""
    # 지원되는 이미지 확장자
    image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"}

    # 변환 통계
    success_count = 0
    fail_count = 0

    # 모든 파일 처리
    for root, _, files in os.walk(source_dir):
        for file in files:
            file_path = Path(root) / file
            file_ext = file_path.suffix.lower()

            # 지원되는 이미지 파일만 처리
            if file_ext in image_extensions:
                # 출력 파일 경로 (같은 위치에 .webp 확장자로)
                webp_path = file_path.with_suffix(".webp")

                # 변환 수행
                if convert_to_webp(file_path, webp_path):
                    success_count += 1
                else:
                    fail_count += 1

    # 결과 출력
    print(f"\n변환 완료: 성공 {success_count}개, 실패 {fail_count}개")


if __name__ == "__main__":
    image_dir = "img"

    # 디렉토리 확인
    if not os.path.exists(image_dir):
        print(f"오류: 디렉토리가 존재하지 않습니다: {image_dir}")
    else:
        print(f"{image_dir} 디렉토리의 모든 이미지 파일을 WebP로 변환합니다...")
        process_directory(image_dir)
