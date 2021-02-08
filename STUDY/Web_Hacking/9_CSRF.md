---
sort: 9
---

# CSRF(Cross-site request forgery)

크로스 사이트 리퀘스트 변조는 사이트간 요청위조라고 불리기도 한다. 피해자의 권한으로 피해자 모르게 공격자가 의도한 요청을 수행 하도록 만드는것이다. 피해자의 권한에 따라서 위험성이 달라진다.

- 피해자는 공격자가 게시한 글을 읽었을 때 악성스크립트에 의한 요청이 서버로 보내지게 되고 서버는 피해자의 권한 내에서 해당 악성스크립트 요청을 처리하게 된다.
- 조작된 요청값을 이용해 웹 애플리케이션을 공격한다.

## 공격 과정

1. 공격자는 게시판에 USER가 관심을 가질 수 있는 제목으로 CSRF 스크립트가 포함된 게시물을 등록한다.
2. USER는 확인이 필요한 게시물로 파악하여, CSRF 스크립트가 포함된 게시물을 확인한다.
3. 게시물을 읽은 USER는 CSRF 스크립트가 포함된 것을 알지 못한 채 게시물을 확인한다. 하지만, USER의 권한으로 공격자가 원하는 CSRF 스크립트 요청이 발생한다.
4. 공격자가 원하는 CSRF 스크립트 결과가 발생하여 피해가 발생한다.

<br>

## 공격 실습

패스워드 변경 서비스를 제공하는 페이지(http://bee-box/bWAPP/csrf_1.php)의 코드를 분석한 후 로그인한 사용자가 http://bee-box/bWAPP/xss_stored_1.php에 접근했을 때 해당 사용자의 패스워드가 1234로 자동 변경되도록 코드 작성!!

**Step 1. csrf_1.php 소스 분석**

![csrf1](https://user-images.githubusercontent.com/76420201/107189246-675a2b80-6a2c-11eb-9706-b5aa5b3331a8.jpg)

method="GET" 요청방식을 사용하고 있으므로 서버로 전달할 내용이 URL에 주소에 포함된다. Change 버튼을 클릭하면 http://bee-box/`csrf_1.php?password_new=_____&password_conf=______&action=change` 형태의 요청이 서버로 전달되는것을 알수있다

**Step 2. 공격 URL을 호출하도록 게시판에 등록**

<iframe src = "http://bee-box/bWAPP/csrf_1.php?password_new=1234&password_conf=1234&action=change" width = "0" height="0"></iframe>