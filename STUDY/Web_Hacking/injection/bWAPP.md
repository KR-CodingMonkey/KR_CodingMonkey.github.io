

# Bee - Box

비박스(bee-box)란 웹 어플리케이션에서 자주 발생하는 취약점을 쉽게 테스트할 수 있도록 의도된 환경을 제공한다. 정확한 명칭은 bWAPP이며, 이를 가상머신의 형태로 꾸며놓은 것을 비박스라고 부른다. 사실 이러한 취약점 테스팅 서비스는 비박스가 처음으로 등장한 것은 아니며, 대표적으로 DVWA이나 WebGoat(OWASP 프로젝트)와 유사하다. 비박스가 가지는 장점은 실습해볼 수 있는 컨텐츠의 양이 절대적으로 훨씬 더 많다는 것이다. 여기에 난이도 조절이 3단계로 가능하므로 조금 더 폭넓은 모의해킹 연습 훈련소로 활용할 수 있다.

<details markdown="1">
<summary><b>Union SQL Injection</b></summary>
<br>   
bWQPP -> SQL Injection(GET/Search) level = Low

영화 정보 제공 서비스

문제: 해당 사이트의 사용자 정보(예: 이름, 이메일 주소, 전화번호, 아이디, 패스워드, …)를 탈취하시오. 

**Step 1. 기본 동작을 유추** 

**Step 2. 인젝션 가능 여부를 확인**

**Step 3. 정상적인 서비스 쿼리가 반환하는 컬럼의 개수를 확인**

**Step 4. UNION 구문을 이용해서 데이터 출력 개수와 위치를 확인**

**Step 5. UNION 구문을 이용해서 데이터베이스 정보를 조회**
</details>

<details markdown="1">
<summary><b>sqlmap을 이용한 공격
</b></summary>
<br>   

</details>