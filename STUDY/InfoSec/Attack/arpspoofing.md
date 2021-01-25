
# ARP spoofing

근거리 통신망 하에서 주소 결정 프로토콜 메시지를 이용하여 상대방의 데이터 패킷을 중간에서 가로채는 중간자 공격 기법
이 공격은 데이터 링크 상의 프로토콜인 ARP 프로토콜을 이용하기 때문에 근거리상의 통신에서만 사용할 수 있는 공격
<center><img src = "https://user-images.githubusercontent.com/76420201/105661757-8e373e80-5f11-11eb-9a24-f413d87914b1.GIF" width = "60%"></center>


|Name|IP|MAC|GateWay|
|-|-|-|-|
|WinXP|192.168.126.128|00-0C29-4B43-8E|192.168.126.2|
|Victim|192.168.126.129 | 00:50:56:27:10:7e| |
|Attacker|192.168.126.130|00:50:56:22:93:7f| |

3개 가상머신의 각각 IP 정보입니다.

**1) WinXP에서 ARP 캐시 테이블 내용과 기본 게이트웨이 주소를 확인**

공격이 있기 전 ARP 테이플에서는 정상적인 Gateway의 MAC주소를 저장하고 있습니다.

![spoofing1](https://user-images.githubusercontent.com/76420201/105667103-102d6480-5f1e-11eb-96f5-921fcd475bc1.GIF)

**2) WinXP에서 IE로 www.google.com에 접속 확인**

정상적인 게이트웨이를 통해서 통신이 잘 이루어지는 모습입니다.

![spoofing2](https://user-images.githubusercontent.com/76420201/105667105-128fbe80-5f1e-11eb-86ee-44fc1658618e.GIF)

**3) Attacker에서 arp spoofing 공격을 시도**

이제,  WinXP ARP 테이블 Gateway의 MAC 주소(00:50:56:e5:2d:46)를 spoofing 공격으로 Attacker의 MAC 주소(00:50:56:22:93:7f)로 변경할 수가 있습니다.

이렇게 Attacker의 MAC주소를 GateWay의 MAC주소라고 입력시켜 버리면 WinXP에서 보내려고 했던 패킷을 Attacker가 훔칠 수 있게 됩니다. 
**4) WinXP에서 ARP 캐시 테이블을 확인**

**5) Attacker에서 Wireshark를 실행**

**6) WinXP에서 구글에 접속되지 않는 것을 확인**

**7) Attacker에서 fragrouter 도구를 이용해서 라우팅 처리**

**8) WinXP에서 구글에 접속하면 Attacker에 아래 로그가 생성되는 것을 확인**

**9) WinXP에서 Attacker로 ping을 전송하고 ARP 캐시 테이블을 확인**
