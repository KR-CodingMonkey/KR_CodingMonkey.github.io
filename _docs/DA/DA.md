---
layout: page
title: Data Analysis
permalink: docs/DA
---

## 1. 데이터 & 라이브러리 불러오기(Load data & Library)


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

<center><img src="https://s3.amazonaws.com/files.dezyre.com/images/Tutorials/Split+Apply+Combine+Strategy.png" width="60%"></center>

### 2.1 그래프
`import matplotlib.pyplot as plt`<br>
- 데이터를 차트나 플롯(plot)으로 그려주는 라이브러리

<center><img width="438" alt="pltplot" src="https://user-images.githubusercontent.com/76420201/155242217-09643f17-a0ea-4b6b-83d4-f906d61dd841.png"></center>

<!-- - 색깔

| 문자열 | 약자 |
|--------|-----|
| blue | b|
|green|g|
|red|r|
|cyan|c|
|megenta|m|
|yellow|y|
|black|k|
|white|w|

- 마커

| 마커 | 의미 |
|--------|-----|
| . | 점 |
|o|원|
|v|역삼각형|
|^|삼각형|
|s|사각형|
|*|별|
|x|엑스|
|d|다이아몬드|

- 선 

| 문자열 | 약자 |
|--------|-----|
| - |실선|
|--|끊어진 실선|
|-.|점+실선|
|:|점선| -->

| 함수 | 설명 |
|-----|------|
|`plt.title(label, fontsize)`|그래프 제목 생성|
|`plt.xlabel(label, fontsize)` | x축 이름 설정|
|`plt.ylabel(label, fontsize)`| y축 이름 설정|
|`plt.axvline(x, color)`| 축을 가로지르는 세로선 생성|
|`plt.text(x, y, s, fontsize)`|원하는 위치에 텍스트 생성|

### 상관계수

`pd.DataFrame.corr()`<br>
- 피어슨 상관 계수(Pearson correlation coefficient)
- 상관계수: 두 개의 변수가 같이 일어나는 강도를 나타내는 수치
- [-1, 1]사이의 값을 가진다
- 분야별로 차이가 있지만, 0.4이상이면 변수간 상관성이 있다고 볼 수 있음

![상관계수](https://t1.daumcdn.net/cfile/tistory/99DEE1425C6A9F2008)
<br>

## 3. 데이터 전처리(Pre-Processing)

`pd.Series.isnull()`<br>
- 결측치 여부를 확인 (결측치 - True, else - False)

`pd.DataFrame.fillna(value)`<br>
- NA/NAN 값을 value로 채우는 함수
<br>

## 4. 변수 선택 및 모델 구축(Feature Engineering & Select Algorithm)

`sklearn.ensemble.RandomForestRegressor()`<br>
`sklearn.linear_model.LinearRegression()`<br>
`sklearn.linear_model.LogisticRegression()`<br>
                    :<br>
                    :
<br>

## 5. 모델 학습 및 검증(Model Training & Evaluation)
`model.fit(X_train, y_train)`<br>
- 모델 학습

`model.predict(y)`
- 모델 예측
<br>

## 6. 결과 및 결언


