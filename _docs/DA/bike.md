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

print(train.info())
'''
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
'''
```

## EDA 

```python
print(train.head())

'''
   id  hour  hour_bef_temperature  hour_bef_precipitation    ...    hour_bef_ozone  hour_bef_pm10  hour_bef_pm2.5  count
0   3    20                  16.3                     1.0    ...              0.027           76.0            33.0   49.0   
1   6    13                  20.1                     0.0    ...              0.042           73.0            40.0  159.0   
2   7     6                  13.9                     0.0    ...              0.033           32.0            19.0   26.0   
3   8    23                   8.1                     0.0    ...              0.040           75.0            64.0   57.0   
4   9    18                  29.5                     0.0    ...              0.057           27.0            11.0  431.0  
'''
```

### 시간별 평균 따릉이 사용량

```python
train_group = train.groupby('hour').mean()
plt.plot(train_group['count'], 'o-')
plt.grid()
plt.title('count by hour')
plt.xlabel('hour')
plt.ylabel('count')
plt.axvline(8, color='r')
plt.axvline(18, color='r')
```
- 출/퇴근 시간에 사용량 증가 (8시, 18시)
![Figure_1](https://user-images.githubusercontent.com/76420201/155281864-d3071577-deaa-4352-99ab-ad0bae64b8ef.png)


### 변수간의 상관계수
```python
import seaborn as sns
plt.figure(figsize=(9,9))
sns.heatmap(train.corr(), annot=True)
plt.show()
```
- `count`와 `hour`, `hour_bef_temperature`, `hour_bef_windspeed`, `hour_bef_ozone` 상관계수가 비교적 높음
<center><img src="https://user-images.githubusercontent.com/76420201/155283947-edd9ac7d-061b-4894-bff6-2bfd254944a6.png" width="75%"></center>


### 컬럼별 결측치 개수 확인
- `hour`, `hour_bef_temperature`, `hour_bef_windspeed`, `hour_bef_ozone` 네 가지 변수로만 학습

```python
train_X = train[['hour', 'hour_bef_temperature', 'hour_bef_windspeed', 'hour_bef_ozone']]
train_y = train[['count']]

print(train_X.isnull().sum())
'''
hour                     0
hour_bef_temperature     2
hour_bef_windspeed       9
hour_bef_ozone          76
dtype: int64
'''
```

## Pre Processing
- train 데이터의 결측치는 train 데이터 평균 값으로 대체
- test 데이터는 실제로는 **알 수 없는 값**이기 때문에 train 데이터의 평균 값으로 대체

```python
print(train_X.isnull().sum())
train_X['hour_bef_temperature'].fillna(train_X['hour_bef_temperature'].mean(), inplace=True)
train_X['hour_bef_windspeed'].fillna(train_X['hour_bef_windspeed'].mean(), inplace=True)
train_X['hour_bef_ozone'].fillna(train_X['hour_bef_ozone'].mean(), inplace=True)


test_X = test[['hour', 'hour_bef_temperature', 'hour_bef_windspeed', 'hour_bef_ozone']] # train과 동일

print(test_X.isnull().sum())
test_X['hour_bef_temperature'].fillna(train_X['hour_bef_temperature'].mean(), inplace=True)
test_X['hour_bef_windspeed'].fillna(train_X['hour_bef_windspeed'].mean(), inplace=True)
test_X['hour_bef_ozone'].fillna(train_X['hour_bef_ozone'].mean(), inplace=True)
```


## Select Model & Predict
- 
```python
model = RandomForestRegressor(n_estimators=50, random_state=0)
model.fit(train_X, train_y)

pred = model.predict(test_X)

sub = pd.read_csv('submission.csv')
sub['count'] = pred

sub.to_csv('output.csv', index=False)
```