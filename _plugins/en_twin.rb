# 글의 영어판(_en/<경로>.md)을 한국어 글(_posts/<같은 경로>.md) 안에 싣기 위한 준비.
#
# 1. 머리말 물려받기: 영어 본문은 영어 문서 자신을 page 로 삼아 그려진다. 그런데 영어
#    파일에는 title · subtitle · description · ref-link 처럼 말이 다른 것만 적는다.
#    본문 속 템플릿이 page.permalink(book.html) · page.category 같은 것을 읽으면 영어판에서만
#    비어 버리므로, 영어 파일에 없는 키는 한국어 글의 값으로 채운다(영어 파일이 늘 이긴다).
#    layout 은 빼고 물려받는다 — 영어 문서는 본문만 쓰이고, 페이지로 나가지 않는다.
#    그리고 lang: en 을 단다. 본문 속 템플릿(template/link.html 등)이 이것을 보고 문구를 영어로 낸다.
#
# 2. 영어판을 먼저 그린다: Jekyll 은 컬렉션을 posts → en 순서로 그린다. 그대로 두면
#    post.html 이 page_en.content 를 읽을 때 영어판은 아직 마크다운 원문이라
#    `**굵게**{:.orange}` · `{% include %}` 가 글자 그대로 드러난다. en 을 맨 앞으로 옮긴다.
Jekyll::Hooks.register :site, :post_read do |site|
  en = site.collections['en']
  next unless en

  posts = site.posts.docs.to_h { |p| [p.relative_path.sub(%r{\A_posts/}, ''), p] }
  en.docs.each do |doc|
    ko = posts[doc.relative_path.sub(%r{\A_en/}, '')]
    next unless ko

    ko.data.each { |key, value| doc.data[key] = value unless key == 'layout' || doc.data.key?(key) }
    doc.data['lang'] ||= 'en'
  end

  ordered = { 'en' => en }.merge(site.collections.reject { |name, _| name == 'en' })
  site.instance_variable_set(:@collections, ordered)
end
