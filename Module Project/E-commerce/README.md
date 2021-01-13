# E-commerce

- 프로젝트 주제
1. 회원관리 프로그램 -> python
2. 주문관리 프로그램 -> python
3. 상품목록 관리 프로그램 -> python
4. 관리자 프로그램 -> python
5. 데이터베이스 생성 -> Mysql
6. Container 가상화로 프로그램과 데이터베이스 구성 -> Docker contianer
7. [Docker hub](https://hub.docker.com) 사이트 자신의 repository에 이미지 배포
---
- 요구사항

1. 회원
- 회원가입을 통해 사용자 등록을 할 수 있따.
- 등록된 사용자는 로그인 한 후, 자신의 정보를 수정 또는 회원 탈퇴 할 수 있다.
- 로그인 한 회원은 상품 목록을 검색 한 후, 상품을 주문할 수 있다.<br/>

2. 주문
- 주문 정보는 로그인 된 회원에 한해서 제공된다.
- 사용자별 주문 정보를 확인 할 수 있다.
- 주문상품이 보유상품보다 클 경우 주문할 수 없다.<br/>

3. 상품목록
- 관리자에 의해서 상품목록이 추가/수정 할 수 있다.
- 주문이 발생하면, 상품목록 정보에서 주문된 상품의 수량만큼 상품의 재고에서 차감된다.<br/>

4. 관리자
- 관리자의 아이디/비밀번호는 admin/admin123로 지정한다.
- 전체 회원 목록을 조회할 수 있다.
- 전체 주문 목록과 회원별 주문 목륵을 조회할 수 있다.
- 상품목록에 상품을 추가할 수 있다.
- 가장 많은 금액을 주문한 사용자 목록을 확인할 수 있다.
- 가장 많이 팔린 상품 목록을 확인할 수 있다.<br/>
---

- 실행화면

Init Page

![init](https://user-images.githubusercontent.com/76420201/104425234-c3fc2f00-55c3-11eb-8f90-7ee102b3742a.GIF)

Admin Mode

![admin](https://user-images.githubusercontent.com/76420201/104425244-c8284c80-55c3-11eb-9fd7-da45dc80e5ab.GIF)

User Mode

![user](https://user-images.githubusercontent.com/76420201/104425241-c65e8900-55c3-11eb-8ae9-21d67056c247.GIF){: width = "20%" height = "20%"}