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

위의 이미지에서 볼 수 있듯이 유사한 데이터 포인트끼리 서로 거리가 가깝다는 것을 알 수 있습니다. KNN은 이러한 가정으로부터 고안된 알고리즘입니다.
KNN은 주변 이웃의 분포에 따라 예측 결과가 달라질 수 있습니다. 가장 단순한 결정 방식은 다수결(Majority voting)입니다. 이웃들 범주 가운데 빈도 기준 제일 많은 범주로 새 데이터의 범주를 예측하는 것입니다.

다른 방식으로는, 가중합(weighted voting) 방식도 있습니다. 거리(d)가 가까운(=유사도가 높은) 이웃의 정보에 좀 더 가중치를 줍니다. 1/(1+d), 1/(1+d2), exp(−d) 등 단조감소함수이기만 하면 무엇이든 가중치 산출 함수로 쓸 수 있다고 합니다.

KNN의 하이퍼파라미터는 `k`(탐색할 이웃 수)와 `거리 측정 방법` 두 가지 입니다. 
k값이 작을 경우 데이터의 직역적 특성에 민감하게 반영되어 **overfitting**의 위험이 있습니다.
반대로, k값이 너무 클 경우 지나치게 정규화 되어 **underfitting**의 위험이 있습니다. 아래 그림처럼 k값의 크기에 따라(k=1, k=15) 경계면이 단순해지는 것을 확인할 수 있습니다. 

<center><img src='https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbAtIiM%2FbtqP4kPIND2%2FDkjRlEnb69KEDKUwXOoYxK%2Fimg.png' width='80%'></center>

데이터 포인트 간의 거리를 측정하는 방법은 여러가지 있지만, 일반적으로 대중적인 유클리디안 거리를 많이 사용합니다. (거리 지표: Euclidean Distance,  Manhattan Distance, Mahalanobis Distance etc.)  


## 최적의 K값
최적의 K값은 데이터셋마다 다르기 때문에 가장 적합한 k를 찾기 위해서는 k의 범위를(ex. 1~100) 지정하고, 각 k에 대하여 KNN알고리즘을 여러 번 실행하여 오차가 가장 적게 나오는 k값을 선택해야 합니다. 학습데이터와 검증데이터(validation data)를 나누고, k값을 늘려가면서 Error rate의 변화를 확인합니다.

<center><img src='https://i.imgur.com/j4EsgY8.png' width='50%'></center>


## 장단점
- 장점
    - 알고리즘이 간단하고 구현하기 쉬움
    - 모델을 구축하거나 여러 매개변수를 조정할 필요가 없음
    - 알고리즘이 다양해서 분류, 회귀 및 검색에 사용할 수 있음
- 단점
    - 데이터(학습데이터, 테스트 데이터) 수가 증가함에 따라 상당히 느려짐
    - 변수의 개수가 많을 경우 KNN의 성능이 떨어질 수 있음


## Recommender system
At scale, this would look like recommending products on Amazon, articles on Medium, movies on Netflix, or videos on YouTube. Although, we can be certain they all use more efficient means of making recommendations due to the enormous volume of data they process.
However, we could replicate one of these recommender systems on a smaller scale using what we have learned here in this article. Let us build the core of a movies recommender system.

## KNN 수행시 주의점

## Reference
https://m.blog.naver.com/bestinall/221760380344
https://ratsgo.github.io/machine%20learning/2017/04/17/KNN/