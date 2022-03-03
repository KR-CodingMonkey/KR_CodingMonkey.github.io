---
title: 영화 관객수 예측 모델 개발
tags: 
 - Data analysis
 - Dacon
 - movie
 - RandomForestRegressor
description: 영화 관객수 예측 모델 개발 
permalink: docs/DA/movie
---

# (문화)영화 관객수 예측 모델 개발

영화 관객수를 예측해 보세요.

- title : 영화의 제목
- distributor : 배급사
- genre : 장르
- release_time : 개봉일
- time : 상영시간(분)
- screening_rat : 상영등급
- director : 감독이름
- dir_prev_bfnum : 해당 감독이 이 영화를 만들기 전 제작에 참여한 영화에서의 평균 관객수(단 관객수가 알려지지 않은 영화 제외)
- dir_prev_num : 해당 감독이 이 영화를 만들기 전 제작에 참여한 영화의 개수(단 관객수가 알려지지 않은 영화 제외)
- num_staff : 스텝수
- num_actor : 주연배우수
- box_off_num : 관객수


## Load Data


```python
import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv('movies_train.csv')
test = pd.read_csv('movies_test.csv')
```

## EDA


```python
train.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>distributor</th>
      <th>genre</th>
      <th>release_time</th>
      <th>time</th>
      <th>screening_rat</th>
      <th>director</th>
      <th>dir_prev_bfnum</th>
      <th>dir_prev_num</th>
      <th>num_staff</th>
      <th>num_actor</th>
      <th>box_off_num</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>개들의 전쟁</td>
      <td>롯데엔터테인먼트</td>
      <td>액션</td>
      <td>2012-11-22</td>
      <td>96</td>
      <td>청소년 관람불가</td>
      <td>조병옥</td>
      <td>NaN</td>
      <td>0</td>
      <td>91</td>
      <td>2</td>
      <td>23398</td>
    </tr>
    <tr>
      <th>1</th>
      <td>내부자들</td>
      <td>(주)쇼박스</td>
      <td>느와르</td>
      <td>2015-11-19</td>
      <td>130</td>
      <td>청소년 관람불가</td>
      <td>우민호</td>
      <td>1161602.50</td>
      <td>2</td>
      <td>387</td>
      <td>3</td>
      <td>7072501</td>
    </tr>
    <tr>
      <th>2</th>
      <td>은밀하게 위대하게</td>
      <td>(주)쇼박스</td>
      <td>액션</td>
      <td>2013-06-05</td>
      <td>123</td>
      <td>15세 관람가</td>
      <td>장철수</td>
      <td>220775.25</td>
      <td>4</td>
      <td>343</td>
      <td>4</td>
      <td>6959083</td>
    </tr>
    <tr>
      <th>3</th>
      <td>나는 공무원이다</td>
      <td>(주)NEW</td>
      <td>코미디</td>
      <td>2012-07-12</td>
      <td>101</td>
      <td>전체 관람가</td>
      <td>구자홍</td>
      <td>23894.00</td>
      <td>2</td>
      <td>20</td>
      <td>6</td>
      <td>217866</td>
    </tr>
    <tr>
      <th>4</th>
      <td>불량남녀</td>
      <td>쇼박스(주)미디어플렉스</td>
      <td>코미디</td>
      <td>2010-11-04</td>
      <td>108</td>
      <td>15세 관람가</td>
      <td>신근호</td>
      <td>1.00</td>
      <td>1</td>
      <td>251</td>
      <td>2</td>
      <td>483387</td>
    </tr>
  </tbody>
</table>
</div>



- 감독의 영향을 많이 받을것 같음 (감독의 이전 영화 관객 평균)
- 상영등급과 장르와도 작은 연관성도 있어보임(추측)


```python
train.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>time</th>
      <th>dir_prev_bfnum</th>
      <th>dir_prev_num</th>
      <th>num_staff</th>
      <th>num_actor</th>
      <th>box_off_num</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>600.000000</td>
      <td>2.700000e+02</td>
      <td>600.000000</td>
      <td>600.000000</td>
      <td>600.000000</td>
      <td>6.000000e+02</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>100.863333</td>
      <td>1.050443e+06</td>
      <td>0.876667</td>
      <td>151.118333</td>
      <td>3.706667</td>
      <td>7.081818e+05</td>
    </tr>
    <tr>
      <th>std</th>
      <td>18.097528</td>
      <td>1.791408e+06</td>
      <td>1.183409</td>
      <td>165.654671</td>
      <td>2.446889</td>
      <td>1.828006e+06</td>
    </tr>
    <tr>
      <th>min</th>
      <td>45.000000</td>
      <td>1.000000e+00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>89.000000</td>
      <td>2.038000e+04</td>
      <td>0.000000</td>
      <td>17.000000</td>
      <td>2.000000</td>
      <td>1.297250e+03</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>100.000000</td>
      <td>4.784236e+05</td>
      <td>0.000000</td>
      <td>82.500000</td>
      <td>3.000000</td>
      <td>1.259100e+04</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>114.000000</td>
      <td>1.286569e+06</td>
      <td>2.000000</td>
      <td>264.000000</td>
      <td>4.000000</td>
      <td>4.798868e+05</td>
    </tr>
    <tr>
      <th>max</th>
      <td>180.000000</td>
      <td>1.761531e+07</td>
      <td>5.000000</td>
      <td>869.000000</td>
      <td>25.000000</td>
      <td>1.426277e+07</td>
    </tr>
  </tbody>
