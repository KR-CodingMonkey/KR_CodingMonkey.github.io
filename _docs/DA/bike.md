---
title: 서울시 따릉이 자전거 이용 예측
tags: 
 - Data analysis
 - Dacon
 - 따릉이
 - RandomForestRegressor
description: 서울시 따릉이 자전거 이용 예측 AI모델 
permalink: docs/DA/Bike
---

# (공공)서울시 따릉이 자전거 이용 예측 AI모델

데이터 분석 과 머신러닝을 처음 접하시는 분들<br>  
혹은 데이콘 대회를 연습으로 경험해보고 싶으신 분들은<br> 
해당 대회를 통해 각 날짜의 1시간 전의 기상상황을 활용 하여 따릉이 대여수를 예측해 보세요.

**데이터 셋**: [서울시 따릉이 데이터](https://dacon.io/competitions/open/235576/data)

## Load Data
```python
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
```

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1459 entries, 0 to 1458
Data columns (total 11 columns):
 #   Column                  Non-Null Count  Dtype  
---  ------                  --------------  -----
 0   id                      1459 non-null   int64
 1   hour                    1459 non-null   int64
 2   hour_bef_temperature    1457 non-null   float64
 3   hour_bef_precipitation  1457 non-null   float64
 4   hour_bef_windspeed      1450 non-null   float64
 5   hour_bef_humidity       1457 non-null   float64
 6   hour_bef_visibility     1457 non-null   float64
 7   hour_bef_ozone          1383 non-null   float64
 8   hour_bef_pm10           1369 non-null   float64
 9   hour_bef_pm2.5          1342 non-null   float64
 10  count                   1459 non-null   float64
 ```