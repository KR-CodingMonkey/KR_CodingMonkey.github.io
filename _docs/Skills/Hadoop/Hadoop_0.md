---
title: Hadoop
tags: 
 - HDFS
 - hadoop
 - Data Engineer
description: hadoop
permalink: docs/Skills/Hadoop/hadoop0
---

# Apache Hadoop

## 빅데이터, 분산 컴퓨팅 및 하둡

스파크 전문가가 되기 위해서는 하둡과 스파크를 함께 사용하는 것에 관해 이해해야 한다.

또한, 스파크에 필수적인 데이터 지역성(data locality), 비공유(shared nothing), 맵리듀스(MapReduce) 같은 하둡 프로젝트의 핵심 개념들에 관한 이해도 필요하다.


## Hadoop

- 하둡은 데이터 지역성이라는 개념에 바탕을 둔 데이터 저장 및 처리 플랫폼이다.
- 하둡은 큰 문제를 작은 문제의 집합으로 나누고 정리하며, 데이터 지역성과 비공유 개념을 적용한다.
    - 데이터 지역성: 데이터를 원격 처리 시스템이나 호스트로 보내 처리하는 처리 방식  
    - 비공유: 서버를 추가하면 서버의 대수에 비례해 성능이 증가함


## 하둡의 핵심 구성 요소

1. 하둡 분산 파일 시스템 (HDFS, Hadoop Distributed File System): 스토리지 서브시스템
2. YARN (YARN, Yet Another Resource Negotiator): 프로세싱 또는 리소스 스케줄링 서브시스템

HDFS 클러스터와 YARN 클러스터가 서로 결합된 두 시스템의 조합을 **하둡 클러스터**라고 한다.

플룸(Flume)이나 스쿱(Sqoop)과 같은 데이터 처리 프로젝트 또는 피그(Pig)나 하이브(Hive)와 같은 데이터 분석 툴처럼 하둡과 상호 작용하거나 통합하는 프로젝트를 **하둡 에코시스템** 프로젝트라고 한다.


### HDFS, Hadoop Distributed File System 이해

- HDFS는 클러스터의 하나 이상의 노드에 파일이 분산돼 있는 블록으로 구성된 가상 파일 시스템이다.

대부분의 분산환경에서 동작하는 분산 플랫폼들은 Master/Slave 구조와 Master가 없는 구조로 나눌 수 있습니다.

<center><img src='https://t1.daumcdn.net/cfile/tistory/9981B2335A88438223' width="80%"></center>

<br>
그 중 Hadoop은 GFS의 아키텍처를 보고 소프트웨어 플랫폼으로 구축하였기 때문에 거의 동일한 구조를 가지고 있습니다. 

GFS의 아키텍처는 Master/Slave 구조이다. Master/Slave의 구조에서 가장 중요한 것은 Master Server에 부하가 가지 않게 설계를 해야합니다. 그림의 표시되어 있는 굵은선(Chunk data)이 클라이언트하고 Chunk Server하고 다이렉트로 연결되게 구성이 되어 있습니다. 실제 traffic을 주고 받을 때 Master Server하고 데이터를 주고 받는 연산이 이루어 지지 않습니다. 대부분의 Master/Slave 구조를 갖는 아키텍처들의 기본적인 특성입니다. Master쪽에 장애가 생기면 전체 클러스터의 역할을 못하게 되기 때문에 Master의 안정성을 우선적으로 보장할 수 있는 아키텍처를 설계/운용을 해야 합니다.
<br/><br/>

> **병렬(Parallel Computing) / 분산(Distributed Computing)**<br/><br/>
분산과 병렬은 비슷한데, 병렬은 보다 CPU 중심으로 한 용어로 사용이 됩니다. CPU를 병렬로 처리를 하는 것에 더 의미를 강조한 용어가 **병렬(Parallel)**이고, **분산(Distributed)**은 데이터에 포커싱되어 있는 용어입니다. 
<br/><br/>데이터를 분산하고 분산된 데이터를 처리를 하면 보통 **분산 컴퓨팅(Distributed Computing)**이라고 하고<br/>데이터를 공용 스토리지에 공유해놓고 CPU코어 수나 메모리를 여러개로 늘려가면서 처리를 하는 것은 **병렬 컴퓨팅(Parallel Computing)**라고 합니다.