
# TCP syn Flooding

공격자가 SYN패킷만 계속해서 전달


Step 1. Victim 가상머신에서 syncookie 사용을 확인 후 사용을 해제

`sudo sysctl -a | grep syncookies`

net.ipv4.tcp_syncookies = 1

syncookie를 사용하면 backlog que가 가득 차 있어도 정보를 계속 쌓을 수 있다.