</table>
</div>




```python
train.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 600 entries, 0 to 599
    Data columns (total 12 columns):
     #   Column          Non-Null Count  Dtype  
    ---  ------          --------------  -----  
     0   title           600 non-null    object 
     1   distributor     600 non-null    object 
     2   genre           600 non-null    object 
     3   release_time    600 non-null    object 
     4   time            600 non-null    int64  
     5   screening_rat   600 non-null    object 
     6   director        600 non-null    object 
     7   dir_prev_bfnum  270 non-null    float64
     8   dir_prev_num    600 non-null    int64  
     9   num_staff       600 non-null    int64  
     10  num_actor       600 non-null    int64  
     11  box_off_num     600 non-null    int64  
    dtypes: float64(1), int64(5), object(6)
    memory usage: 56.4+ KB
    

- dir_prev_bfnum(전 영화들의 평균 관객)을 제외한 나머지 feature에는 결측치가 없음
- dir_prev_bfnum feature 특성상 NaN과 0은 다른 의미를 가지므로 평균값으로 처리 (fillna(train[].mean())


```python
plt.figure(figsize=(20, 6))

# genre
plt.subplot(221)
train_group_genre = train.groupby('genre').mean()
plt.plot(train_group_genre['box_off_num'])
plt.grid()
plt.rc('font', family='Gulim')

# screening_rat
plt.subplot(222)
train_group_screen = train.groupby('screening_rat').mean()
plt.plot(train_group_screen['box_off_num'])
plt.grid()

# year
plt.subplot(223)
train['year'] = train['release_time'].apply(lambda x: int(x[:4]))
train_group_year = train.groupby('year').mean()
plt.plot(train_group_year['box_off_num'])
plt.grid()

# distributor
plt.subplot(224)
d_top5 = train['distributor'].value_counts()[:5]
def distributor_top5(distributor):
    if distributor not in d_top5:
        return '기타'
    else:
        return distributor
        
train['distributor'] = train['distributor'].apply(distributor_top5)
test['distributor'] = test['distributor'].apply(distributor_top5)

train_group_dis = train.groupby('distributor').mean()
plt.plot(train_group_dis['box_off_num'])
        
