
# UDP / TCP  

UDP와 TCP에 대해서 자세하게 다룸

## UDP(User Datagram Protocol)

- UDP는 전송 방식은 너무 단순해서 **서비스의 신뢰성이 낮고, 데이터그램 도착 순서가 바뀌거나 중복되거나 누락**이 되기도한다.

- 일반적으로 **오류의 검사와 수정이 필요 없는 프로그램**에서 사용한다.

<img src = "https://user-images.githubusercontent.com/76420201/105715658-37595580-5f61-11eb-8295-9612a4a8911e.png">

UDP 프로토콜은 간단하게 생겼습니다.

- 출발지 포트, 목적지 포트: 2byte * 2 → 응용 계층에 속하는 프로토콜의 종류가 65536개
- 길이(length): UDP 페이로드와 UDP 헤더를 더한 데이터 그램의 크기
- 오류검사(checksum): 기본적으로 비활성화 

UDP 사용하는 대표적인 프로그램 : RIP 프로토콜, DNS 서버, tftp 서버

<br>

## TCP(Transmission Control Protocol)

- TCP 전송 제어 프로토콜은 인터넷에 연결된 컴퓨터에서 실행되는 프로그램 간에 통신을 **안정적으로, 순서대로, 누락없이** 교환할 수 있게 합니다.

- TCP는 UDP보다 느리지만 안전합니다. (체감할 만큼의 속도 차이가 나지는 않는다)

<center><img src = "https://user-images.githubusercontent.com/76420201/105715665-39231900-5f61-11eb-94d4-c5ec9e540e0f.jpg"></center>

- 출발지 포트, 목적지 포트: 2byte * 2

- 일련 번호(sequence number): 
    - 전송하는 데이터의 순서를 의미 → 수신측에서 쪼개진 세그먼트의 순서를 파악해서 재조립할 수 있도록 제공 
    - 최초로 데이터를 전송할 때는 랜덤한 수로 초기화하고, 이후에는 자신이 보낼 데이터의 1바이트 당 일련번호를 1씩 증가시켜서 데이터의 순서를 표현
    - 확인 또는 승인 번호(acknowledgment number):
    - 수신자가 예상하는 다음 시퀀스 번호를 의미 ⇒ 다음에 보내줘야 하는 데이터의 시작점
    - 연결 설정과 연결 해제 때 발생하는 핸드쉐이킹 과정에서는 상대방이 보낸 시퀀스 번호 + 1 을 확인 번호로 설정
    - 실제 데이터를 주고 받을 때는 상대방이 보낸 시퀀스 번호 + 자신 받은 데이터의 바이트 수 를 확인 번호로 설정

- 오프셋(offset)
    전체 세그먼트에서 헤더가 아닌 데이터가 시작되는 위치를 표시

- TCP 플래그(flags)
    현재 세그먼트의 속성을 나타낸다.
    |-|-|
    |CWR (Congestion Window Reduced)	|	혼잡 윈도우 크기 감소 신호|
    |ECN (Explicit Congestion Notification) |	혼잡 발생 신호|
    |URG (Urgent)			|		긴급 데이터|
    |ACK (Acknowledgment)	|			확인 응답 신호|
    |PSH (Push)				|	수신측에 데이터를 최대한 빠르게 응용 프로그램에게 전달|
    |RST (Reset)			|		연결을 강제로 리셋해달라는 요청|
    |SYN (Synchronize)		|		연결을 생성|
    |FIN (Finish)			|		연결을 종료|

- 윈도우 크기(windows size): 한번에 전송할 수 있는 데이터의 양(크기)
- 오류 검사(checksum): 데이터 송수신 중에 발생하는 오류를 검출하기 위해 사용
- 긴급 포인트(urgent pointer): URG 플래그사 설정된 경우, 해당 데이터를 우선 처리

