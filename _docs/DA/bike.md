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

<!-- # [공공]서울시 따릉이 자전거 이용 예측 AI모델 -->

<!-- **데이터 셋**: [Data](https://dacon.io/competitions/open/235576/data) -->

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