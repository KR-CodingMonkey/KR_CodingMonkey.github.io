---
title: Support Vector Machine
tags: 
 - Machine Learning
 - SVM
 - SVC
 - ML
 - 인공지능(AI)
 - Model
 - Decision Boundary
 - Supervised Learning
description: SVM(Support Vector Machine)
permalink: docs/ML/SVM
---

# SVM(Support Vector Machine)
- SVM은 Support Vector와 Hyperplane(초평면) 이용하여 분류를 하는 알고리즘
- SVM: 서포트 벡터 머신, Support Vector Machine
    - SVC: Support Vector Classifier, 범주형 변수일 경우
    - SVR: Support Vector Regression, 연속형 변수일 경우
    - 보통 SVM 자체는 범주형 변수일 때를 일컫습니다.

<center><img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOpA-9pXmR7jRJCd_PJ9H8p7L8BD3CgPzDklXD2e0E5_Du9ZTp4mPPLXwuSj7HySpGfd4&usqp=CAU' width="50%"></center><br>


SVM의 목적은 두 개의 다른 클래스를 가장 잘 분류할 수 있는 결정 경계(Decision Boundary)를 찾는 것입니다.<br>
**잘 분류한다는 것**(결정 경계의 조건)은 **서포트 벡터(Support Vector)**로부터 거리가 가장 먼 결정 경계를 찾는 것인데(**Margin**이 가장 큰 값일 때)<br>어느 한쪽에 치우치지 않게 하며, 빈 공간이라도 양쪽 군집과 균등한 위치에 있어야 합니다. 

## 결정 경계(Decision Boundary)

- 클래스를 분류하기 위한 경계
- 2차원의 결정 경계는 선, 3차원은 평면, 그 이상은 **초평면(Hyperplane)**이라고 부릅니다.
    - 초평면은 시각적으로 표시할 수 없음

<img src = 'https://i0.wp.com/hleecaster.com/wp-content/uploads/2020/01/svm01.png?fit=1024%2C806' width="45%">
<img src = 'https://i0.wp.com/hleecaster.com/wp-content/uploads/2020/01/svm02.png?fit=1024%2C852' width="50%">

## 마진(Margin)

- 마진(margin): 결정 경계와 서포트 벡터 사이의 거리
- 서포트 벡터는 결정 경계와 가장 가까이 있는 데이터 Vector들을 의미합니다.

<center><img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FJyfbT%2FbtqEqtpxbch%2FflfwGbM7mgv1kP1kkn4nQK%2Fimg.png" width = "40%"></center><br>


SVM은 데이터들을 올바르게 분리하면서 마진의 크기를 최대화해야 하기 때문에, 이상치(Outlier)들을 잘 다루는게 중요합니다.<br> 여기서 **하드 마진(Hard margin)**과 **소프트 마진(Soft margin)**이라는 개념이 나옵니다.

- 하드 마진
    - 결정 경계와 서포트 벡터의 거리가 좁은 마진
    - 과적합(Overfitting)을 야기할 수 있음

- 소프트 마진: 
    - 결정 경계와 서포트 벡터의 거리가 넓은 마진
    - 과소적합(Underfitting)을 야기할 수 있음 

<center><img src='https://hyunkyung12.github.io/files/soft%20margin%20SVM.PNG' width="80%"></center><br>

**하드마진 VS 소프트마진**
<br>
데이터 세트가 선형으로 분리 될 때 소프트 마진 SVM이 더 좋아질 것으로 기대합니다. 하드 마진 SVM에서 단일 이상치가 경계를 결정할 수 있기 때문에 분류자가 데이터의 노이즈에 지나치게 민감하게 만들기 때문입니다.

- 하드 마진을 할 경우 빨간색 이상치가 경계를 결정하며 과적합을 일으키는 경우
<center><img src='https://user-images.githubusercontent.com/76420201/156518004-3931f475-9457-4c2a-baed-bff822789e79.png' width="25%"></center>

## 커널(Kernel)

선형으로 분리할 수 있는 경우와 그렇지 않은 경우가 있는데 지금까지는 선형으로 분리할 수 있는 경우의 예시만 보여드렸습니다.<br> 
선형으로 분리할 수 없는 경우에는 비선형 SVM을 써야 하는데 어떻게 구축할 수 있을지가 핵심이고 관측 데이터들을 더 높은 차원의 데이터로 변환시켜서 분류해 보자는 아이디어가 제시되었습니다.

- 커널 기법은 데이터를 더 높은 차원으로 이동시켜 데이터를 분류하는 방법
- 커널 종류: 선형, 다항식, 가우시안, 시그모이드(Sigmoid)

### 1. 다항식(Polynomial)

- `(x,y)`처럼 2차원의 좌표를 3차원의 좌표로 변환
- 더 높은 차원으로 변형하여 초평면 결정 경계를 얻을 수 있음

<center><img src="https://user-images.githubusercontent.com/76420201/156521828-38e85f49-d536-4aa0-9854-e2d350e70326.png" width="50%"></center>

<center><img src="https://www.sallys.space/image/svm/2.png" width="60%"></center>

### 2. 가우시안 커널(RBF: Radial Bias Function, Gaussian kernel)

- 성능이 우수하여 가장 많이 쓰이는 기법
- 2차원의 좌표를 무한한 차원의 좌표로 변환
- gamma: SVM 가우시안 커널의 파라미터
    - 값이 클수록 유연 -> 오버피팅 위험
    - 값이 작을수록 뻣뻣 -> 언더피팅 위험

<center><img src="https://datascienceschool.net/_images/13.03%20%EC%BB%A4%EB%84%90%20%EC%84%9C%ED%8F%AC%ED%8A%B8%20%EB%B2%A1%ED%84%B0%20%EB%A8%B8%EC%8B%A0_39_0.png" width = "60%"></center>



## 정리

- SVM은 서포트 벡터(Support Vector)로부터 Margin이 가장 큰 결정 경계(Decision Boundary)를 찾아 두 클래스를 분류하는 알고리즘
- 고차원 데이터의 분류문제의 좋은 성능을 보임
- 범주형 데이터, 수치형 데이터의 분류 문제에 사용 가능
- 예측이 어떻게 결정되었는지 이해하기 어렵고 모델을 분석하기도 어려움

## REFERENCE
[https://hleecaster.com/ml-svm-concept/](https://hleecaster.com/ml-svm-concept/)<br>
[https://techblog-history-younghunjo1.tistory.com/78](https://techblog-history-younghunjo1.tistory.com/78)<br>
[김성범 [핵심 머신러닝]SVM모델](https://youtu.be/qFg8cDnqYCI)