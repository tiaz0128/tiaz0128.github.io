FROM ruby:3.2

RUN bundle config --global frozen 1

WORKDIR /srv/jekyll

COPY Gemfile Gemfile.lock tale.gemspec ./

RUN bundle install
