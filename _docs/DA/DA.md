---
layout: page
title: Data Analysis
permalink: docs/DA
---

## 1. Load data & Library

ML 기초를 다룹니다.

```python
import pandas pd
from sklearn.ensemble import RandomForestRegressor
 :

train = pd.read_csv('train.csv')
test = pd.read_csv('test'.csv')
```

## 2. 탐색적 자료분석(EDA, Exploratory Data Analysis)

`pd.DataFrame.head()`<br>
- 데이터 프레임의 위에서 부터 n개 행을 보여주는 함수
- n의 기본 값(default 값)은 5