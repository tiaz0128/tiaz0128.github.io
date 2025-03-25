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

## 이미지 -> webp

```bash
$ pip install pillow

$ python convert-webp.py
```
