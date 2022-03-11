---
title: Data Engineer
tags: 
 - CS
 - BigData
 - Data Engineer
 - Master Table
 - Transaction Table
 - History Table
description: Data Engineer
permalink: /docs/DE/table
---

# Master Table & Transaction Table

- 데이터베이스 시스템에는 Master와 Transaction 두 가지 유형의 테이블이 있습니다.
- 데이터 웨어하우스 혹은 데이터 레이크 구축시, 원천테이블의 종류와  특성을 파악하고 설계하는 것이 중요합니다.
- 데이터베이스 개발 중에 Master Table과 Transaction Table을 식별하여 어떻게 상호작용이 일어나는지 이해하는 것 또한 중요합니다. 

<center><img src="https://metamug.com/article/images/differ-master-vs-transaction-table.svg"></center>


## Master Table

- 기준이 되는 테이블
- 마스터 테이블은 DB를 설계할 때 가장 우선적으로 설계됩니다 
- 마스터 테이블은 시스템의 기본이 되는 테이블이기 때문에 마스터 테이블의 열과 제약조건은 시스템의 Entity를 나타냅니다.
- Ex) 고객마스터, 계정마스터..

또한 마스터 테이블은 가장 최신의 상태를 유지하고 변경이 있을때마다 주기적으로 마스터 테이블의 정보를 저장하는 History Table(이력 테이블)이 존재합니다.(가변속성들을 관리)

## Transaction Table

트랜잭션은 시스템 내 Entity(마스터 테이블)에 의해 수행되는 활동입니다.
이러한 활동은 트랜잭션 테이블에 저장되며 일반적으로 트랜잭션 테이블에는 마스터 테이블에 대한 외래 키가 있습니다.

- 주문, 출석, 판매.. 
- CREATE OR DELETE, UPDATE는 없음

