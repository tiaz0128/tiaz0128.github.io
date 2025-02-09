// TOC와 h2 태그를 선택합니다.
var tagLinks = document.querySelectorAll(".tags-clouds > a");
var h2Elements = Array.from(document.querySelectorAll("h2.tags-item-label"));

// 스크롤 이벤트 리스너를 추가합니다.
window.addEventListener('scroll', function() {
    var scrollPosition = window.pageYOffset;

    // 현재 스크롤 위치가 어느 h2 태그 구간에 있는지 찾습니다.
    var currentSection = h2Elements.findIndex((h2, i) => {
        if (i === h2Elements.length - 1) {
            return scrollPosition >= h2.offsetTop - 60;
        } else {
            return scrollPosition >= (h2.offsetTop - 60) && scrollPosition < h2Elements[i + 1].offsetTop - 60;
        }
    });

    // TOC 링크의 스타일을 업데이트합니다.
    tagLinks.forEach((link, i) => {
        if (i === currentSection) {
            link.classList.add("active"); // "active" 클래스를 추가합니다.
        } else {
            link.classList.remove("active"); // "active" 클래스를 삭제합니다.
        }
    });
});


// 각 TOC 링크에 클릭 이벤트 리스너를 추가합니다.
tagLinks.forEach((link, i) => {
    link.addEventListener('click', function(e) {
        e.preventDefault(); // 기본 클릭 이벤트를 막습니다.

        // 클릭한 링크에 해당하는 h2 태그의 위치로 스크롤합니다.
        // 여기서 20px을 더하여 스크롤 위치를 조정합니다.
        window.scrollTo({
            top: h2Elements[i].offsetTop - 70,
            behavior: 'smooth' // 스크롤이 부드럽게 이동하도록 설정합니다.
        });
    });
});