# Ruby 이미지를 기반으로 합니다.
FROM ruby:2.7

# 작업 디렉토리를 설정합니다.
WORKDIR /usr/src/app

# Gemfile과 Gemfile.lock을 복사합니다.
COPY Gemfile tale.gemspec ./

# Bundler를 설치하고, Gemfile에 명시된 gem들을 설치합니다.
RUN gem install bundler && bundle install

# 소스 코드를 컨테이너에 복사합니다.
COPY . .

# Jekyll 서버를 실행합니다.
CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0", "--port", "4000"]
