
# DNS Spoofing

DNS(Domain Name Server) spoofing(DNS cache Spoofing 이라고도 함)은 DNS 서버로 보내는 질문을 가로채서 변조된 결과를 보내주는 것으로 일종의 중간자 공격이다.

![DNS-spoofing](https://user-images.githubusercontent.com/76420201/105853028-93d37800-6028-11eb-9b62-5bfb607fb803.jpg)

- MITM(Man in the middle) : 사용자를 다른 or 악의적인 IP주소로 라우팅하기 위해 사용자와 DNS서버간의 통신을 가로채는 것

- DNS 서버 손상 : DNS서버를 손상시켜 악의적인 IP주소를 반환하도록 함

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