---
title: Data Type
tags: 
 - CS
 - BigData
 - Data Engineer
 - Data Type
 - Qualitative
 - Quantitative
 - Continuous
 - Ordinal
 - Categorical
 - Numerical
description: Data Type
permalink: /docs/DE/datatype
---


# 데이터 타입(Data Type)

<center><img src="https://studyonline.unsw.edu.au/sites/default/files/field/image/types%20of%20data.png"></center>

데이터 분석 시 다양한 데이터 타입들을 볼 수 있습니다.

- Qualitative(질적), Categorical(범주형)
    - Nomial(명목형): 순서가 없는 범주
    - Ordinal(순서형): 순서가 있는 범주

- Quantitative(양적), Numerical(수치형)
    - Discrete(불연속적, 이산형): 연속되지 않는 수치
    - Continuous(연속형): 연속되는 수치

<br>

## 1. 명목형 데이터(Nominal Data)

- 순서가 없는 범주형 데이터
- 성별(남/녀), 혈액형(A, B..), 요일(월, 화, 수..)
- 카테고리를 숫자로 표현한다면, 월:1, 화:2, 수:3 ... 일:7
- 2(화)>1(월)이라는 관계가 성립되지 않음  

<br>

## 2. 순서형 데이터(Ordinal Data)

- 순서가 있는 범주형 데이터
- 학년(1, 2, 3, 4), 좌석 등급(R, S, A ..)
- 좌석 등급을 숫자로 표현하면, R:5, S:4, A:3
- 5(R) > 4(S) 라는 순서관계가 성립
- 카테고리를 숫자로 표현할 시 합리적인 변환이 필요함

<br>

## 3. 이산형 데이터(Discrete Data)

- 연속되지 않는 수치형 데이터
- 수치적인 의미를 가지나 소수점의 형태로 표현할 수 없는 데이터
- 사람(1명, 2명..), 불량품(1대, 2대..)

<br>

## 4. 연속형 데이터(Continous Data)

- 연속되는 수치형 데이터
- 수치적으로 의미가 있고 소수점으로 표현되는 데이터
- 키, 몸무게, 나이
- 데이터 수집 방법에 따라 데이터 타입이 다를 수 있음
    - 29살, 18살: 연속형 데이터
    - 20대, 30대: 순서형 데이터


<center><img width="650" alt="DT" src="https://user-images.githubusercontent.com/76420201/158094169-c9d295d0-5739-4015-a7a5-39d13c076e2b.PNG" width="120%"></center>


## REF

[https://junklee.tistory.com/10](https://junklee.tistory.com/10)
[https://studyonline.unsw.edu.au/blog/types-of-data](https://studyonline.unsw.edu.au/blog/types-of-data)