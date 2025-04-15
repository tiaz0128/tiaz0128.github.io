import requests
import os


# 유튜브 URL에서 비디오 ID 추출 함수
def extract_video_id(youtube_url):
    """
    유튜브 URL에서 비디오 ID를 추출합니다.

    Args:
        youtube_url (str): 유튜브 비디오 URL

    Returns:
        str: 유튜브 비디오 ID 또는 None
    """
    if "youtu.be" in youtube_url:
        # youtu.be/VIDEO_ID 형식
        return youtube_url.split("/")[-1].split("?")[0]
    elif "youtube.com/watch" in youtube_url:
        # youtube.com/watch?v=VIDEO_ID 형식
        import urllib.parse as urlparse
        from urllib.parse import parse_qs

        parsed_url = urlparse.urlparse(youtube_url)
        return parse_qs(parsed_url.query)["v"][0]
    else:
        print("지원되지 않는 URL 형식입니다.")
        return None


def download_thumbnail(video_id, save_path="thumbnail.jpg"):
    """
    유튜브 비디오 ID로부터 최고 화질의 썸네일을 다운로드합니다.

    Args:
        video_id (str): 유튜브 비디오 ID
        save_path (str): 저장할 파일 경로

    Returns:
        bool: 다운로드 성공 여부
    """
    # 최고 화질 썸네일 URL (maxresdefault.jpg)
    thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"

    # 요청 보내기
    response = requests.get(thumbnail_url)

    # 최고 화질 썸네일이 없는 경우 (404 에러), 다음 고화질 썸네일 시도
    if response.status_code != 200:
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
        response = requests.get(thumbnail_url)

    # 다운로드 성공
    if response.status_code == 200:
        # 파일로 저장
        with open(save_path, "wb") as file:
            file.write(response.content)
        print(f"썸네일이 '{save_path}'에 성공적으로 저장되었습니다.")
        return True
    else:
        print(f"썸네일 다운로드 실패: 상태 코드 {response.status_code}")
        return False


def main() -> None:
    # 사용자 입력
    youtube_url = input("유튜브 URL을 입력하세요: ")
    video_id = extract_video_id(youtube_url)

    if video_id:
        # 기본 저장 경로 설정 (현재 디렉토리에 video_id.jpg)
        save_path = f"{video_id}.jpg"
        download_thumbnail(video_id, save_path)


if __name__ == "__main__":
    main()
