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

데이터 분석 시 다양한 데이터 타입들을 볼 수 있습니다.

<center><img src="https://studyonline.unsw.edu.au/sites/default/files/field/image/types%20of%20data.png" width="80%"></center>
<br>

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
- 카테고리를 척도로 나타내면, 월:1, 화:2, 수:3 ... 일:7
- 2(화)>1(월)이라는 관계가 성립되지 않음
- 한 그룹에 속하면 다른 그룹에 속하지 않는 상호배타적이 관계  

<br>

## 2. 순서형 데이터(Ordinal Data)

- 순서가 있는 범주형 데이터
- 학년(1, 2, 3, 4), 좌석 등급(R, S, A ..)
- 좌석 등급을 척도로 나타내면, R:5, S:4, A:3
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

<br>

## 5. 구간 데이터(Interval Data)

- nominal data와 ordered data(순서형)의 특성을 가지고 있지만 정량화 할 수 있고 데이터 간의 차이를 수치로 나타낼 수 있습니다.
- 수치끼리 더하거나 뺄 수 있지만 곱하거나 나눌 수는 없습니다. 
    - ex) 20도 X 2는 40도가 아닙니다.
- Interval Data의 0이라는 척도는 존재하지 않음을 의미하는 것이 아니라 의미가 있는 데이터로 인지해야 합니다. 
    - ex) 시간 00:00, 온도 0도
- 데이터 간격은 동일한 의미를 가집니다.
    - ex) 12:30-13:00 = 14:15-14:45 (30분)

<br>

### 6. 비율 데이터(Radio Data)

- 비율 데이터 ex) 키, 무게, 높이, 거리 
- 더하기, 빼기, 곱하기, 나누기 가능
- 비율데이터의 0은 없음을 의미합니다. (키와 몸무게가 0혹은 음수가 될 수 없음)

## 정리

명목 척도는 값에 레이블을 지정하거나 설명하는 데 사용됩니다. 
서수 척도는 데이터 포인트의 특정 순서에 대한 정보를 제공하는 데 사용되며 주로 만족도 조사에서 볼 수 있습니다. 
간격 척도는 순서와 차이점을 이해하는 데 사용됩니다. 
비율 척도는 동일성, 순서 및 차이에 대한 추가 정보와 함께 각 데이터 포인트 내의 수치적 세부 사항에 대한 분석을 제공합니다.

<br>
<center><img width="650" alt="DT" src="https://user-images.githubusercontent.com/76420201/158094169-c9d295d0-5739-4015-a7a5-39d13c076e2b.PNG" width="110%"></center>

<br>

## REF

[https://studyonline.unsw.edu.au/blog/types-of-data](https://studyonline.unsw.edu.au/blog/types-of-data)