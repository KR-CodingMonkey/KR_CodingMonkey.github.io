

# Bee - Box

<center><img src = "https://user-images.githubusercontent.com/76420201/106377985-3783a600-63e4-11eb-924e-731743774575.jpg" width = "70%"></center>
<br>

- 비박스(bee-box)란 웹 어플리케이션에서 자주 발생하는 취약점을 쉽게 테스트할 수 있도록 의도된 환경을 제공한다. 정확한 명칭은 bWAPP이며, 이를 가상머신의 형태로 꾸며놓은 것을 비박스라고 부른다. 
- 취약점 테스팅 서비스는 비박스가 처음으로 등장한 것은 아니며, 대표적으로 DVWA이나 WebGoat(OWASP 프로젝트)와 유사하다. 비박스가 가지는 장점은 실습해볼 수 있는 컨텐츠의 양이 절대적으로 훨씬 더 많다는 것이다. 
- 난이도 조절이 3단계로 가능하므로 조금 더 폭넓은 모의해킹 연습 훈련소로 활용할 수 있다.

<br>

<details markdown="1">
<summary><b>Union SQL Injection</b></summary>
<br>   

```
bWQPP -> SQL Injection(GET/Search)

ID : bee
PW : bug
level : Low

문제: 해당 사이트에서 사용자 정보(이름, 아이디, 패스워드 등)를 탈취하기 
```

---

**Step 1. 기본 동작을 유추**

해당 페이지는 영화 제목을 검색하는 페이지기 때문에 **DB에서 사용자 입력을 키워드로 조회한 결과**를 보여준다.

<center><img src = "https://user-images.githubusercontent.com/76420201/106378432-1c1a9a00-63e8-11eb-924b-c9bdac4f8bfd.gif"></center>

서버 내부 처리(추측)<br>
`select * from movies where title like '%man%'`

---

**Step 2. 인젝션 가능 여부를 확인**

검색란에 작은따옴표`'`를 입력하여 SQL 인젝션이 가능한지 알아본다. 변수에 SQL 인젝션 취약점이 존재하는 경우 SQL오류 메시지를 출력한다.<br>
작은따옴표`'`를 입력하는 이유는 DB에서 `'`로 문자 데이터를 구분하기 때문이다. 따라서 취약점이 존재할 때 `'`를 입력하면 웹 서버에서 DB서버에 질의하는 쿼리에 문법 오류가 발생한다.

서버 내부 처리(추측)<br>
`SELECT * FROM moview WEHRE LIKE ' %man'% '`

<center><img src= "https://user-images.githubusercontent.com/76420201/106378433-1d4bc700-63e8-11eb-960d-4bd979b6dc9b.gif"></center>

오류 메시지에는 DB 서버가 포함되는데, DB서버 종류의 따라 SQL 구문이 다르기 때문에 가장먼서 서버 정보를 확인한다. 오류 메시지를 확인해 보면 해당 DB 서버는 MySQL이라는 정보를 출력하고 있다.

---

**Step 3. UNION 구문을 이용해서 데이터 출력 개수와 위치를 확인**

`or 1=1`이라는 쿼리는 앞 쿼리의 내용과는 상관없이 항상 참이라는 결과를 만드는 쿼리이다. 이 쿼리를 통해서 **어떤 주석 문자를 사용하는지 알아본다**. 맨 마지막에 주석 문자를 붙여주면서 기존 코드의 뒷부분을 주석 처리한다. 

MySQL주석 문자는 `#` 또는 `--`을 사용한다. 따라서 두가지 쿼리를 입력해봐야 한다.
1. `' or 1=1--`
2. `' or 1=1#` 

<center><img src = "https://user-images.githubusercontent.com/76420201/106378861-50dc2080-63eb-11eb-9e03-29994b7f91b3.gif" width = "70%"></center>

첫번째 쿼리에서는 에러가 나고 두번째 쿼리에서 정상적으로 결과가 출력되는걸 확인할 수 있다.

더 자세한 정보를 알아내기 위하여 UNION SELECT 구문을 사용한다. UNION은 SELECT 문이 둘 이상일 때 이를 결합하여 결과를 하나로 반환한다.

두 쿼리의 결과를 하나의 테이블로 합치기 때문에 UNION 구문을 사용하려면 이전 쿼리에서 사용하는 **SELECT 문의 칼럼 수를 일치** 시켜줘야 한다. 칼럼의 수가 일치하지 않는경우 오류 메시지가 나오고, 오류 메시지가 나오지 않을 때까지 칼럼 수를 늘려가며 확인한다.

`' UNION SELECT  1,2,3,4,5#`

<center><img src = "https://user-images.githubusercontent.com/76420201/106379433-59cef100-63ef-11eb-8937-fc0ad93e4445.gif"></center>
<br>

`' UNION SELECT  1,2,3,4,5,6,7#`<br>
칼럼수가 7개가 될 때 정상적으로 결과를 출력한다. 또한 `1,2,3,4,5,6,7`로 입력 하였을때 `2, 3, 5, 4`칼럼의 값만 출력되는 것을 확인할 수 있다.

<center><img src = "https://user-images.githubusercontent.com/76420201/106379432-589dc400-63ef-11eb-8b33-ee22c1813be0.gif" width = "70%"></center>

---

**Step 4. UNION 구문을 이용해서 데이터베이스 정보를 조회**

MySQL 버전을 확인하기 위해서 시스템 변수나 시스템 함수를 활용하여 쿼리를 입력한다.

`' UNION SELECT 1, @@version, 3, 4, 5, 6, 7#`

<center><img src = "https://user-images.githubusercontent.com/76420201/106381745-52fbaa80-63fe-11eb-9503-cf5ac7de52d3.gif" width = "70%"></center>

- SQL 인젝션으로 데이터베이서의 정보를 파악할 수 있는 변수와 함수

| 시스템 변수 및 함수 | 설명 |
|-------------------|------|
| databases() | 데이터베이스 명을 알려주는 함수|
| user() | 현자 사용자의 아이디 |
| system_user() | 최고 권한 사용자의 아이디 |
| @@version | 데이터베이스 서버의 버전 |
| @@datadir | 데이터베이스 서버가 존재하는 디렉터리 |

---

**Step 5. 구글링을 통해 버전 정보 확인 ⇒ DBMS의 종류가 MySQL인 것을 확인**

</details>

<br>

<details markdown="1">
<summary><b>sqlmap을 이용한 공격
</b></summary>
<br>   

</details>