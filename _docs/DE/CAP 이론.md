---
title: CAP 이론
tags: 
 - Data Engineer
 - Consistency
 - Availability
 - Partition tolerance
 - NoSQL
description: Data Engineer
permalink: /docs/DE/CAP
---

# CAP 이론

- 분산컴퓨팅 환경은 **일관성, 가용성, 분단 내성**이라는 3가지 특징을 가지고 있으며, 이중 두가지만 만족할 수 있다는 이론
- 분산시스템에 내재하는 제약사항을 분석한 이론

<center><img src="https://miro.medium.com/max/1400/1*djklTxhAf1Jfu_moetZNeg.png" width="45%"></center>

- 일관성(Consistency): 모든 노드들은 같은 시간에 동일한 항목에 대하여 같은 내용의 데이터를 사용자에게 보여준다
- 가용성(Availability): 모든 사용자들이 읽기 및 쓰기가 가능해야 하며, 몇몇 노드의 장애 시에도 다른 노드에 영향을 미치면 안된다.
- 분단 내성(Partition tolerance): 클러스터가 여러 대 동작하고 있을 때, 해당 클러스터 사이에 접속이 단절되어 서로 통신을 할 수 없는 상황
에서도 시스템이 잘 동작해야 한다.

## Pick Two

1. C+A
- P를 포기 -> 네트워크 통신장애를 허용하지 않음
- 메시지 손실을 방지하는 강한 신뢰형
- RDBMS, Oracle..

2. C+P
- A를 포기 -> 노드의 장애를 혀용하지 않음
- 데이터 보다는 성능이 중요한 퍼모먼스형
- MongoDB, BigTable..

3. A+P
- C를 포기 -> 데이터의 일관성을 포기
- 일관성을 크게 요하지 않는 서비스에 적합
- DynamoDB, Cassandra.. 


## SQL vs NoSQL

관계형 데이터베이스(RDBMS)은 일관성(C)와 가용성(A)를 챙기고, 분단 허용성(P)를 포기하는 형태인 CA시스템이다. 
같은 경우 동시에 다량의 서버를 운용하는 클러스터링에 적합하지 않는다.

[dfsf](https://dongwooklee96.github.io/post/2021/03/26/cap-%EC%9D%B4%EB%A1%A0%EC%9D%B4%EB%9E%80/)