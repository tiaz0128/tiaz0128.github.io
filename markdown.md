### 글자색상
---
- `{:.y-p}`
- `{:.y-s}`
- `{:.b-s}`

```mk
`대상 문자열`{:class_name}

`반드시 전역 이름과 비밀번호를 기억해자`{:.y-p}

**win10**{:.y-s}
```

### 링크
```mk
[link](http://www.naver.com){:target="_blank"}
```

### 콜아웃
```mk
<div class="callout">:memo:
  <div>
    <p>JS 는 기본적으로 동기로 실행 → 실행이 끝나야 다음 코드가 실행된다.</p>
    <p>Promise 는 <strong>비동기로 실행</strong></p>
  </div>
</div>
```

### 코드
```mk
{% raw %}{% highlight python linenos %}
print code
{% endhighlight %}{% endraw %}
```

### 코드블럭 이스케이프
```mk
{% raw %} 
    {% raw %} code { % endraw % }
{% endraw %}
```

### 이미지
---
- `{:.img-s}`
- `{:.img-l}`

```mk
!["github blog"](/assets/img/content/title/python.png){:.img-s}

!["github blog"](/assets/img/content/title/python.png){:.img-l}
```

### 표
---
- `{:.post-table }`

```mk
|head|head|
|----|----|
| 1 | text |
| 2 | text |
{:.post-table }
```