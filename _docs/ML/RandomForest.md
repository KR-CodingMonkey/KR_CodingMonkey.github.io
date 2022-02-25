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
- Bagging 또는 랜덤 노드 최적화(Randomized node optimization)와 같은 기술을 통해 단점을 극복, 성능을 일반화 합니다.
- 랜덤 포레스트는 일반화 된 트리를 만들기 위해 다수의 결정 트리들을 학습하는 앙상블 방법입니다. 
- 랜덤 포레스트는 검출, 분류, 그리고 회귀 등 다양한 문제에 활용 됩니다.


## 배깅(Bagging, Bootstrap aggregating)

- 배깅: 부트스트랩을 통해 서로 다른 훈련 데이터로 훈련된 기초 분류기들을 결합시키는 방법
- 부트스트랩: 주어진 훈련 데이터에서 중복을 허용하는 원 데이터셋과 같은 크기의 데이터셋을 만드는 과정
    1. 부트스트랩을 통해 N개의 훈련 데이터셋을 생성
    2. N개의 트리들을 훈련
    3. 트리들을 하나의 분류기(랜덤 포레스트)로 결합한다(평균 or 과반수를 채택)

<center><img src='https://upload.wikimedia.org/wikipedia/commons/c/c7/Randomforests_ensemble.gif'></center>


## 앙상블 모델(Ensemble Model)