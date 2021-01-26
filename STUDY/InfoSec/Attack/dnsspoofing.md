
# DNS Spoofing

DNS(Domain Name Server) spoofing(DNS cache Spoofing 이라고도 함)은 DNS 서버로 보내는 질문을 가로채서 변조된 결과를 보내주는 것으로 일종의 중간자 공격이다.

![DNS-spoofing](https://user-images.githubusercontent.com/76420201/105853028-93d37800-6028-11eb-9b62-5bfb607fb803.jpg)

- MITM(Man in the middle) : 사용자를 다른 or 악의적인 IP주소로 라우팅하기 위해 사용자와 DNS서버간의 통신을 가로채는 것

- DNS 서버 손상 : DNS서버를 손상시켜 악의적인 IP주소를 반환하도록 함

**DNS spoofing 공격 원리**

1. 사용자의 컴퓨터는 보통 컴퓨터가 사용하는 IP 주소대신 사람들이 쓰기 편한 문자로 구성되어 있는 URL주소를 사용한다. 하지만 컴퓨터는 URL주소를 바로 인식할 수 없기 때문에, 사용자로부터 URL주소를 입력을 받으면 등록된 도메인 네임 시스템의 주소로 UDP프로토콜을 이용하여 질의를 보낸다.

2. 이때 중간자 공격을 받고 있는 경우에는 사용자의 컴퓨터가 보내는 질의의 내용을 수정하여 도메인 네임 시스템서버에 전송하고, 도메인 네임 시스템서버는 변경된 질의에 대한 답을 사용자의 컴퓨터로 보내고, 사용자의 컴퓨터는 질의에 나와 있는 IP 주소를 이용하여 접속을 하게 된다. 이때 이미 질의가 중간자 공격으로 인해 원래의 값이 아니기 때문에 의도치 않은 곳으로 접속될 수 있다.


`ipconfig /flushdns` : dns 테이플 초기화
`ipconfig /displaydns` : dns 테이블 조회

ettercap : 중간자 공격(MTM Attack, Man in the Middle)을 쉽게 할 수 있도록 만들어진 프로그램

ettercap에서 사용할 변조 DNS 정보를 설정

Step 1. WinXP에서 DNS 캐시 테이블을 확인

Step 2. Attacker 가상머신에서 ettercap에서 사용할 변조 DNS정보를 설정

`vi /etc/ettercap/etter.dns` 파일 수정

Step 3. Attacker 가상머신에서 아파치를 실행 후 브라우저를 통해 확인


Step 4. Attacker 가상머신에서 ettercap 실행

Step 5. WinXP 가상머신에서 ARP 테이블을 확인

Step 6. WinXP 가상머신에서 구글 접속을 확인

Step 7. Attacker 가상머신에서 DNS Spoofing을 실행

Step 8. WinXP 가상머신에서 구글 접속 및 DNS 캐시 테이블 확인