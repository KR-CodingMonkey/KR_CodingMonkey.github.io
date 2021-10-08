---
title: 네트워크
tags: 
 - CS
 - Network
description: Network
permalink: /docs/CS/Network
---

# 네트워크 / 운영체제

---

**OSI 7계층**

<center><img src='https://user-images.githubusercontent.com/33534771/74589801-e603cf00-504b-11ea-862c-765c57d3169b.png' width='60%'></center>

상위층(7,6,5) : 데이터를 만들어내는게 주된업무
- 7 계층(응용 계층): 사용자와 직접 상호작용하는 응용 프로그램들이 포함된 계층
- 6 계층(표현 계층): 데이터의 형식(Format)을 정의하는 계층
- 5 계층(세션 계층): 컴퓨터끼리 통신을 하기 위해 세션을 만드는 계층
<br>

하위층(4,3,2) : 데이터를 전송하는게 주된업무
- 4 계층(전송 계층): 최종 수신 프로세스로 데이터의 전송을 담당하는 계층
- 3 계층(네트워크 계층): 패킷을 목적지까지 가장 빠른 길로 전송하기 위한 계층
- 2 계층(데이터링크 계층): 데이터의 물리적인 전송과 에러 검출, 흐름 제어를 담당하는 계층
<br>



- 1 계층(물리 계층): 데이터를 전기 신호로 바꾸어주는 계층(하드웨어적인 부분)

<br/><br/>

**DNS(Domain Name System)**
- 도메인 이름과 IP 주소의 대응 관계를 데이터베이스 형태로 저장하고 제공하는 서비스 
- 네트워크 상에서 사람이 기억할 수 쉽게 문자로 만들어진 도메인을 컴퓨터가 처리할 수 있는 IP주소로 바꾸는 시스템

    ex ) www.naver.com -> 125.209.222.141

<br/><br/>

**TCP / UDP**

UDP
- 전송 방식은 너무 단순해서 서비스의 신뢰성이 낮고, 데이터그램 도착 순서가 바뀌거나 중복되거나 누락이 되기도한다.
- 일반적으로 오류의 검사와 수정이 필요 없는 프로그램에서 사용한다.

TCP
- 전송 제어 프로토콜은 인터넷에 연결된 컴퓨터에서 실행되는 프로그램 간에 통신을 안정적으로, 순서대로, 누락없이 교환할 수 있게 합니다.
- TCP는 UDP보다 느리지만 안전합니다.

<center><img src = "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F9a0c2%2FbtqKIpf6QGI%2Fv5akvGVZj4kVVvAzLVThF1%2Fimg.png" width = "70%"></center>

<br/><br/>

**GET / POST**

GET
- GET은 서버로부터 정보를 조회하기 위해 설계된 메소드
- 데이터를 헤더에 추가하여 전송하는 방식
- URL에 데이터가 노출되기 때문에 보안적으로 중요한 데이터를 포함해서는 안됩니다.
- GET은 불필요한 요청을 제한하기 위해 요청이 캐시될 수 있습니다

POST
- POST는 리소스를 생성/변경하기 위해 설계된 메소드
- 데이터를 바디에 추가하여 전송하는 방식 
- POST 요청은 GET과 달리 대용량 데이터를 전송할 수 있습니다.
- 완전히 안전하다는 것은 아니지만 URL에 데이터가 노출되지 않아 GET보다는 안전합니다.


<br/><br/>

**HTTP(Hyper Text Transfer Protocol)**

HTTP는 텍스트 기반의 통신 규약으로 인터넷에서 데이터를 주고받을 수 있는 프로토콜입니다.
- HTTP 메시지는 HTTP 서버와 HTTP 클라이언트에 의해 해석이 된다.
- TCP/ IP를 이용하는 응용 프로토콜이다.
- HTTP는 연결 상태를 유지하지 않는 비연결성 프로토콜이다. (Cookie와 Session이 등장)
- HTTP는 연결을 유지하지 않는 프로토콜이기 때문에 요청/응답 방식으로 동작한다.

<center><img src='https://mdn.mozillademos.org/files/13691/HTTP_Response.png' width='70%'></center>
x
<br/><br/>

