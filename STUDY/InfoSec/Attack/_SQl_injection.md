
# SQL Injection

외부 입력값을 쿼리 조작 문자열 포함 여부를 검증하지 않고 SQL문 생성 및 실행에 사용하는 경우 <br>
1. 쿼리의 의미와 구조가 변경되어서 실행
2. 의도하지 않은 데이터베이스에 대한 조작이 가능

## 공격자 패턴

1. 항상 참이 되는 입력
ex) a' or 'a' = 'a
select * from users where name = 'a' or 'a' = 'a' -> 모든 데이터를 조회 -> 권한 밖에 데이터에 접근 가능

2. 오류를 유발하는 입력

ex) a'
-> select * from users where name = 'a'' -> 구분 오류를 유발

시스템 오류를 통해서 시스템 내부 정도 수집에 활용

3. 추가 정보를 조회하는 입력
ex) hong' union select * from ... --
select * from users where name = 'hong' 
union
select * from ... --

4. 시스템 명령어 실행하는 입력

입력 ex) hong'; exec xp_cmdshell 'cmd.exe /c ipconfig'; -- 
select * from users where name = 'hong'; exec xp_cmdshell 'cmd.exe /c ipconfig'; -- '

해당 DBMS의 쉘 이용이 가능 = 제어권을 탈취


5. 참, 거짓을 유발하는 입력 ⇒ Blind SQL Injection

## 방어 기법

방어기법
- 쿼리 조작 문자열 포함 여부를 확인
    - 제거하고 사용
    - 안전한 형태로 바꿔서 사용
- 일정한 형태로 쿼리가 실행되는 것을 보장 = 구조화된 쿼리 실행 = 파라미터화된 쿼리 실행 = 정적 쿼리 실행
- 오류 메시지를 통제 = 오류 메시지에 시스템 정보가 포함되지 않도록 처리
- 어플리케이션에서 사용하는 DB 사용자의 권한을 최소로 부여
