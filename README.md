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