plt.show()
```



![output_10_0](https://user-images.githubusercontent.com/76420201/155699687-dd8e32d6-f6d6-4a97-bc49-0156b1ae7dfc.png)
    



```python
train[train['screening_rat']=='전체 관람가']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>distributor</th>
      <th>genre</th>
      <th>release_time</th>
      <th>time</th>
      <th>screening_rat</th>
      <th>director</th>
      <th>dir_prev_bfnum</th>
      <th>dir_prev_num</th>
      <th>num_staff</th>
      <th>num_actor</th>
      <th>box_off_num</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>나는 공무원이다</td>
      <td>(주)NEW</td>
      <td>코미디</td>
      <td>2012-07-12</td>
      <td>101</td>
      <td>전체 관람가</td>
      <td>구자홍</td>
      <td>23894.0</td>
      <td>2</td>
      <td>20</td>
      <td>6</td>
      <td>217866</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>6</th>
      <td>길위에서</td>
      <td>기타</td>
      <td>다큐멘터리</td>
      <td>2013-05-23</td>
      <td>104</td>
      <td>전체 관람가</td>
      <td>이창재</td>
      <td>NaN</td>
      <td>0</td>
      <td>32</td>
      <td>5</td>
      <td>53526</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1789, 바스티유의 연인들</td>
      <td>기타</td>
      <td>뮤지컬</td>
      <td>2014-09-18</td>
      <td>129</td>
      <td>전체 관람가</td>
      <td>정성복</td>
      <td>NaN</td>
      <td>0</td>
      <td>3</td>
      <td>5</td>
      <td>4778</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>17</th>
      <td>별이 빛나는 밤</td>
      <td>기타</td>
      <td>드라마</td>
      <td>2012-04-05</td>
      <td>98</td>
      <td>전체 관람가</td>
      <td>린슈유</td>
      <td>773.0</td>
      <td>1</td>
      <td>8</td>
      <td>4</td>
      <td>5693</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>32</th>
      <td>다이노 타임</td>
      <td>CJ 엔터테인먼트</td>
      <td>애니메이션</td>
      <td>2015-04-30</td>
      <td>85</td>
      <td>전체 관람가</td>
      <td>최윤석</td>
      <td>NaN</td>
      <td>0</td>
      <td>10</td>
      <td>8</td>
      <td>285084</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>578</th>
      <td>메밀꽃, 운수 좋은 날, 그리고 봄봄</td>
      <td>기타</td>
      <td>애니메이션</td>
      <td>2014-08-21</td>
      <td>90</td>
      <td>전체 관람가</td>
      <td>안재훈</td>
      <td>53235.0</td>
      <td>1</td>
      <td>167</td>
      <td>7</td>
      <td>35567</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>580</th>
      <td>정글히어로</td>
      <td>CJ 엔터테인먼트</td>
      <td>애니메이션</td>
      <td>2014-10-02</td>
      <td>82</td>
      <td>전체 관람가</td>
      <td>박태동</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>72052</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>582</th>
      <td>뽀로로 극장판 컴퓨터 왕국 대모험</td>
      <td>(주)NEW</td>
      <td>애니메이션</td>
      <td>2015-12-10</td>
      <td>62</td>
      <td>전체 관람가</td>
      <td>박영균</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
      <td>8</td>
      <td>446054</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>585</th>
      <td>후쿠시마의 미래</td>
      <td>기타</td>
      <td>다큐멘터리</td>
      <td>2015-04-09</td>
      <td>70</td>
      <td>전체 관람가</td>
      <td>이홍기</td>
      <td>NaN</td>
      <td>0</td>
      <td>4</td>
      <td>1</td>
      <td>938</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>587</th>
      <td>서유기 리턴즈</td>
      <td>기타</td>
      <td>SF</td>
      <td>2011-02-17</td>
      <td>79</td>
      <td>전체 관람가</td>
      <td>신재호</td>
      <td>67602.0</td>
      <td>1</td>
      <td>220</td>
      <td>4</td>
      <td>12696</td>
      <td>2011</td>
    </tr>
  </tbody>
</table>
<p>92 rows × 13 columns</p>
</div>



음... 그럴만 한걸로..


```python

```


```python
import seaborn as sns

sns.heatmap(train.corr(), annot=True)
plt.show()
```


    
<center><img scr= "https://user-images.githubusercontent.com/76420201/155699753-db08afe0-3326-4c35-a8a6-11a4ab9b79ae.png"></center>

    


## 데이터 전처리


