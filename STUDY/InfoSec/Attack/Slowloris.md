
# Slowloris Attack

**Slowloris Attack** : 웹 서버의 다수의 커넥션 연결 후 각 커넥션 별로 비정상 HTTP헤더 (완료되지 않는 헤더)를 전송함으로써 웹 서버 단의 커넥션 자원을 고갈 시키는 공격

- HTTP Header 정보를 비정상적으로 조작하여 웹서버가 온전한 Header정보가 올때 까지 기다리도록 한다.

- 서버가 연결 상태를 유지할 수 있는 가용자원은 한계가 있으므로 임계치를 넘어가면 다른 정상적인 접근을 거부하게 된다.

<br>

## Slowloris Attack 공격 원리

1. HTTP에선 헤더의 끝을 /r/n 이라는 개행문자를 구분한다.
2. 공격자(Attacker)는 이 마지막 문자를 보내지 않고 지속적으로 의미없는 변수를 추가한다.
3. 서버는 헤더 정보가 아직 전송 중이라고 인식하고 연결을 유지한다.
4. timer가 만료되기전에 불완전한 HTTP 요청을 반복적으로 수행하면서 client connection의 최대 수용가능한 수까지 도달하여 서버의 connection 자원을 고갈시킨다.

<br>

## Slowloris Attack 공격 순서

**Step 1. Victim 가상머신에서 네트워크 상태를 모니터링**

```
┌──(kali㉿kali)-[/var/www/html/bWAPP]
└─$ watch "netstat -pant"  
```

![slowloris](https://user-images.githubusercontent.com/76420201/105925447-8ac3c480-6083-11eb-9d32-a8c568352850.gif)


- netstat [option]
    -p	: 해당 프로토콜을 사용하고 있는 프로그램을 표시
    -a	: 모든 연결 및 수신 대기 포트 표시
    -n	: 주소나 포트 형식을 숫자로 표현
    -t	: TCP로 연결된 포트를 표시

<br>

**Step 2. Attacker 가상머신에서 브라우저로 Victim 가상머신의 아파치로 접속**

![slowloris0](https://user-images.githubusercontent.com/76420201/106067998-21a38600-6143-11eb-91ae-2e60f826c0fe.jpg)

|STATE| 의미|
|-|-|
|LISTEN 	|	서버의 데몬이 떠 있어서 클라이언트의 접속 요청을 기다리고 있는 상태 (LISTENING)|
|SYN_RECV | 서버가 클라이언트로부터 접속 요구SYN)를 받아 클라이언트에게 응답(SYN/ACK)를 보낸 상태|
|ESTABLISHED |	서버와 클라이언트 간에 세션 연결이 성립되어 통신이 이루어지고 있는 상태 |
|FIN_WAIT1|	클라이언트가 서버에게 연결을 끊고자 요청하는 상태|
|FIN_WAIT2|	서버가 클라이언트로부터 연결 종료 응답을 기다리는 상태|
|LAST_ACK |	호스트가 원격지 호스트의 연결 종료 요구 승인을 기다리는 상태 |
|TIME_WAIT|	연결이 종료되었지만 당분간 소켓을 열어 놓은 상태|

<br>

**Step 3. Attacker 가상머신에서 Slowloris.py를 생성**

<br>

**Step 4. Victim 가상머신에서 패킷 정보, 웹 서버 상태 정보, 네트워크 상태 정보를 확인**

<br>

**Step 5. Victim 가상머신에서 Request Timeout 모듈을 제거 후 아파치를 재실행**

<br>

**Step 6. 다시 공격을 시도하면 해당 웹 페이지로 접속되지 않는 것을 확인**


---

```tip
공격이 원활히 진행되지 않는 경우 @Attacker 가상머신의 iptables 설정을 확인
효율적으로 공격이 진행될 수 있도록 RST 패킷이 외부로 전달되지 않도록 설정 

└─$ sudo iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP
```
```
┌──(kali㉿kali)-[~]
└─$ sudo iptables -L

[sudo] password for kali: 
Chain INPUT (policy ACCEPT)
target     prot opt source              destination         

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination         
DROP       tcp  --  anywhere             anywhere             tcp flags:RST/RST
                                          
```
