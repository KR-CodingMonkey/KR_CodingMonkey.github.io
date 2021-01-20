# OSI 7계층

OSI 7 계층은 네트워크에서 통신이 일어나는 과정을 7단계로 나눈 것을 말한다

*계층을 나눈 이유는 통신이 일어나는 과정이 단계별로 파악할 수 있기 때문이다.
흐름을 한눈에 알아보기 쉽고, 사람들이 이해하기 쉽고, 7단계 중 특정한 곳에 이상이 생기면 다른 단계의 장비 및 소프트웨어를 건들이지 않고도 이상이 생긴 단계만 고칠수 있기 때문이다.

(이해하기 쉬워서 교육용 자료로 사용됨)

![OSI7layer](https://user-images.githubusercontent.com/76420201/105174881-8751aa00-5b66-11eb-9d86-b55b0eb09e62.png)


## OSI 7 Layer Model

상위층(7,6,5) : 데이터를 만들어내는게 주된업무 (Linux수업에서 중요함)
하위층(4,3,2) : 데이터를 전송하는게 주된업무 (Network수업에서 중요함)
   
컴퓨터안에서는 2계층까지만 작업함.<br/>
1계층은 전달 (하드웨어적인 부분)

<br>

### 상위계층

---

- Application(응용계층, 7 Layer) : 사용자에게 네트워크 서비스를 제공해주는 계층

- Presentation(표현계층, 6 Layer) :	
  - 사람과 컴퓨터 사이에서 알아볼 수 있는 형태로 변환 (기계어로 바꿔주고, 기계어를 다시 알아볼수있게 바꿔준다)
  - 부가적 기능 : 데이터의 암호화, 데이터의 압축
  
- Session(연결계층, 5 Layer)

	application 간의 연결을 담당<br/>
	(서로대화할수 있는 방을만드는 그안에서 대화를 주고받는데, 어플리케이션안에서 연결을 담당, 통신을하기 위해서 어플리케이션안에서 방을만듬, 게임,카톡 등)


### 하위계층 

---

하위계층 - 계층마다 주소를 따로 사용

- Transport(전송계층, 4 Layer)
	
	- 데이터의 분할과 조합이 일어나는 계층
	   (한번의 전달할수있는 최대데이터 크기 = MTU, Maximum Transmisson Unit)
	   (분할후 받기쉽게 번호를 붙여줌, 데이터의 순서번호 = Sequence Number)

	- 데이터 전송방식을 결정하는 계층
           TCP : 확인하면서 전송(ACK = 확인메세지, ACK가 안오면 다시보냄, 손실거의x)
	   UDP : 확인하지 않고 쭉쭉 보냄(손실 가능성이 있음)

			TCP		UDP
	   신뢰성(확인)      O		 x 
     		속도	↓		 ↑

	일반적으로 TCP방식을 쓰지만, 급할경우 UDP쓸수도 있음.
	음성데이터같은경우 처리속도가 빨라야 하기 때문에 UDP사용

	● Network 서비스를 구분해주는 계층
	   -주소 port (2byte) : 1~1023 Well-known port (80 : http 를 이용)
	   -장비 L4 switch (4계층에서 데이터를 부를때 segment 라고 부른다)
		 port - tcp - data
              -Data unit segment

- Network(네트워크 계층, 3 Layer)
	
	● 네트워크 통신경로를 만들어주는 계층
	   Routing - 통신경로를 만들어주는 작업

	● 논리적주소를 사용하여 통신하는 계층
	   주소 - IP(4byte)
	   장비 - Router, L3 switch 
	   data unit - Packet
	

- Data(2 Layer)

	● 데이터의 포장방식을 결정하는 계층
	   LAN - Ethernet
	   WAN - HDLC(Cisco에서 개발한 포장방식), PPP(표준으로 채택된 방법)

	● 물리적주소를 사용하여 통신하는 계층
	   주소 - MAC(6byte)
	   장비 - Switch, Bridge(포트개수가 적어서 거의 사용안함)
	   Data unit - Frame

	출발지 주소 - source address
	도착지 주소 - destination address

5. Physical Layer(물리적 계층) 

	● 위에서 만들어진 프레임을 전기적 신호로 바꿔서 
	   매개체를 통해 다른 장비로 전달하는 실질적인 계층

	   주소 - 없음
	   장비 - cable, Hub, Repeater
	   Data unit - bit
