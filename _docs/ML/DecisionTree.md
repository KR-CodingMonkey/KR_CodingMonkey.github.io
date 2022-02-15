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
- 지도학습 모델, 분류 규칙을 통해 데이터를 분류(Classification), 회귀(Regression)
    - 분류 트리는 리프 노드에 속한 특정 클래스의 레이블을 결정하는 반면,회귀 트리의 경우 리프 노드에 속하는 데이터의 평균값을 이용해 예측값을 계산한다는 차이점이 있습니다.


![DecisionTree](https://s3.amazonaws.com/codecademy-content/programs/data-science-path/decision-trees/tree_gif.gif)

위 그림은 의사결정트리의 예시로서,
- X: Hours Slept, Plans to Cheat, Hours Studied, Average Grade 
- y: Got an A

X 데이터를 통해 y를 예측하는 모델이 만들어지는 과정입니다.

Decision Tree는 Root Node, Intermediate Node, Terminal Node(=Leaf Node)로 구성이 되어 있습니다.<br> **Root Node**는 맨 처음 분류 기준, **Intermediate Node**는 중간 분류 기준, **Terminal Node(=Leaf Node)**는 결과 값이 됩니다.

모델의 성능을 높이기 위해선 데이터를 잘 분류해야 하고,<br>
불순도(Impurity)계산을 통해 분류 기준을 정량화 하여 비교/선정 할 수 있습니다.

## 불순도(Impurity)

### 지니 불순도(Gini Impurity)

## Information Gain(정보 획득)

- 위 구성방법을 사용하여 트리를 형성하게 되면, leaf 노드가 순도 100%의 한가지 범주만을 가지게 되는 Full tree(최대 트리)를 형성하게 된다.
- 하지만 이러한 최대 트리는 새로운 데이터에 적용할 때 과적합 문제(Overfitting)가 발생하여 일반화 성능이 떨어지게 된다.
- 따라서 형성된 결정트리에 대해 가지치기(Pruning)를 수행하여 일반화 성능을 높힌다.
## 가지치기

## 마치며