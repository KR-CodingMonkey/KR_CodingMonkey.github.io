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

불순도를 수치적으로 나타탤 수 있는 지수는 대표적으로 Gini와 Entropy가 있습니다.

### 지니(Gini)

fomula: 
<center><img width="168" alt="giniindex" src="https://user-images.githubusercontent.com/76420201/153979958-5f76cf94-d5fc-40c4-8161-8c53ad5f34ea.PNG"></center>

Gini index interval:
<center><img width="270" alt="gini_minmax" src="https://user-images.githubusercontent.com/76420201/153979997-b5089352-94c7-4274-b7ad-4db2aaca81c4.PNG"></center>

### 엔트로피(Entropy)

fomula: 
<center><img width="209" alt="entropy" src="https://user-images.githubusercontent.com/76420201/153980029-f5392b0e-7867-49e6-88d8-44cdcabd792d.PNG"></center>

Entropy interval:
<center><img width="351" alt="entropy_minmax" src="https://user-images.githubusercontent.com/76420201/153980062-deb2a12c-8518-498f-b4b0-0dbc4e3076a8.PNG"></center>

<br>

Entropy는 로그를 사용하기 때문에 조금 더 복잡하고 오래 걸립니다. 성능은 Entropy가 약간 우세하지만 차이가 크게 나지 않기 때문에 **Gini가 더 낫다**는 평가입니다. 
[more...](https://quantdare.com/decision-trees-gini-vs-entropy/)

## Information Gain(정보 획득)

- 위 구성방법을 사용하여 트리를 형성하게 되면, leaf 노드가 순도 100%의 한가지 범주만을 가지게 되는 Full tree(최대 트리)를 형성하게 된다.
- 하지만 이러한 최대 트리는 새로운 데이터에 적용할 때 과적합 문제(Overfitting)가 발생하여 일반화 성능이 떨어지게 된다.
- 따라서 형성된 결정트리에 대해 가지치기(Pruning)를 수행하여 일반화 성능을 높힌다.

## 가지치기

## 마치며