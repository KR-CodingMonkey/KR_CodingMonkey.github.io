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
permalink: /docs/DE/DataEngineer
---

# Master Table & Transaction Table

- 데이터베이스 시스템에는 Master와 Transaction 두 가지 유형의 테이블이 있습니다.
- 데이터 웨어하우스 혹은 데이터 레이크 구축시, 원천테이블의 종류와 그 특성을 파악하고 설계하는 것이 중요합니다.
- 데이터베이스 개발 중에는 Master Table과 Transaction Table을 식별하여 어떻게 상호작용이 일어나는지 이해하는 것이 중요합니다. 

## Master Table

- During database design, the master tables are designed first. Since the purpose of master tables is to capture the system. The design of the master tables i.e. its columns and constraints describe the entities in the system. For example user, account, customer etc. Generally, entities of the system are mapped to master tables.


## Transaction Table

To understand the difference between the two types we need to understand what exactly we mean by a transaction. A transaction is an activity performed by entities(master tables) within the system. These activities are captured in transaction tables and usually, these transaction entries have foreign keys to master records.

Transaction tables are designed to store events in the system.

These events are associated with master records to ensure normalization. Because the transactions can quickly grow in large numbers. The analytics tools, OLTP, partitioning are applied on transaction tables. Most of the querying is done on transaction tables.

The Pie charts, line charts, and graphs are drawn using transaction tables. The design of transaction tables.