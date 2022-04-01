---
title: K-Nearest Neighbor Algorithm
tags: 
 - Machine Learning
 - ML
 - Big Data
 - 인공지능(AI)
 - Model
 - KNN
description: K-Nearest Neighbor Algorithm
permalink: docs/ML/kNN
---

# K-최근접 이웃 알고리즘 (KNN, K-Nearest Neighbor Algorithm)
- KNN 알고리즘은 input_data로부터 거리가 가까운 k개의 다른 데이터의 레이블을 참조하여 분류하는 알고리즘
- 거리를 측정할 때 **유클리디안 거리** 계산법을 활용
- KNN 간단하지만 이미지 처리, 글자 인식, 영화나 음악 추천 알고리즘 등 많은 분야에서 사용됨

<center><img src='http://i.imgur.com/gLBo1gX.png'></center><br>

위의 이미지에서 볼 수 있듯이 유사한 데이터 포인트끼리 서로 거리가 가깝다는 것을 알 수 있습니다.<br>
KNN은 이러한 가정을 토대로 고안된 알고리즘입니다.<br>
데이터 포인트 간의 거리를 계산하는 방법은 여러가지 있지만, 일반적으로 대중적이고 친숙한 유클리드 거리를 사용합니다.     

## 모델 개요

KNN의 하이퍼파라미터는 `k`(탐색할 이웃 수)와 `거리 측정 방법` 두 가지 입니다. <br>
k가 작을 경우 데이터의 직역적 특성을 지나치게 반영하여 overfitting의 위험이 있습니다.<br>
반대로, k값이 너무 클 경우는 지나치게 정규화가 되어 underfitting의 위험이 있습니다.<br>

아래 그림처럼 k의 크기에 따라(k=1, k=15) 경계면이 단순해지는 것을 확인할 수 있습니다. 

<center><img src='https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbAtIiM%2FbtqP4kPIND2%2FDkjRlEnb69KEDKUwXOoYxK%2Fimg.png' width='80%'></center>

## 최적의 K값
데이터에 적합한 k를 선택하기 위해서 k의 범위를(ex. 1~100) 지정하고, 각 k에 대하여 KNN알고리즘을 여러 번 실행하여 오차를 가장 작게 하는 k값을 선택합니다.

<center><img src='https://i.imgur.com/j4EsgY8.png'></center>


## 장단점
- 장점
    - 알고리즘이 간단하고 구현하기 쉬움
    - 모델을 구축하거나 여러 매개변수를 조정할 필요가 없음
    - 알고리즘이 다양해서 분류, 회귀 및 검색에 사용할 수 있음
- 단점
    - 변수의 수가 증가함에 따라 상당히 느려짐

## Recommender system
At scale, this would look like recommending products on Amazon, articles on Medium, movies on Netflix, or videos on YouTube. Although, we can be certain they all use more efficient means of making recommendations due to the enormous volume of data they process.
However, we could replicate one of these recommender systems on a smaller scale using what we have learned here in this article. Let us build the core of a movies recommender system.


## Reference
https://m.blog.naver.com/bestinall/221760380344
https://ratsgo.github.io/machine%20learning/2017/04/17/KNN/