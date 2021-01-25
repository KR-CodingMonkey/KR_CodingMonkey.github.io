
# ARP spoofing

근거리 통신망 하에서 주소 결정 프로토콜 메시지를 이용하여 상대방의 데이터 패킷을 중간에서 가로채는 중간자 공격 기법
이 공격은 데이터 링크 상의 프로토콜인 ARP 프로토콜을 이용하기 때문에 근거리상의 통신에서만 사용할 수 있는 공격

![arpspoofing](https://user-images.githubusercontent.com/76420201/105661757-8e373e80-5f11-11eb-9a24-f413d87914b1.GIF)

#1 @WinXP에서 ARP 캐시 테이블 내용과 기본 게이트웨이 주소를 확인

#2 @WinXP에서 IE로 www.google.com에 접속 확인

#3 @Attacker에서 arp spoofing 공격을 시도 

#4 @WinXP에서 ARP 캐시 테이블을 확인

#5 @Attacker에서 Wireshark를 실행

#6 @WinXP에서 구글에 접속되지 않는 것을 확인

#7 @Attacker에서 fragrouter 도구를 이용해서 라우팅 처리

#8 @WinXP에서 구글에 접속하면 @Attacker에 아래 로그가 생성되는 것을 확인

#9 @WinXP에서 @Attacker로 ping을 전송하고 ARP 캐시 테이블을 확인
