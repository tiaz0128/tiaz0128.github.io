---
layout: post
---
### 글자색상
```text
`반드시 전역 이름과 비밀번호를 기억해자`{:.y-p}

**win10**{:.y-s}
```

```html
<div>
  <span class="y-s">win10</span>
</div>
```

### 링크
```text
[link](http://www.naver.com){:target="_blank"}
```

### 콜아웃
```html
<div class="callout">:memo:
  <div>
    <p>JS 는 기본적으로 동기로 실행 → 실행이 끝나야 다음 코드가 실행된다.</p>
    <p>Promise 는 <strong>비동기로 실행</strong></p>
  </div>
</div>
```

### 코드
```text
{% raw %}{% highlight javascript linenos %}
print code
{% endhighlight %}{% endraw %}
```

### 코드블럭 이스케이프
```text
{% raw %} {% raw %} code { % endraw % }  {% endraw %}
```

### 이미지
```bash
!["github blog"](/assets/img/content/git_blog/git_blog.png){:.img-s}

!["github blog"](/assets/img/content/git_blog/git_blog.png){:.img-l}
```

### 표
```text
|head|head|
|----|----|
| 1 | text |
| 2 | text |
{:.post-table }
```