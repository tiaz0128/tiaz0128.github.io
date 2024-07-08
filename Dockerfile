# Ruby 이미지를 기반으로 합니다.
FROM ruby:3.0

RUN bundle config --global frozen 1

WORKDIR /srv/jekyll

COPY Gemfile Gemfile.lock tale.gemspec ./

RUN bundle install

VOLUME /srv/jekyll
