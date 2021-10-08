---
title: Hadoop1
tags: 
 - HDFS
 - hadoop
 - Data Engineer
description: hadoop
permalink: docs/Skills/Hadoop/hadoop1
---
# HDFS, Hadoop Distributed File System 이해

대부분의 분산환경에서 동작하는 분산 플랫폼들은 Master/Slave 구조와 Master가 없는 구조로 나눌 수 있습니다.

<center><img src='https://t1.daumcdn.net/cfile/tistory/9981B2335A88438223' width="80%"></center>

<br>
Hadoop은 GFS의 아키텍처를 보고 소프트웨어 플랫폼으로 구축하였기 때문에 거의 동일한 구조를 가지고 있습니다. 

GFS의 아키텍처는 Master/Slave 구조입니다. Master/Slave의 구조에서 가장 중요한 것은 Master Server에 부하가 가지 않게 설계를 해야합니다. 그림의 표시되어 있는 굵은선(Chunk data)이 클라이언트하고 Chunk Server하고 다이렉트로 연결되게 구성이 되어 있습니다. 실제 traffic을 주고 받을 때 Master Server하고 데이터를 주고 받는 연산이 이루어 지지 않습니다. 대부분의 Master/Slave 구조를 갖는 아키텍처들의 기본적인 특성입니다. Master쪽에 장애가 생기면 전체 클러스터의 역할을 못하게 되기 때문에 Master의 안정성을 우선적으로 보장할 수 있는 아키텍처를 설계/운용을 해야 합니다.
<br/><br/>

> **병렬(Parallel Computing) / 분산(Distributed Computing)**<br/><br/>
분산과 병렬은 비슷한데, 병렬은 보다 CPU 중심으로 한 용어로 사용이 됩니다. CPU를 병렬로 처리를 하는 것에 더 의미를 강조한 용어가 **병렬(Parallel)**이고, **분산(Distributed)**은 데이터에 포커싱되어 있는 용어입니다. 
<br/><br/>데이터를 분산하고 분산된 데이터를 처리를 하면 보통 **분산 컴퓨팅(Distributed Computing)**이라고 하고<br/>데이터를 공용 스토리지에 공유해놓고 CPU코어 수나 메모리를 여러개로 늘려가면서 처리를 하는 것은 **병렬 컴퓨팅(Parallel Computing)**라고 합니다.



