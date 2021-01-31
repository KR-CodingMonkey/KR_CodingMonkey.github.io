
# TCP SYN Flooding

<center><img src = "https://user-images.githubusercontent.com/76420201/106401723-fbdeef80-6468-11eb-80f2-9ee8eaece9d6.jpg"></center>


TCP/IP 네트워크에서의 정상적 TCP 연결 3-way handshake 과정의 경우, 클라이언트가 원격지 서버의 특정 포트에 SYN패킷(packet)을 발송합으로써 연결을 요청하고 요청을 받은 원격 서버가 SYN/ACK 패킷으로 응답한 후 수신된 연결 요청 정보를 해당 시스템 TCP 연결 자원인 Backlog Queue내 incomplete connection queue에 저장한다.

이때 서버가 응답한 SYN+ACK에 대하여 클라이언트가 ACK로써 응답을 보내지 않으면 accept()시스템콜을 통해 클라이언트와 통신할 연결소켓을 생성하지 못하므로 서버는 incomplete connetion queue에 있던 연결 요청 정보를 수행하지 못하고 그대로 남아있다는 **half-open TCP** 연결 상태에 머무르는 구조적 취약점이 있는데 

Attacker(공격자)는 이 취약점을 이용한 서비스 거부(Dos)를 유발하는 공격을 위해서 서버 특정 포트에 SYN packet을 발송하는 과정을 대량으로 중첩시켜 Backlog Queue내 incomplete connetion queue를 가득 채움으로써 소진시키게 되고 이로인해 더 이상 새로운 클라이언트의 TCP 연결요청을 받을 수 없게 되어 이 후 요청되는 다수의 TCP 연결이 완료되지 않고 무시된다.

**공격자가 SYN패킷만 계속해서 전달**


Step 1. Victim 가상머신에서 syncookie 사용을 확인 후 사용을 해제

`sudo sysctl -a | grep syncookies`

net.ipv4.tcp_syncookies = 1

syncookie를 사용하면 backlog que가 가득 차 있어도 정보를 계속 쌓을 수 있다.