---
title: Decision Tree
tags: 
 - Machine Learning
 - Decision Tree
 - information gain
 - ML
 - Big Data
 - 인공지능(AI)
 - Model
description: Decision Tree
permalink: docs/ML/DT
---

# 의사결정트리(Decision Tree)
- 결과 모델이 Tree 구조를 가지고 있다.
- 수치형 범주형 변수를 한꺼번에 다룰 수 있다.
- 지도학습 모델, 분류 규칙을 통해 데이터를 분류(Classification), 회귀(Regression)
    - 분류=최빈값, 회귀=평균
    - 분류 트리는 리프 노드에 속한 특정 클래스의 레이블을 결정하는 반면, 회귀 트리의 경우 리프 노드에 속하는 데이터의 평균값을 이용해 예측값을 계산한다는 차이점이 있습니다.

<center><img src='https://s3.amazonaws.com/codecademy-content/programs/data-science-path/decision-trees/tree_gif.gif' width="80%"></center><br>

위 그림은 의사결정트리의 예시로서,
- X: Hours Slept, Plans to Cheat, Hours Studied, Average Grade 
- y: Got an A

X 데이터를 통해 y를 예측하는 모델이 만들어지는 과정입니다.

Decision Tree는 Root Node, Intermediate Node, Terminal Node(=Leaf Node)로 구성이 되어 있습니다.<br> **Root Node**는 맨 처음 분류 기준, **Intermediate Node**는 중간 분류 기준, **Terminal Node(=Leaf Node)**는 결과 값이 됩니다.

모델의 성능을 높이기 위해선 데이터를 잘 분류해야 하고,<br>
불순도(Impurity)계산을 통해 분류 기준을 정량화 하여 비교/선정 할 수 있습니다.

## 불순도(Impurity)
- 복잡성을 의미
- 다양한 개체들이 섞여 있을수록 불순도가 높습니다.
- 분기기준을 정할 때 자식노드의 불순도가 현재노드의 불순도보다 낮게하는 기준을 분기기준으로 정해야 합니다.
- Information gain = (현재노드 불순도) - (자식노드 불순도)

불순도를 수치적으로 나타낼 수 있는 지수는 대표적으로 Gini와 Entropy가 있습니다.

### 지니(Gini)

fomula: 
<center><img width="168" alt="giniindex" src="https://user-images.githubusercontent.com/76420201/153979958-5f76cf94-d5fc-40c4-8161-8c53ad5f34ea.PNG"></center>

Gini index interval:
<center><img width="270" alt="gini_minmax" src="https://user-images.githubusercontent.com/76420201/153979997-b5089352-94c7-4274-b7ad-4db2aaca81c4.PNG"></center><br>

만약 특정 그룹에 오직 한 종류의 label만 존재한다면, 해당 그룹의 Gini Impurity는 `0`이 됩니다.<br> 데이터 분할 이후의 각 그룹의 불순도가 낮으면 낮을 수록 데이터가 잘 분류되었다고 할 수 있습니다.

### 엔트로피(Entropy)

fomula: 
<center><img width="209" alt="entropy" src="https://user-images.githubusercontent.com/76420201/153980029-f5392b0e-7867-49e6-88d8-44cdcabd792d.PNG"></center>

Entropy interval:
<center><img width="351" alt="entropy_minmax" src="https://user-images.githubusercontent.com/76420201/153980062-deb2a12c-8518-498f-b4b0-0dbc4e3076a8.PNG"></center>

<br>

Entropy는 로그를 사용하기 때문에 조금 더 복잡하고 오래 걸립니다.<br>성능은 Entropy가 약간 우세하지만 차이가 크게 나지 않기 때문에 **Gini가 더 낫다**는 평가입니다. 
[more...](https://quantdare.com/decision-trees-gini-vs-entropy/)

## 정보 이득(Information Gain)
- information gain을 계산함으로써 분류기준을 정할 수 있습니다.
    - information gain이 높을수록 데이터 분리에 있어서 중요한 변수
- information gain = (현재노드 불순도) - (자식노드 불순도)
    - `0.5` - (`0.2*0`+`0.5*0.375`+`0.3*0`) = `0.026`

<center><img src='https://s3.amazonaws.com/codecademy-content/programs/data-science-path/decision-trees/weighted_info.svg'></center><br>

이런 방식으로 모든 분류후보(feature, column)들에 대해서 information gain을 계산하고, 가장 높게 나온 분류후보를 기준으로 데이터를 분할하면 됩니다.

## 가지치기(Pruning)
- 트리의 Depth가 깊어질수록 Leaf Node가 많아지고 과적합 문제(Overfitting)가 발생하여 일반화 성능이 떨어질 수 있습니다.
- 가지치기(Pruning): Max Depth, Leaf Node 개수 등을 제한함으로써 일반화 성능을 높일 수 있습니다.

<center><img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKKu6sB7QVhZvaJNbD75WAGmpZZKJwoEV43g&usqp=CAU'></center>

## 마치며
Decision Tree는 기본적으로 greedy한 알고리즘으로 항상 최적의 트리를 생성하지는 않지만 이러한 Decision Tree는 계산복잡성 대비 좋은 성능을 보입니다.<br>
Decision Tree 모델을 사용하는 주된 요인은 어떤 feature가 중요한 영향인자인지 직관적으로 확인할 수 있고 어느만큼의 척도로 분류를 했는지 상세한 기준을 파악할 수 있다는 점입니다.


## REFERENCE
1. [https://quantdare.com/decision-trees-gini-vs-entropy/](https://quantdare.com/decision-trees-gini-vs-entropy/)
2. [https://www.codecademy.com/](https://www.codecademy.com/)