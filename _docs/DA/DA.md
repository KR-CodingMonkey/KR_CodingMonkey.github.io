---
layout: page
title: Data Analysis
permalink: docs/DA
---

## 1. Load data & Library


```python
import pandas pd
from sklearn.ensemble import RandomForestRegressor
 :
import numpy as np

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
```

## 2. 탐색적 자료분석(EDA, Exploratory Data Analysis)

### 2.1 수치
`pd.DataFrame.head()`<br>
- 데이터 프레임의 위에서 부터 n개 행을 보여주는 함수
- n의 기본 값(default 값)은 5

`pd.DataFrame.shape`<br>
- 데이터 프레임의 행의 개수와 열의 개수가 저장되어 있는 값

`pd.DataFrame.info()`<br>
- 데이터셋의 column별 정보를 알려주는 함수
    - 비어 있지 않은 값은 (Non-null)의 개수
    - column의 type (int, float, object, etc.)

`pd.DataFrame.describe()`<br>
- 숫자형 column들의 기술 통계량을 보여주는 함수
- 기술통계량: column을 대표할 수 있는 통계값
    - count: non-nulld의 개수
    - mean: 평균값
    - std: 표준편차
    - min, max: 최솟, 최댓값 (이상치 포함)
    - 3분위수(quantile)
        - 25%(Q1): 1/4번째 지점에 있는 값
        - 50%(Q2): 중앙값
        - 75%(Q3): 3/4번째 지점에 있는 값
- 이상치(Outlier): 울타리 밖에 있는 값
    - [more..](DA/outlier)

<center><img src = 'https://miro.medium.com/max/10125/1*NRlqiZGQdsIyAu0KzP7LaQ.png' width='70%'></center>

`pd.DataFrame.groupby()`<br>
- 집단에 대한 통계량

### 2.1 그래프
`import matplotlib.pyplot as plt`


- 색깔

| 색깔 | 약자 | | 마커|의미|
|--------|-----|-|-----|-----|
| blue | b|| . | 점 |
|green|g||o|원|
|red|r||v|역삼각형|
|cyan|c||^|삼각형|
|megenta|m||s|사각형|
|yellow|y||*|별|
|black|k||x|엑스|
|white|w||d|다이아몬드|

- 마커

| 마커 | 의미 |
|--------|-----|
|^|삼각형|
|s|사각형|
|*|별|
|x|엑스|
|d|다이아몬드|

-선 

| 문자열 | 약자 |
|--------|-----|
| - |실선|
|--|끊어진 실선|
|-.|점+실선|
|:|점선|