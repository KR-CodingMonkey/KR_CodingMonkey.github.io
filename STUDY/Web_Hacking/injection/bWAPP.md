

# Bee - Box

<center><img src = "https://user-images.githubusercontent.com/76420201/106377985-3783a600-63e4-11eb-924e-731743774575.jpg" width = "70%"></center>
<br>

- 비박스(bee-box)란 웹 어플리케이션에서 자주 발생하는 취약점을 쉽게 테스트할 수 있도록 의도된 환경을 제공한다. 정확한 명칭은 bWAPP이며, 이를 가상머신의 형태로 꾸며놓은 것을 비박스라고 부른다. 
- 취약점 테스팅 서비스는 비박스가 처음으로 등장한 것은 아니며, 대표적으로 DVWA이나 WebGoat(OWASP 프로젝트)와 유사하다. 비박스가 가지는 장점은 실습해볼 수 있는 컨텐츠의 양이 절대적으로 훨씬 더 많다는 것이다. 
- 난이도 조절이 3단계로 가능하므로 조금 더 폭넓은 모의해킹 연습 훈련소로 활용할 수 있다.

<details markdown="1">
<summary><b>Union SQL Injection</b></summary>
<br>   
bWQPP -> SQL Injection(GET/Search) level = Low

문제: 해당 사이트에서 사용자 정보(이름, 아이디, 패스워드 등)를 탈취하기 

---

**Step 1. 기본 동작을 유추** '

해당 페이지는 영화 제목을 검색하는 페이지기 때문에 **DB에서 사용자 입력을 키워드로 조회한 결과**를 보여준다.

![bwapp0](https://user-images.githubusercontent.com/76420201/106378432-1c1a9a00-63e8-11eb-924b-c9bdac4f8bfd.gif)

서버 내부 처리(추측)<br>
`select * from movies where title like '%man%'`

---

**Step 2. 인젝션 가능 여부를 확인**

검색란에 작은따옴표(')를 입력하여 SQL 인젝션이 가능한지 알아본다. 변수에 SQL 인젝션 취약점이 존재하는 경우 SQL오류 메시지를 출력한다.<br>
작은따옴표(')를 입력하는 이유는 DB에서 `'`로 문자 데이터를 구분하기 때문이다. 따라서 취약점이 존재할 때 `'`를 입력하면 웹서버에서 DB서버에 질의한느 쿼리에 문법 오류가 발생한다.

`SELECT * FROM moview WEHRE LIKE ' man' '`

![bwapp1](https://user-images.githubusercontent.com/76420201/106378433-1d4bc700-63e8-11eb-960d-4bd979b6dc9b.gif)

오류 메시지에는 DB 서버가 포함되는데, DB서버 종류의 따라 SQL 구문이 다르기 때문에 가장먼서 서버 정보를 확인한다. 오류 메시지를 확인해 보면 해당 DB 서버는 MYSQL이라는 정보를 출력하고 있다.

---

**Step 3. 정상적인 서비스 쿼리가 반환하는 컬럼의 개수를 확인**

---

**Step 4. UNION 구문을 이용해서 데이터 출력 개수와 위치를 확인**

---

**Step 5. UNION 구문을 이용해서 데이터베이스 정보를 조회**

---

**Step 6. 구글링을 통해 버전 정보 확인 ⇒ DBMS의 종류가 MySQL인 것을 확인**

</details>

<br>

<details markdown="1">
<summary><b>sqlmap을 이용한 공격
</b></summary>
<br>   

</details>