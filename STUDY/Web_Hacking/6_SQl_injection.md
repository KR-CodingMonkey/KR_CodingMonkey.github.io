---
sort: 6
---

# SQL Injection

<center><img src = "https://user-images.githubusercontent.com/76420201/106089260-ee74ed00-616a-11eb-8fe7-1ac6681d5e2e.png" ></center>

SQL Injection 이란 악의적인 사용자가 보안상의 취약점을 이용하여, 임의의 SQL 문을 주입하고 실행되게 하여 데이터베이스가 비정상적인 동작을 하도록 조작하는 행위 입니다. 인젝션 공격은 비교적 쉬운 편이고 공격에 성공할 경우 큰 피해를 입힐 수 있는 공격입니다. SQL 인젝션은 사용자가 데이터를 입력할 수 있는 곳 어디에서든 발생할 수 있고, 이를 통하여 공격자는 SQL 쿼리를 변수에 입력하여 데이터베이스 정보를 획득하거나 시스템 내부를 파악할 수 있습니다.

- 외부 입력값을 쿼리 조작 문자열 포함 여부를 검증하지 않고 SQL문 생성 및 실행에 사용하는 경우 <br>
    - 쿼리의 의미와 구조가 변경되어서 실행
    - 의도하지 않은 데이터베이스에 대한 조작이 가능

- 공격 방법이나 사용 언어에 따라 인젝션의 종류가 달라지는데, 대표적인 유형으로 SQL 인젝션, HTML 인젝션, OS command 인젝션, LDAP 인젝션 등이 있음

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
예) `hong' union select * from ... --`<br>
```
select * from users where name = 'hong' <br>
union<br>
select * from ... --<br>
```

4. 시스템 명령어 실행하는 입력<br><br>
예) hong'; exec xp_cmdshell 'cmd.exe /c ipconfig'; -- <br>
`select * from users where name = 'hong'; exec xp_cmdshell 'cmd.exe /c ipconfig'; -- '`<br>
-> 해당 DBMS의 쉘 이용이 가능 = 제어권을 탈취

5. 참, 거짓을 유발하는 입력 ⇒ Blind SQL Injection

<br>

## 방어 기법

- 쿼리 조작 문자열 포함 여부를 확인
    - 제거하고 사용
    - 안전한 형태로 바꿔서 사용
- 일정한 형태로 쿼리가 실행되는 것을 보장 = 구조화된 쿼리 실행 = 파라미터화된 쿼리 실행 = 정적 쿼리 실행
- 오류 메시지를 통제 = 오류 메시지에 시스템 정보가 포함되지 않도록 처리
- 어플리케이션에서 사용하는 DB 사용자의 권한을 최소로 부여