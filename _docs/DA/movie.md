---
title: 서울시 따릉이 자전거 이용 예측
tags: 
 - Data analysis
 - Dacon
 - 따릉이
 - RandomForestRegressor
description: 서울시 따릉이 자전거 이용 예측 AI모델 
permalink: docs/DA/movie
---

```python
import pandas as pd
import matplotlib.pyplot as plt
```


```python
pwd
```




    'C:\\Users\\ahipp\\OneDrive\\바탕 화면\\CoTe\\dacon\\2.영화_관객수_예측_모델_개발'




```python
train = pd.read_csv('movies_train.csv')
test = pd.read_csv('movies_test.csv')
```


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




```python

```
