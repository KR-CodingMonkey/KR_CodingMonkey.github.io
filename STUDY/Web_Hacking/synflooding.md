---
sort: 3
---

# TCP SYN Flooding

<center><img src = "https://user-images.githubusercontent.com/76420201/106401723-fbdeef80-6468-11eb-80f2-9ee8eaece9d6.jpg"></center>


TCP/IP 네트워크에서의 정상적 TCP 연결 3-way handshake 과정의 경우, 클라이언트가 원격지 서버의 특정 포트에 SYN패킷(packet)을 발송함으로써 연결을 요청하고 요청을 받은 원격 서버가 SYN/ACK 패킷으로 응답한 후 수신된 연결 요청 정보를 해당 시스템 TCP 연결 자원인 Backlog Queue내 incomplete connection queue에 저장한다.

이때 서버가 응답한 SYN+ACK에 대하여 클라이언트가 ACK로써 응답을 보내지 않으면 accept()시스템 콜을 통해 클라이언트와 통신할 연결소켓을 생성하지 못하므로 서버는 incomplete connetion queue에 있던 연결 요청 정보를 수행하지 못하고 그대로 남아있다는 **half-open TCP** 연결 상태에 머무르는 구조적 취약점이 있다.

Attacker(공격자)는 이 취약점을 이용한 서비스 거부(Dos)를 유발하는 공격을 위해서 서버 특정 포트에 SYN packet을 발송하는 과정을 대량으로 중첩시켜 Backlog Queue내 incomplete connetion queue를 가득 채움으로써 소진시키게 되고 이로인해 더 이상 새로운 클라이언트의 TCP 연결요청을 받을 수 없게 되어 이 후 요청되는 다수의 TCP 연결이 완료되지 않고 무시된다.

```note
백로그 큐가 꽉 차게 되면 더 이상 연결요청을 받을 수 없어 정상적인 서비스 제공이 불가능한 상태가 된다.

클라이언트의 응답 문자(ACK)가 없으면 서버에서는 클라이언트의 접속 정보를 잠시 운용 기록에 쌓아 두는데, 이러한 요구가 증가했을 경우 시스템은 운용기록 공간을 확보하기 못하게 되고, 결국 네트워크 중단으로 이어여 Dos가 일어난다.

TCP 통신 연결 수립을 위한 3way-handshake 특성을 이용하여 클라이언트에서 SYN 정보만 전송 후, SYN/ACK 정보 수신에 따른 ACK전송을 하지 않음으로써 서버를 장시간 대기상태로 만들어 리소스를 점유하는 전형적인 SYN Flooding 공격 유형이다.
```

## 공격과정

**Step 1. Victim 가상머신에서 syncookie 사용을 확인 후 사용을 해제**

```
┌──(kali㉿kali)-[~]
└─$ sudo sysctl -a | grep syncookies
'net.ipv4.tcp_syncookies = 1'
```

syncookie를 사용하면 backlog que가 가득 차 있어도 정보를 계속 쌓을 수 있다. 실습을 위해서 Victim의 syncookie를 해제한다.

```
┌──(kali㉿kali)-[~]
└─$ sudo sysctl -w  net.ipv4.tcp_syncookies=0		
'net.ipv4.tcp_syncookies = 0'	
```

---

**Step 2. TCP syn flooding 공격**

```
┌──(kali㉿kali)-[~]
└─$ sudo scapy   
```
