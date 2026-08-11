# 블로그 글 작성 가이드

> Jekyll + Kramdown 기반 블로그의 모든 구문 및 마크다운 문법 정리

## 목차

- [Front Matter](#front-matter)
- [Kramdown 인라인 속성](#kramdown-인라인-속성)
- [기본 마크다운 문법](#기본-마크다운-문법)
- [Jekyll Include 템플릿](#jekyll-include-템플릿)
- [이미지 관련](#이미지-관련)
- [링크 관련](#링크-관련)
- [코드 블록](#코드-블록)
- [수식 표현](#수식-latexmathjax)
- [Mermaid 다이어그램](#mermaid-다이어그램)
- [자주 사용하는 패턴 예시](#자주-사용하는-패턴-예시)
- [주의: 이모지 자동 변환](#주의-이모지-자동-변환)
- [체크리스트](#체크리스트)

---

## Front Matter

모든 포스트는 상단에 Front Matter(YAML 헤더)를 포함해야 합니다.

```yaml
---
layout: post
ins_date: 2025-03-15              # 작성일
upd_date: 2025-03-27              # 수정일
category: "ai"                    # 카테고리
subject: "cursor-mcp"             # 주제
title: "MCP Cursor 연동"          # 제목
description: "설명"                # 메타 설명
subtitle: "부제목"                 # 부제목
author: tiaz0128                  # 저자
permalink: /ai/2                  # 고유 주소
prev_post: /ai/1                  # 이전 글
next_post: /ai/3                  # 다음 글
tags: [MCP, Cursor, AI]           # 태그
ref-link:                         # 참고 링크
  - type: youtube
    url: 'https://youtu.be/...'
    title: '제목'
  - type: url
    url: 'https://example.com'
    title: '제목'
  - type: github
    url: 'https://github.com/...'
    title: '제목'
  - type: doc
    url: 'https://...'
    title: '제목'
  - type: book
    url: 'https://...'
    title: '제목'
---
```

### ref-link 타입 종류
- `youtube`: 유튜브 링크
- `url`: 일반 웹사이트 링크
- `github`: GitHub 링크
- `doc`: 문서 링크
- `article`: 기사 링크
- `book`: 책 링크
- `facebook`: 페이스북 링크
- `linkedin`: 링크드인 링크

---

## Kramdown 인라인 속성

Kramdown의 강력한 기능인 인라인 속성(IAL - Inline Attribute Lists)을 사용하여 스타일을 적용할 수 있습니다.

### 텍스트 색상 강조

```markdown
**강조할 텍스트**{:.orange}
**강조할 텍스트**{:.yellow}
```

**사용 예시:**
- `**중요한 내용입니다.**{:.orange}` → 오렌지색 강조
- `**주의가 필요합니다.**{:.yellow}` → 노란색 강조

### 이미지 캡션

```markdown
`> 이미지 설명 텍스트`{:.img-caption}
*> 출처 포함 캡션*{:.img-caption}
```

**사용 예시:**
```markdown
![이미지](/path/to/image.webp){:.img-m}

`> AI가 MCP로 GitHub를 도구처럼 이용한다! 😲`{:.img-caption}
```

### 경로/파일명 표시

```markdown
`경로나 파일명`{:.path}
```

**사용 예시:**
- `Open Cursor Settings`{:.path}
- `pyproject.toml`{:.path}
- `--python <PYTHON>`{:.path}

---

## 기본 마크다운 문법

### 제목 (Headings)

```markdown
# H1 제목
## H2 제목
### H3 제목
#### H4 제목
```

### 강조 (Emphasis)

```markdown
*이탤릭체*
**볼드체**
***볼드 + 이탤릭***
~~취소선~~
```

### 리스트 (Lists)

```markdown
# 순서 있는 리스트
1. 첫 번째
2. 두 번째
3. 세 번째

# 순서 없는 리스트
- 항목 1
- 항목 2
  - 하위 항목 2-1
  - 하위 항목 2-2
- 항목 3
```

### 인용 (Blockquote)

```markdown
> 인용문 내용
> 여러 줄도 가능합니다.
```

**사용 예시:**

```markdown
> "AI가 당신의 일을 빼앗지는 않을 것입니다. 하지만 AI를 사용하는 사람이 당신의 일을 빼앗을 것입니다."

> 생성자가 여러 차례 호출되더라도 실제로 생성되는 객체는 하나이고 최초 생성 이후에 호출된 생성자는 최초의 생성자가 생성한 객체를 리턴한다. ~ 위키백과 ~

> thread
> 1. 실
> 2. (이야기 등의) 가닥[맥락]
> 3. (실 등을) 꿰다
```

### 테이블 (Table)

```markdown
| 헤더1 | 헤더2 | 헤더3 |
| --- | --- | --- |
| 데이터1 | 데이터2 | 데이터3 |
| 데이터4 | 데이터5 | 데이터6 |
```

**정렬 옵션:**

```markdown
| 왼쪽 정렬 | 가운데 정렬 | 오른쪽 정렬 |
| :--- | :---: | ---: |
| Left | Center | Right |
```

**사용 예시:**

```markdown
| 포맷 | 의미 |
| --- | --- |
| %Y | 연도 (네 자리 숫자) |
| %m | 월 (두 자리 숫자) |
| %d | 일 (두 자리 숫자) |
| %H | 시간을 24시간 형식으로 |

| 유형 | 장점 | 단점 |
|----|----|----|
| 호스트형 가상화 | 호스트 OS와 작업 공존 가능 | 하드웨어 접근 속도 저하 |
| 컨테이너형 가상화 | 리소스 효율성 및 빠른 실행 | 커널 의존성 |
```

### 구분선 (Horizontal Rule)

```markdown
---
```

---

## Jekyll Include 템플릿

블로그에서 사용하는 재사용 가능한 템플릿들입니다.

### 1. alert.html - 알림 상자

```liquid
{% include template/alert.html
  type="warning"
  about="알림 내용"
%}
```

**type 옵션:**
- `warning`: 경고
- `note`: 참고
- `caution`: 주의
- `tip`: 팁

**사용 예시:**
```liquid
{% include template/alert.html
  type="warning"
  about="토큰은 유출되지 않게 복사해두고 잘 간직합니다!"
%}

{% include template/alert.html
  type="note"
  about="Cursor 버전을 꼭 확인 하세요!"
%}

{% include template/alert.html
  type="tip"
  about="다음글에서 계속 됩니다."
%}
```

### 2. link.html - 내부 링크 안내

```liquid
{% include template/link.html
  type="note"
  about="설명"
  url="/경로"
  title="링크 제목"
%}
```

**사용 예시:**
```liquid
{% include template/link.html
  type="note"
  about="vscode에서 mcp연동"
  url="/ai/4"
  title="MCP vscode 연동"
%}
```

### 3. youtube.html - 유튜브 영상 삽입

```liquid
{% include template/youtube.html
  url="유튜브 embed URL"
%}
```

**사용 예시:**

```liquid
{% include template/youtube.html
  url="https://www.youtube.com/embed/VIDEO_ID"
%}
```

**유튜브 + 캡션:**

```liquid
{% include template/youtube.html
    url="https://www.youtube.com/embed/MwiM_nPyx5Y?si=n1pjph5PL-awBd2g&amp;start=2285"
%}

`> Columbia Business School - NVIDIA CEO Jensen Huang Reveals Keys to AI, Leadership`{:.img-caption}
```

### 4. github.html - GitHub 소스 링크

```liquid
{% include template/github.html
  url="GitHub URL"
  repo_name="저장소명"
  branch="브랜치명"
%}
```

**사용 예시:**
```liquid
{% include template/github.html
  url="https://github.com/user/repo"
  repo_name="tiaz0128/project"
  branch="main"
%}
```

### 5. gallery.html - 이미지 갤러리 (캐러셀)

```liquid
{% include template/gallery.html
  id="gallery-id"
  images=images_array
  alt="이미지 설명"
%}
```

**사용 예시:**
```liquid
{% capture images %}
/assets/img/001.webp,
/assets/img/002.webp,
/assets/img/003.webp
{% endcapture %}
{% assign images_array = images | split: "," | map: "strip" %}

{% include template/gallery.html
  id="my-gallery"
  images=images_array
  alt="갤러리 이미지"
%}
```

### 6. tetris-gallery.html - 테트리스 스타일 갤러리

```liquid
{% include template/tetris-gallery.html
  id="gallery-id"
  images=images_array
  alt="이미지 설명"
%}
```

데스크탑에서는 테트리스 스타일 그리드, 모바일에서는 캐러셀로 표시됩니다.

### 7. img-container.html - 2개 이미지 나란히 배치

```liquid
{% include template/img-container.html
  type="half"
  left="/path/to/left.webp"
  right="/path/to/right.webp"
%}
```

**type 옵션:**
- `half`: 5:5 비율
- `3-7`: 3:7 비율 (왼쪽:오른쪽)
- `7-3`: 7:3 비율 (왼쪽:오른쪽)

### 8. book.html - 책 정보

```liquid
{% include template/book.html
  title="책 제목"
  author="저자명"
  publisher="출판사"
  book_url="책 구매 링크"
  target_readers="대상 독자"
  review="한줄 평"
%}
```

### 9. ref.html - 참고 문헌

```liquid
{% include template/ref.html refs=page.ref-link %}
```

Front Matter의 `ref-link`에 정의된 참고 문헌을 자동으로 렌더링합니다.

---

## 이미지 관련

### 이미지 삽입 기본

```markdown
![대체 텍스트](/assets/img/path/image.webp)
```

### 이미지 크기 클래스

Kramdown IAL을 사용하여 이미지 크기를 조절할 수 있습니다.

```markdown
![이미지](/path/to/image.webp){:.img-s}        # small
![이미지](/path/to/image.webp){:.img-m}        # medium
![이미지](/path/to/image.webp){:.img-l}        # large
![이미지](/path/to/image.webp){:.img-200x200}  # 200x200 고정
```

### 이미지 + 캡션

```markdown
![이미지 설명](/assets/img/content/ai/002/001.webp){:.img-m}

`> 이미지 캡션 내용`{:.img-caption}
```

### 출처 포함 캡션

```markdown
![차트](/assets/img/chart.webp)

*> 출처 : [출처명](링크URL){:target="_blank"}*{:.img-caption}
```

**사용 예시:**

```markdown
![TIOBE Index](/assets/img/tiobe.webp){:.img-l}

*> 출처 : [tiobe.com](https://www.tiobe.com/tiobe-index/){:target="_blank"}*{:.img-caption}
```

---

## 링크 관련

### 기본 링크

```markdown
[링크 텍스트](URL)
```

### 새 탭에서 열기

```markdown
[링크 텍스트](URL){:target="_blank"}
```

### 내부 링크 (밑줄 없음)

```markdown
[링크 텍스트](/internal/path){:.none}
[링크 텍스트](/internal/path){:.none target="_blank"}
```

**사용 예시:**
```markdown
다음글: [MCP 서버 구축](/ai/3){:.none target="_blank"}
[싱글턴 패턴](/python/4){:.none}을 사용하여...
```

---

## 코드 블록

### 인라인 코드

```markdown
`코드 내용`
```

### 코드 블록 (언어 지정)

````markdown
```python
def hello():
    print("Hello, World!")
```

```javascript
console.log("Hello, World!");
```

```bash
npm install package-name
```
````

### 파일명 포함 코드 블록

```markdown
<div class="file-name">파일명.py</div>

```python
# 코드 내용
```
```

**사용 예시:**
```markdown
<div class="file-name">.cursor/mcp.json</div>

```json
{
  "mcpServers": {
    "github": {
      "command": "npx"
    }
  }
}
```
```


---

## 수식: LaTeX/MathJax

블로그는 MathJax를 지원하여 수학 수식을 표현할 수 있습니다.

`jekyll-spaceship` 플러그인이 페이지에 수식이 있는지 감지해서 빌드할 때 MathJax를 자동으로 넣어줍니다. 따라서 **Front Matter에 `math: true`를 넣을 필요가 없습니다.** 넣으면 테마의 오래된 MathJax 2.7.5가 한 벌 더 로드되어 중복됩니다. (`mermaid: true`는 실제로 필요하니 혼동하지 말 것)

### 인라인 수식

```markdown
텍스트 중간에 $x = y + z$ 이렇게 수식을 넣을 수 있습니다.
```

**렌더링 결과:**  
텍스트 중간에 $x = y + z$ 이렇게 수식을 넣을 수 있습니다.

### 블록 수식

```markdown
$$
Octet = 8bit = 2^8 = 256
$$
```

**렌더링 결과:**

$$Octet = 8bit = 2^8 = 256$$

### 수식 사용 예시

```markdown
IP 주소는 8bit가 4개이므로 32bit를 이용해서 약 42억개의 IP를 표현 가능합니다.

$$\text{IPv4} = 8bit \times 4 = 32bit = 2^{32} = 4,294,967,296$$

VPC는 IP 주소 32bit 중에서 16bit를 고정하고 나머지 16개를 사용합니다.

$$2^{16} = 65536 = \text{앞에 두덩이는 고정. 나머지 두 덩이(16bit)는 사용 가능}$$

Subnet은 256개의 IP를 사용할 수 있는 범위를 의미합니다.

$$2^{8} = 256 = \text{Subnet은 256개의 IP를 사용할 수 있는 범위를 뜻함}$$
```

---

## Mermaid 다이어그램

블로그는 Mermaid.js를 지원하여 다양한 다이어그램을 그릴 수 있습니다.

### Mermaid 사용 설정

Mermaid를 사용하려면 Front Matter에 `mermaid: true`를 추가해야 합니다.

```yaml
---
layout: post
title: "제목"
mermaid: true    # Mermaid 활성화
---
```

### Mermaid 다이어그램 작성

```html
<pre class="mermaid center">
%%{
  init: {
    'theme': 'base',
    'themeVariables': {
      'primaryColor': '#2a3844',
      'lineColor': '#fff',
      'primaryTextColor': '#fff',
      'tertiaryColor': '#fff'
    }
  }
}%%

# 여기에 Mermaid 코드 작성
</pre>
```

### Mermaid 테마 색상 커스터마이징

```javascript
%%{
  init: {
    'theme': 'base',
    'themeVariables': {
      'primaryColor': '#2a3844',      // 기본 배경색
      'primaryTextColor': '#fff',     // 기본 텍스트 색상
      'primaryBorderColor': '#fff',   // 테두리 색상
      'lineColor': '#fff',            // 선 색상
      'secondaryColor': '#006100',    // 보조 색상
      'tertiaryColor': '#fff'         // 3차 색상
    }
  }
}%%
```

### 자주 사용하는 Mermaid 패턴

#### 패턴 1: 아키텍처 플로우차트

```html
<pre class="mermaid center">
flowchart TB
    subgraph "Client Layer"
        Web[Web Browser]
        Mobile[Mobile App]
    end
    
    subgraph "Server Layer"
        API[API Server]
        Auth[Auth Service]
    end
    
    subgraph "Data Layer"
        DB[(Database)]
        Cache[(Redis)]
    end
    
    Web --> API
    Mobile --> API
    API --> Auth
    API --> DB
    API --> Cache
</pre>
```

#### 패턴 2: 디자인 패턴 클래스 다이어그램

```html
<pre class="mermaid center">
classDiagram
    class Interface{
        <<interface>>
        +method()
    }
    
    class ConcreteClassA{
        +method()
    }
    
    class ConcreteClassB{
        +method()
    }
    
    Interface <|.. ConcreteClassA
    Interface <|.. ConcreteClassB
</pre>
```

---

## 자주 사용하는 패턴 예시

### 패턴 1: 알림 + 링크

```liquid
{% include template/alert.html
  type="note"
  about="추가 정보가 필요하신가요?"
%}

자세한 내용은 [관련 문서](/path){:.none target="_blank"}를 참고하세요.
```

### 패턴 2: 이미지 + 캡션 + 설명

```markdown
![설명](/assets/img/image.webp){:.img-m}

`> 이미지 캡션`{:.img-caption}

이미지에 대한 추가 설명을 여기에 작성합니다.
```

### 패턴 3: 코드 + 설명

```markdown
아래 코드는 **중요한 기능**{:.orange}을 구현합니다:

<div class="file-name">example.py</div>

\`\`\`python
def important_function():
    return "result"
\`\`\`

이 함수는...
```

### 패턴 4: 단계별 설명

```markdown
1. `Open Cursor Settings`{:.path} 버튼 클릭
2. `MCP`{:.path} 탭 선택
3. 원하는 MCP 설정
```

### 패턴 5: 글 마무리

```liquid
## 마무리

내용 정리...

{% include template/alert.html
  type="tip"
  about="다음글에서 계속 됩니다."
%}

다음글: [다음 주제](/category/next){:.none target="_blank"}

감사합니다! 😊

## 참고 문헌

{% include template/ref.html refs=page.ref-link %}
```

---

## 주의: 이모지 자동 변환

`jemoji`와 `jekyll-spaceship`이 `:단축코드:` 형태를 이모지 이미지로 바꿉니다. 문제는 **백틱으로 감싼 코드 스팬 안에서도 변환된다**는 점입니다.

콜론으로 구분되는 값을 쓸 때 걸립니다. 특히 IPv6 주소가 대표적입니다.

```markdown
2001:db8:1234:1a00::/56   → :1234: 가 🔢 로 변환됨
2001:db8:abcd:1a00::/56   → :abcd: 가 🔡 로 변환됨
```

`:1234:`(🔢), `:abcd:`(🔡), `:abc:`(🔤), `:100:`(💯) 등이 모두 실제 단축코드입니다. IPv6 예시 주소를 쓸 때는 이런 값을 피하거나 `::`로 압축해서 콜론 사이에 단어가 오지 않게 합니다.

```markdown
2001:db8:1a00::/56   → 안전
```

작성 후 렌더링된 페이지에서 확인하는 게 확실합니다.

```bash
$ curl -s http://localhost:4000/AWS/6 | grep -c 'class="emoji"'
```

---

## 체크리스트

글 작성 전 확인사항:

- [ ] Front Matter 작성 완료
- [ ] 카테고리와 태그 설정
- [ ] 이미지 경로 확인 (`/assets/img/content/...`)
- [ ] 외부 링크에 `{:target="_blank"}` 추가
- [ ] 코드 블록 언어 지정
- [ ] 참고 문헌 `ref-link` 추가
- [ ] 이미지 캡션 작성
- [ ] 중요 내용 강조 (`{:.orange}`, `{:.yellow}`)
- [ ] 경로/파일명 `{:.path}` 표시
- [ ] 수식 사용 시 `$$` 블록 수식 또는 `$` 인라인 수식
- [ ] Mermaid 사용 시 Front Matter에 `mermaid: true` 추가
- [ ] 테이블 형식이 필요한 경우 마크다운 테이블 사용
- [ ] 콜론이 들어간 값(IPv6 주소 등)이 이모지로 변환되지 않았는지 확인

---

**작성일:** 2025-11-04  
**마지막 업데이트:** 2025-11-04
