---
title: 개발언어(python)
tags: 
 - python
 - programming
description: 개발언어(Python)
permalink: docs/CS/Python
---

# 개발언어 (Python)

### Framework / Library
- Framework(프레임워크)
    - 프레임워크는 뼈대나 기반구조를 뜻하고, 제어의 역전 개념이 적용된 기술
    - 소프트웨어의 특정 문제를 해결하기 위해서 상호 협력하는 클래스와 인터페이스의 집합
    - 객체 지향 개발을 하게 되면서 통합성, 일관성의 부족이 발생되는 문제를 해결하기 위한 방법 중 하나  
<br/>

- Library(라이브러리)
    - 단순 활용 가능한 도구들의 집합
    - 개발자가 만든 클래스를 호출  
<br/>

- Framework와 Library의 차이
    - 제어 흐름(Flow)의 대한 주도성이 누구에게/어디에 있는지 따라 구분
    - 프레임워크는 들어가서 사용하는 느낌
    - 라이브러리는 가져다가 쓰는 것 

<br/>

---

### 컴파일러 / 인터프리터
- 컴파일러
    - 전체 프로그램을 스캔해서 기계어로 한 번에 번역한다
    - 소스 코드를 분석하는 데 많은 시간이 걸리지만 실행시간은 비교적 빠르다 (실행 파일이 생성된다)
    - 연결을 위한 중간 객체코드를 생성하기 때문에 더 많은 메모리가 필요하다
    - 한번에 번역하기 때문에 디버깅이 비교적 어렵다
    - C, C++, C#, JAVA, COBOL  
<br/>

- 인터프리터
    - 한 줄씩 번역한다 
    - 소스코드를 분석하는 데 걸리는 시간은 적지만 실행 시간은 느리다 (매번 실행할 때마다 같은번역을 진행한다)
    - 중간 객체 코드가 생성되지 않아 메모리가 효율적
    - 디버깅이 용이하다
    - Python, Ruby, Basic, JavaScript, SQL, HTML

<br/>

---

### Python Standard Sorting Algorithm
- Timsort: 삽입정렬 + 병합정렬
- 평균 시간복잡도, 최악의 경우 시간 복잡도 = O(nlogn)
- Timsort는 정렬 아고리즘의 단점을 최대한 극복하기 위해 고안된 알고리즘
- python, java, swift 등 많은 프로그래밍 언어에서 표준 정렬 알고리즘으로 사용됨

<br/>

---

### 오버라이딩(Overriding) / 오버로딩(Overloading)
완전히 다른 개념이지만 이름이 헷갈림

- 오버라이딩(Overriding)
    - 클래스의 상속 시 부모 클래스에서 정의한 메소드를 자식 클래스에서 변경하는 것
<br/>

- 오버로딩(Overloading)
    - 동일한 이름의 함수를 매개변수에 따라 다른 기능으로 동작하는 것 (다형성)

<br/>

---

### GIL, Global Interpreter Lock

- 파이썬 인터프리터가 하나의 Thread만 하나의 바이트 코드를 실행 시킬 수 있도록 해주는 장치
- 하나의 Thread에 모든 자원을 할당하고 Lock을 걸어서 다른 Thread를 실행할 수 없게 막음

<center><img src = 'https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbAMe0O%2FbtqHOZLSxjm%2Fg3KOLQOBuZAFZQ5tz5OrK0%2Fimg.png' width='50%'></center>

위 그림은 python에서 3개의 Thread가 동작하는 예시인데, 하나의 Thread가 동작할 때 다른 Thread들은 동작을 멈추게 됩니다.

<br>

**Global Interpreter Lock을 쓰는 이유**

python에서는 메모리 관리를 garbage collection과 reference counting을 통해서 하게 됩니다.
https://ssungkang.tistory.com/entry/python-GIL-Global-interpreter-Lock%EC%9D%80-%EB%AC%B4%EC%97%87%EC%9D%BC%EA%B9%8C

<br/>

---

### 가비지 컬렉션, 컬렉터(Garbage Collection, GC)

- 메모리 관리 방법 중 하나로, 시스템에서 더이상 사용하지 않는 동적메모리 블럭을 찾아가 자동으로 다시 사용 가능한 자원으로 회수하는 것
- 시스템에서 가비지 컬렉션을 수행하는 부분을 가비지 컬렉터(Garbage Collector)라고 부름

프로그램은 실행될 때 메모리를 관리하는 OS에 필요한 메모리를 요청합니다. 이때 OS는 프로그램 실행에 필요한 메모리를 어디에 저장할지 그 주소를 할당해줍니다.

기존에 가리키고 있던 메모리를 새롭게 선언하거나 형변환을 하면서 다른 주소를 가리키게 되어 정리되지 않는 메모리가 생겨버리게 됩니다. 
이렇게 프로그램이 돌아가면서 메모리 누수가 발생하게 되는데,  파이썬에서는 기본적으로 **레퍼런스 카운팅(Reference Counting)**을 통해 GC를 수행하고 메모리를 관리합니다.

- 레퍼런스 카운팅(Reference Countion): 모든 객체는 참조될 때 레퍼런스 카운트가 증가하고, 참조가 해제될 때 감소된다. 값이 0이 되면 메모리에서 해제
