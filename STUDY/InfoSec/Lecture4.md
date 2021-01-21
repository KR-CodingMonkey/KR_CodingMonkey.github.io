
# 패킷 분석

WireShark를 통한 패킷 분석 방법을 알아본다.

## TCP

[1] Protocol이 TCP 인걸 찾아서 클릭하면 TCP에 관한 정보가 나오게 됩니다.

![wireshark-tcp1](https://user-images.githubusercontent.com/76420201/105362187-eafad680-5c3d-11eb-82ef-59c278888f06.GIF)

<br/>

[2]

![wireshark-tcp2](https://user-images.githubusercontent.com/76420201/105362478-49c05000-5c3e-11eb-8d11-c853efa93033.GIF)

- Src Port(Source port) : 발신지 포트, 위의 패킷의 경우 443(HTTPS 포트)

- Dst Port(Destination port) : 목적지 포트, 56759 포트

- Seq(Sequence number) : 와이어샤크에서는 Seq번호를 쉽게 구분하기 위해서 상대번호라는 것을 사용한다. 상대번호는 1씩 증가 하게 됩니다. 그림에서는 1354가 상대번호 입니다.

- Seq (raw) : TCP에서는 데이터를 보낼때 마다 각 데이터에 고유한 번호를 부여해서 전송을 시도한다. 이 고유한 번호가 바로 Sequence Number이다. 전송중 순서가 바뀌어서 수신되는 경우 이를 **순서대로 재구성**할 수 있게 되는 것이다. 이 순차번호는 패킷에 포함되있는 데이터 만큼 증가하게 됩니다. 예를 들어 5000byte 짜리 파일을 전송하는 경우를 살펴보자. 이 때의 MSS가 100byte라고 생각하면 TCP는 5000 byte짜리 파일을 전송하기 위해 50개의 세그먼트를 생성하게 될 것이다. (5000 / 100 = 50). 이런 경우 TCP는 각 세그먼트의 Sequence Number Field에 Byte 기준 번호를 붙인다. 즉, 첫 번째 세그먼트의 Sequence number가 0이라 가정하면 두 번째 세그먼트는 100번, 세번째 세그먼트는 200번의 식으로 Sequence number가 설정된다. 화면에서는 1354의 값을 가집니다. 3840871932가 절대 번호입니다.

- Ack(Acknowledgment number) : 확인 응답 번호 필드는 다음번에 기대되는 순차번호를 표시한다. ack number에 관련하여 1078의 값을 가지게 됩니다.

- Header length : 데이터 오프셋필드는 TCP헤더의 길이를 정의합니다. 길이는 4byte씩 증가되고, 이 필드의 값이 20이면 80바이트 길이를 갖는다는 것입니다. TCP헤더의 길이가 다양하게 변화시킬 필요가 있으므로 이 필드가 필요하게 됩니다.

<br/>

[3] Flag

![wireshark-tcp3](https://user-images.githubusercontent.com/76420201/105363729-b4be5680-5c3f-11eb-8dd7-18062bc4bda9.GIF)

URG (Urgent) : 긴급 포인터, 잘 사용하지 않음, 만약 이 플래그가 1일경우 긴급포인터 필드로 정의되는 특정위치에서 시작하는 패킷의 데이터를 알기 위해 발신자가 원하는 수신자를 나타냄, 이게 무슨말이지? (fix-it)

ACK (Acknowledgment) : 확인 응답 패킷, flag가 1일경우 해당 패킷은 확인응답이라는 것을 나타냅니다.

PSH (Push) : 네트워크에서 버퍼링 우회와 데이터 즉시 통과, 이 플래그는 TCP 세그먼트가 발신자나 수신자의 측면에서 버퍼에 유지되면 안 된다는 것을 표시합니다.

RST (Reset) : 연결 닫기, RST 비트 설정에 대한 TCP 패킷은 TCP 연결을 종료, 즉 접속을 강제로 종료합니다. 이 패킷은 이상 종료 시 사용됩니다.

SYN (Synchronize) : 동기화 순차번호, SYN 비트는 송신측과 수신측의 일련번호를 확인할 때 사용되고 이 비트가 1이면 이 패킷은 TCP 핸드셰이크 프로세스의 SYN 단계라는 뜻입니다.

FIN (Finish) : 트랜잭션 종료, Finish 비트는 프로세스가 완료됐고 데이터 스트림이 전송 됐다는 것을 의미합니다.

<br/>

[4]

![wireshark-tcp4](https://user-images.githubusercontent.com/76420201/105363740-b720b080-5c3f-11eb-805a-aefd878595c0.GIF)


## UDP

## ICMP

## DNS


<!-- ## ARP Poison 분석 방법 

ARP 스푸핑(ARP spoofing)은 근거리 통신망(LAN) 하에서 주소 결정 프로토콜(ARP) 메시지를 이용하여 상대방의 데이터 패킷을 중간에서 가로채는 중간자 공격 기법이다. 이 공격은 데이터 링크 상의 프로토콜인 ARP 프로토콜을 이용하기 때문에 근거리상의 통신에서만 사용할 수 있는 공격이다.

이 기법을 사용한 공격의 경우 특별한 이상 증상이 쉽게 나타나지 않기 때문에 사용자는 특별한 도구를 사용하지 않는 이상 쉽게 자신이 공격당하고 있다는 사실을 확인하기 힘들다.

### ARP Spoofing 발생 증상

---

(1) 피해 시스템에서의 증상

 - 네트워크 속도 저하
 - 악성코드가 웹 페이지 시작 부분에 위치
 - 정기적인 ARP 패킷 다량 수신

 (2) 공격 시스템에서의 증상

 - 네트워크 사용량 증가
 - 정기적인 ARP 패킷 발송
 - 악성 프로그램의 프로세스 동작

 <br/>

 ### 피해 탐지 방법

 (1) ARP table을 통한 MAC주소 중복 확인

 - ARP Spoofing공격이 실행될 때 서버의 ARP 패킷을 분석하면 필요 이상의 reply패킷이 있습니다. 서버는 지속적으로 G/W와 통신하기 때문에 MAC의 주소가 ARP table에서 삭제되지 않기 때문에 request가 없는 reply패킷만 수신되지 않습니다. -->


<!-- 출처: https://soldier5683.tistory.com/18 [White-hacker] -->