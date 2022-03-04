---
title: 운영체제(OS)
tags: 
 - CS
 - OS
description: Operating System
permalink: /docs/CS/OS
---

# 운영체제(OS)

---

### 운영체제(OS, Operating System)

운영체제란 컴퓨터 하드웨어 바로 윗단에 설치되는 소프트웨어를 말한다.

<center><img src = "https://camo.githubusercontent.com/48fa22ffe1a5a518a734aca3ba8c3ba2763eb862936ecdc57f077ed5c8cc756a/68747470733a2f2f6b2e6b616b616f63646e2e6e65742f646e2f626a686164532f627471766e473438774c672f43424a4e644f614a6144415a6c7430724b356a4d52312f696d672e706e67" width="70%"></center>

기능 
- 컴퓨터 시스템 내의 자원을 효율적으로 관리하는 것
    - CPU 스케줄링 : 어떤 프로그램에게 CPU를 줄 것인가?
    - 메모리 관리 : 한정된 메모리를 어떻게 나누어 사용할 것인가?
    - 파일 관리 : 디스크에 파일을 어떻게 보관할 것인가?
    - 입출력 관리 : 각기 다른 입출력 장치와 컴퓨터 간에 어떻게 정보를 주고 받을 것인가?
    - 프로세스 관리: 프로세스의 생성과 삭제, 자원 할당 및 반환, 프로세스 간 협력
    - 그 외 (보호 시스템, 네트워킹, 명령어 해석기)
    
- 컴퓨터 시스템을 편리하게 사용할 수 있는 환경을 제공하는 것
- 사용자 및 프로그램들 간에 자원이 형평성 있게 분배되도록 하는 균형자 역할도 제공한다.
- 사용자와 운영 체제 자신을 보호하는 역할을 담당.

<br/><br/>

### REST
- 웹에 존재하는 모든 자원(문서, 이미지, 동영상 등)에 고유한 URI를 부여해 활용하는 것으로 자원을 정의하고 자원에 대한 주소를 지정하는 방법론
- 웹의 기존 기술과 HTTP 프로토콜을 그대로 활용하기 때문에 웹의 장점을 최대한 활용할 수 있는 아키텍처 스타일이다.
- 서버와 클라이언트가 데이터를 주고받는 형식은 json, xml, text, rss 등이 있으며 Key와 Value를 활용하는 json을 주로 사용한다.
- HTTP 메소드(POST, GET, PUT, DELETE)를 통해 CRUD(Create, Read, Update, Delete) 연산을 수행한다.
- Resource(URI), Method, Representation of Resource 세 가지 구성 요소를 갖는다.
    - HTTP URI(Uniform Resource Identifier)를 통해 자원(Resource)을 명시하고,
    - HTTP Method(POST, GET, PUT, DELETE)를 통해    
    - 해당 자원(URI)에 대한 CRUD Operation을 적용하는 것을 의미합니다.

<br/><br/>

### REST API
- REST의 특징을 기반으로 API를 제공하는 것
- 공공데이터, 구글 맵, 마이크로 서비스 등 대부분이 REST API를 통해 제공한다.
- HTTP 표준을 기반으로 구현하기 때문에 HTTP를 지원하는 프로그램 언어를 사용하여 클라이언트와 서버를 구현할 수 있다.

<br/><br/>

### RESTful API
- REST의 규칙(6가지)을 잘 지켜서 설계된 API를 RESTful API라고 한다.
- 이해하기 쉽고 사용하기 쉬운 REST API를 만드는 것을 목적으로 성능이 중요하다면 꼭 RESTful하게 구현할 필요는 없다.

<br/><br/>

### 프로세스 / 쓰레드

프로세스
- 정의
    - 컴퓨터에서 연속적으로 실행되고 있는 컴퓨터 프로그램
    - 메모리에 올라와 실행되고 있는 프로그램의 인스턴스
- 특징
    - 운영체제로부터 독립된 메모리 영역을 할당받는다.
    - 프로세스들은 독립적이기 때문에 통신하기 위해 IPC(Inter-Process Communication)를 사용해야 한다.
    - 프로세스에는 최소한 1개의 쓰레드가 있다

<center><img src="https://gmlwjd9405.github.io/images/os-process-and-thread/process.png" width="50%"></center>

<br>

쓰레드
- 정의
    - 프로세스 내에서 할당받은 자원을 이용해 동작하는 실행 단위
- 특징
    - 프로세스 내에 존재하며 프로세스가 할당받은 자원을 이용하여 실행된다.
    - 쓰레드는 프로세스 내에서 Stack만 따로 할당 받고, Code, Data, Heap영역은 공유한다.
    - 쓰레드는 자원을 공유하기 때문에 다른 쓰레드에 의한 결과를 즉시 확인할 수 있다.

<center><img src="https://gmlwjd9405.github.io/images/os-process-and-thread/thread.png" width="50%"></center>

<br/><br/>  

### 컨텍스트 스위칭(Context Switching)

현재 진행하고 있는 Task(Process, Thread)의 상태를 저장하고 다음 진행할 Task의 상태 값을 읽어 적용하는 과정이다.

- 컴퓨터는 메모리에 해야 할 여러 일(프로세스)들을 늘어놓고 하나씩 가져와서 처리한 다음 일이 끝나면 다시 메모리에 돌려준다.
- 이 때, CPU는 한 번에 하나의 일만 처리할 수 있지만 Task를 빠르게 바꿔가며 실행하기 때문에 동시에 처리하는 것으로 보인다.

<br/><br/>

### 멀티 프로세스 / 멀티 쓰레드

멀티 프로세스
- 하나의 작업(Task)을 다수의 프로세스가 나누어서 동시에 처리하는 것(병렬)
- 특징
    - 하나의 프로세스에 문제가 생겨도 다른 프로세스의 영향을 주지 않는다
    - Context Switching 과정에서 캐쉬 메모리 초기화 등 무거운 작업이 진행되고 많은 시간이 소모되는 등의 오버헤드가 발생하게 된다.
    - 프로세스는 독립되어 있기 때문에 통신이 어렵다(IPC)

<br>

멀티 쓰레드
- 하나의 프로세스에 여러 쓰레드로 자원을 공유하며 작업을 나누어 수행하는 것
- 특징
    - 메모리를 공유하기 때문에 자원을 효율적으로 관리할 수 있다
    - 프로세스를 위해 자원을 할당하는 시스템콜이나 Context Switching의 오버헤드를 줄일 수 있다.
    - 하나의 쓰레드에 문제가 생기면 전체 쓰레드가 영향을 받는다
    - 여러 쓰레드가 동시에 하나의 자원에 접근하는 경우 자원 공유(동기화)의 문제가 발생할 수 있다.

<center><img src="https://user-images.githubusercontent.com/58318041/91327464-82c7d600-e800-11ea-818e-faf42b7ff162.png" width='50%'></center>

<br/><br/>

**멀티 프로세스 대신 멀티 쓰레드를 사용하는 이유**

- 프로그램 여러개를 키는 것보다 하나의 프로그램 안에서 여러 작업을 해결하는 것이 좋음
- 프로세스간의 통신(IPC)보다 쓰레드 간의 통신이 비용과 부담이 적다.
- 프로세스를 생성하여 자원을 할당하는 시스템 콜이 줄어들어 자원을 효율적으로 사용할 수 있음
    - 프로세스 간의 Context Switching시 단순히 CPU레지스터 교체 뿐만 아니라 RAM과 CPU 사이의 캐쉬 메모리에 대한
    데이터까지 초기화되므로 오버헤드가 큼

