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


SVM은 두 개의 다른 클래스를 분류할 수 있는 여러가지 결정 경계(Decision Boundary)중에 가장 잘 분류할 수 있는 결정 경계를 찾습니다.<br>
**잘 분류한다는 것**(결정 경계의 조건)은 서포트 벡터(Support Vector)로부터 거리가 가장 먼 결정 경계를 찾는 것 입니다.(Margin이 가장 큰 값일 때)<br>어느 한쪽에 치우치지 않게 분류하며, 빈 공간이라도, 양쪽 군집과 균등한 위치에 있어야합니다. 

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

<center><img src='https://user-images.githubusercontent.com/76420201/156563288-d653cf05-ddcb-490e-886e-6b7df8f4d00d.png' width=120%"></center>

<br>
데이터 세트가 선형으로 분리 될 때 소프트 마진 SVM이 더 좋아질 것으로 기대합니다. 그 이유는 하드 마진 SVM에서 단일 이상치가 경계를 결정할 수 있기 때문에 분류자가 데이터의 노이즈에 지나치게 민감하게 만듭니다.

- 하드 마진을 할 경우 빨간색 이상치가 경계를 결정하며 과적합을 일으키는 경우
<center><img src='https://user-images.githubusercontent.com/76420201/156518004-3931f475-9457-4c2a-baed-bff822789e79.png' width="25%"></center>

## 커널(Kernel)

- 커널 종류: 선형, 다항식, 가우시안, 시그모이드

### 1. 다항식(Polynomial)

몇몇 데이터들은 선형SVM으로 분류하기 어려운 데이터들이 있습니다. 커널 기법은 데이터를 더 높은 차원으로 이동시켜 데이터를 분류하는 방법입니다.

- `(x,y)`처럼 2차원의 좌표를 3차원의 좌표로 변환
- 더 높은 차원으로 변형하여 초평면 결정 경계를 얻을 수 있습니다.

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


## REFERENCE
[https://hleecaster.com/ml-svm-concept/](https://hleecaster.com/ml-svm-concept/)

[https://techblog-history-younghunjo1.tistory.com/78](https://techblog-history-younghunjo1.tistory.com/78)

[https://muzukphysics.tistory.com/entry/ML-8-%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-SVM-%EA%B8%B0%EB%B3%B8-%EA%B0%9C%EB%85%90%EA%B3%BC-%EC%9E%A5%EB%8B%A8%EC%A0%90-Support-Vector-Machine]
(https://muzukphysics.tistory.com/entry/ML-8-%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-SVM-%EA%B8%B0%EB%B3%B8-%EA%B0%9C%EB%85%90%EA%B3%BC-%EC%9E%A5%EB%8B%A8%EC%A0%90-Support-Vector-Machine)