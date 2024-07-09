
## Blog URL
[https://tiaz.dev/](https://tiaz.dev/)

Eat Sleep Coding. Never Never Giveup.

밥잠코. 절절포

<img src="./assets/img/zo.jpg" width="200" height="200"/>

<br/>


## Using Theme
Made with Jekyll using the [Tale](https://github.com/chesterhow/tale) theme.

<br/>

## Use docker

- windows 환경에서는 --livereload(= -l) 옵션이 제대로 동작하지 않을수 있음
-WSL 에서 --livereload 동작 가능

### 1. Gemefile.lock 파일 생성

```yml
FROM ruby:3.0

WORKDIR /srv/jekyll

VOLUME /srv/jekyll
```

```bash
$ docker run -v="./:/srv/jekyll" -it blog bundle install
```

### 2. docker image build

```yml
# Ruby 이미지를 기반으로 합니다.
FROM ruby:3.0

RUN bundle config --global frozen 1

WORKDIR /srv/jekyll

COPY Gemfile Gemfile.lock tale.gemspec ./

RUN bundle install

VOLUME /srv/jekyll
```

### 3. docker-compose up

```bash
$ docker-compose up --build

$ docker-compose down
```
