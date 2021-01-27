
# Slowloris Attack


**Step 1. Victim 가상머신에서 네트워크 상태를 모니터링**

```
┌──(kali㉿kali)-[/var/www/html/bWAPP]
└─$ watch "netstat -pant"  
```

![slowloris](https://user-images.githubusercontent.com/76420201/105925447-8ac3c480-6083-11eb-9d32-a8c568352850.gif)


- netstat [option]
    - p	: 해당 프로토콜을 사용하고 있는 프로그램을 표시
    - a	: 모든 연결 및 수신 대기 포트 표시
    - n	: 주소나 포트 형식을 숫자로 표현
    - t	: TCP로 연결된 포트를 표시

**Step 2. Attacker 가상머신에서 브라우저로 Victim 가상머신의 아파치로 접속

|-|-|
|LISTEN 	|	서버의 데몬이 떠 있어서 클라이언트의 접속 요청을 기다리고 있는 상태 (LISTENING)|
|SYN_RECV | 서버가 클라이언트로부터 접속 요구SYN)를 받아 클라이언트에게 응답(SYN/ACK)를 보낸 상태|
|ESTABLISHED |	서버와 클라이언트 간에 세션 연결이 성립되어 통신이 이루어지고 있는 상태 |
|TIME_WAIT|	연결이 종료되었지만 당분간 소켓을 열어 놓은 상태|
|LAST_ACK |	호스트가 원격지 호스트의 연결 종료 요구 승인을 기다리는 상태 |
|FIN_WAIT1|	클라이언트가 서버에게 연결을 끊고자 요청하는 상태|
|FIN_WAIT2|	서버가 클라이언트로부터 연결 종료 응답을 기다리는 상태|