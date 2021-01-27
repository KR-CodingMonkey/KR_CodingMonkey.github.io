
# ARP spoofing

- 근거리 통신망 하에서 주소 결정 프로토콜 메시지를 이용하여 상대방의 데이터 패킷을 중간에서 가로채는 중간자 공격 기법
이 공격은 데이터 링크 상의 프로토콜인 ARP 프로토콜을 이용하기 때문에 **근거리상의 통신에서만 사용할 수 있는 공격**

- 흔히 사용되는 공격 방식은 게이트웨이 IP를 스푸핑하는 것으로, 이 경우 외부로 전송되는 모든 **패킷이 공격자에 의해 가로채거나 변조될 수 있다**

- 이 기법을 사용한 공격의 경우 특별한 이상 증상이 쉽게 나타나지 않기 때문에 사용자는 특별한 도구를 사용하지 않는 이상 쉽게 자신이 공격당하고 있다는 사실을 확인하기 힘들다.

<center><img src = "https://user-images.githubusercontent.com/76420201/105661757-8e373e80-5f11-11eb-9a24-f413d87914b1.GIF" width = "60%"></center>

ARP spoofing이 어떻게 이루어 지는지 살펴봅니다.

|Name|IP|MAC|GateWay|
|-|-|-|-|
|WinXP|192.168.126.128|00-0C29-4B43-8E|192.168.126.2|
|Victim|192.168.126.129 | 00:50:56:27:10:7e| |
|Attacker|192.168.126.130|00:50:56:22:93:7f| |

3개 가상머신의 각각 IP 정보입니다.

<br>

**1) WinXP에서 ARP 캐시 테이블 내용과 기본 게이트웨이 주소를 확인**

공격이 있기 전 ARP 테이플에서는 정상적인 Gateway의 MAC주소를 저장하고 있습니다.

![spoofing1](https://user-images.githubusercontent.com/76420201/105667103-102d6480-5f1e-11eb-96f5-921fcd475bc1.GIF)

---

**2) WinXP에서 IE로 www.google.com에 접속 확인**

정상적인 게이트웨이를 통해서 통신이 잘 이루어지는 모습입니다.

![spoofing2](https://user-images.githubusercontent.com/76420201/105667105-128fbe80-5f1e-11eb-86ee-44fc1658618e.GIF)

---

**3) Attacker에서 arp spoofing 공격을 시도**

ARP spoofing 공격을 통해서 WinXP ARP 테이블안에 저장되어있는 Gateway의 MAC 주소(00:50:56:e5:2d:46)를 Attacker의 MAC 주소(00:50:56:22:93:7f)로 변경할 수가 있습니다.

이렇게 Attacker의 MAC주소를 GateWay의 MAC주소라고 입력시켜 버리면 WinXP에서 보내려고 했던 패킷을 Attacker가 가로채거나 변조할 수 있게 됩니다. 

![spoofing3](https://user-images.githubusercontent.com/76420201/105709665-62d84200-5f59-11eb-87ee-28aa9826e142.GIF)

---

**4) WinXP에서 ARP 캐시 테이블을 확인**
![spoofing4](https://user-images.githubusercontent.com/76420201/105709672-64096f00-5f59-11eb-90d5-61718cc7f82a.GIF)

---

**5) WinXP에서 구글에 접속되지 않는 것을 확인**

<img src = "https://user-images.githubusercontent.com/76420201/105710372-5e605900-5f5a-11eb-891e-61e53ead9820.GIF" width = "70%">

---

**6) Attacker에서 fragrouter 도구를 이용해서 라우팅 처리**

`fragrouter -B1` B1 옵션은 송수신 데이터가 변조 없이 그대로 포워딩을 해주는 역할을 합니다.

arpspoof 만을 사용하게 되면 희생자는 서비스를 원활하게 이용할 수 없게 되니 이상함을 눈치챌 수 있으니<br>
fragrouter를 같이 이용해 줌으로서 통신은 정상적으로 되고 모든 패킷은 공격자를 통해서 전달하게 됩니다.

```                                                                         
┌──(kali㉿kali)-[~]
└─$ sudo fragrouter -B1
[sudo] password for kali: 
fragrouter: base-1: normal IP forwarding
```

---

**7) WinXP에서 Attacker로 ping을 전송하고 ARP 캐시 테이블을 확인**

![spoofing7](https://user-images.githubusercontent.com/76420201/105712207-d4fe5600-5f5c-11eb-94bc-1bce0bcc9440.GIF)

이렇게 APR Table을 확인 하였을때 GateWay의 MAC주소가 다른 IP의 MAC주소와 같다면 Spoofing을 당하고 있다는 것입니다.


![spoofing5](https://user-images.githubusercontent.com/76420201/105709673-64096f00-5f59-11eb-975f-0131417b969a.GIF)

spoofing을 종료하게 되면 자동으로 원래 MAC주소로 돌려 놓읍니다.
