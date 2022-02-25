---
title: Random Forest
tags: 
 - Machine Learning
 - Random Forest
 - bagging
 - ML
 - Big Data
 - 인공지능(AI)
 - Model
 - ensemble
description: Random Forest
permalink: docs/ML/RandomForest
---


# 랜덤 포레스트(Random Forest)
- Decision Tree는 overfitting될 가능성이 높다는 약점을 가지고 있습니다. 가지치기를 통해 트리의 최대 높이를 설정해 줄 수 있지만 이로써는 overfitting을 충분히 해결할 수 없습니다.
- Bagging 또는 임의 노드 최적화(Randomized node optimization)와 같은 기술을 통해 단점을 극복, 성능을 일반화 합니다.
- 랜덤 포레스트는 일반화 된 트리를 만들기 위해 다수의 결정 트리들을 학습하는 앙상블 방법입니다. 
- 랜덤 포레스트는 검출, 분류, 그리고 회귀 등 다양한 문제에 활용 됩니다.


## 배깅(Bagging, Bootstrap aggregating)
- 배깅: 부트스트랩을 통해 서로 다른 훈련 데이터로 훈련된 기초 분류기들을 결합시키는 방법
- 부트스트랩: 주어진 훈련 데이터에서 중복을 허용하는 원 데이터셋과 같은 크기의 데이터셋을 만드는 과정
    1. 부트스트랩을 통해 T개의 훈련 데이터셋을 생성
    2. T개의 트리들을 훈련
    3. 트리들을 하나의 분류기(랜덤 포레스트)로 결합한다(평균 or 과반수를 채택)

<center><img src='https://upload.wikimedia.org/wikipedia/commons/c/c7/Randomforests_ensemble.gif'></center>


## 매개변수

`sklearn.ensemble.RandomForestClassifier`<br>
`sklearn.ensemble.RandomForestRegressor`

1. 트리의 개수, n_estimators
    - 포레스트를 몇 개의 트리로 구성할 지 설정하는 변수
    - T가 작으면 시간이 짧게 걸리지만 일반화 성능이 떨어질 수 있음 
    - Defalut = 100 (version 0.22)

<br>
2. Featrue의 개수, max_feature
    - 트리하나의 선택할 feature의 개수
    - max_feature의 값이 너무 크면 트리들의 상관성이 커짐(안좋음)
    - max_feature의 값이 작으면 트리들의 모양이 달라져서 overfitting을 피할 수 있음
    - 일반적으로 Defalut(= sqrt(n_features)) 값을 따름

<br>
3. 트리 최대 깊이, max_depth
    - 하나의 트리에서의 최대 깊이를 설정하는 변수
    - 너무 낮으면 underfitting, 너무 크면 overfitting을 야기
    - Defalut = None, 모든 노드가 leaf node가 되거나 node에 샘플이 min_samples_split 미만이 될 때까지 확장 

