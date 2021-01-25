
# UDP / TCP  

UDP와 TCP에 대해서 자세하게 다룸

## UDP

UDP(User Datagram Protocol)은 전송 방식은 너무 단순해서 **서비스의 신뢰성이 낮고, 데이터그램 도착 순서가 바뀌거나 중복되거나 누락**이 되기도한다.

UDP는 일반적으로 **오류의 검사와 수정이 필요 없는 프로그램**에서 사용한다.

<img src = "https://user-images.githubusercontent.com/76420201/105715658-37595580-5f61-11eb-8295-9612a4a8911e.png">

UDP 프로토콜은 간단하게 생겼습니다.

- 출발지 포트, 목적지 포트: 2byte * 2 → 응용 계층에 속하는 프로토콜의 종류가 65536개
- 길이(length): UDP 페이로드와 UDP 헤더를 더한 데이터 그램의 크기
오류검사(checksum): 기본적으로 비활성화 

UDP 사용하는 대표적인 프로그램 : RIP 프로토콜, DNS 서버, tftp 서버

<br>

## TCP

TCP(Transmission Control Protocol) 전송 제어 프로토콜은 인터넷에 연결된 컴퓨터에서 실행되는 프로그램 간에 통신을 **안정적으로, 순서대로, 누락없이 교환할 수 있게 합니다.

TCP는 UDP보다 느리지만 안전합니다. (체감할 만큼의 속도 차이가 나지는 않는다)

<center><img src = "https://user-images.githubusercontent.com/76420201/105715665-39231900-5f61-11eb-94d4-c5ec9e540e0f.jpg"></center>

- 출발지 포트, 목적지 포트: 2byte * 2