```python
X_train = train[['time', 'num_staff', 'genre', 'screening_rat', 'distributor']]
X_test = test[['time', 'num_staff', 'genre', 'screening_rat', 'distributor']]
# X_test['distributor'] = X_test['distributor'].apply(distributor_top5)

y_train = train['box_off_num']

X_test.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>time</th>
      <th>num_staff</th>
      <th>genre</th>
      <th>screening_rat</th>
      <th>distributor</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>125</td>
      <td>304</td>
      <td>느와르</td>
      <td>청소년 관람불가</td>
      <td>기타</td>
    </tr>
    <tr>
      <th>1</th>
      <td>113</td>
      <td>275</td>
      <td>멜로/로맨스</td>
      <td>12세 관람가</td>
      <td>(주)쇼박스</td>
    </tr>
    <tr>
      <th>2</th>
      <td>115</td>
      <td>419</td>
      <td>드라마</td>
      <td>12세 관람가</td>
      <td>CJ 엔터테인먼트</td>
    </tr>
    <tr>
      <th>3</th>
      <td>116</td>
      <td>408</td>
      <td>액션</td>
      <td>15세 관람가</td>
      <td>(주)쇼박스</td>
    </tr>
    <tr>
      <th>4</th>
      <td>110</td>
      <td>380</td>
      <td>공포</td>
      <td>15세 관람가</td>
      <td>CJ 엔터테인먼트</td>
    </tr>
  </tbody>
</table>
</div>




```python
X_train = pd.get_dummies(X_train)
X_test = pd.get_dummies(X_test)

X_train.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 600 entries, 0 to 599
    Data columns (total 24 columns):
     #   Column                  Non-Null Count  Dtype
    ---  ------                  --------------  -----
     0   time                    600 non-null    int64
     1   num_staff               600 non-null    int64
     2   genre_SF                600 non-null    uint8
     3   genre_공포                600 non-null    uint8
     4   genre_느와르               600 non-null    uint8
     5   genre_다큐멘터리             600 non-null    uint8
     6   genre_드라마               600 non-null    uint8
     7   genre_멜로/로맨스            600 non-null    uint8
     8   genre_뮤지컬               600 non-null    uint8
     9   genre_미스터리              600 non-null    uint8
     10  genre_서스펜스              600 non-null    uint8
     11  genre_애니메이션             600 non-null    uint8
     12  genre_액션                600 non-null    uint8
     13  genre_코미디               600 non-null    uint8
     14  screening_rat_12세 관람가   600 non-null    uint8
     15  screening_rat_15세 관람가   600 non-null    uint8
     16  screening_rat_전체 관람가    600 non-null    uint8
     17  screening_rat_청소년 관람불가  600 non-null    uint8
     18  distributor_(주)NEW      600 non-null    uint8
     19  distributor_(주)마운틴픽쳐스   600 non-null    uint8
     20  distributor_(주)쇼박스      600 non-null    uint8
     21  distributor_CJ 엔터테인먼트   600 non-null    uint8
     22  distributor_기타          600 non-null    uint8
     23  distributor_롯데엔터테인먼트    600 non-null    uint8
    dtypes: int64(2), uint8(22)
    memory usage: 22.4 KB
    

## 모델 학습 


```python
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(n_estimators=200, max_depth=5)
model.fit(X_train, y_train)
```




    RandomForestRegressor(max_depth=5, n_estimators=200)



## Predict


```python
pre = model.predict(X_test)
pre[:5]
```




    array([2575828.30749279, 1073711.92769165, 1431003.928046  ,
           1867132.0040308 , 1087788.9545834 ])




```python
sub = pd.read_csv('./submission.csv')
sub['box_off_num'] = pre

sub.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>box_off_num</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>용서는 없다</td>
      <td>2.575828e+06</td>
    </tr>
    <tr>
      <th>1</th>
      <td>아빠가 여자를 좋아해</td>
      <td>1.073712e+06</td>
    </tr>
    <tr>
      <th>2</th>
      <td>하모니</td>
      <td>1.431004e+06</td>
    </tr>
    <tr>
      <th>3</th>
      <td>의형제</td>
      <td>1.867132e+06</td>
    </tr>
    <tr>
      <th>4</th>
      <td>평행 이론</td>
      <td>1.087789e+06</td>
    </tr>
  </tbody>
</table>
</div>




```python
sub.to_csv('output.csv', index=False)
```


```python

```
