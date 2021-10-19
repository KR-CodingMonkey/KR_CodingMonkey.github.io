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
2. YARB (YARN, Yet Another Resource Negotiator): 프로세싱 또는 리소스 스케줄링 서브시스템

HDFS 클러스터와 YARN 클러스터가 서로 결합된 두 시스템의 조합을 **하둡 클러스터**라고 한다.

