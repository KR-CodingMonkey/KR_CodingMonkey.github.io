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
- SVM: 서포트 벡터 머신, Support Vector Machine
    - SVC: Support Vector Classifier, 범주형 변수일 경우
    - SVR: Support Vector Regression, 연속형 변수일 경우
    - 보통 SVM 자체는 범주형 변수일 때를 일컫습니다.

<center><img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOpA-9pXmR7jRJCd_PJ9H8p7L8BD3CgPzDklXD2e0E5_Du9ZTp4mPPLXwuSj7HySpGfd4&usqp=CAU' width="70%"></center>

<!-- 
<center><img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FJyfbT%2FbtqEqtpxbch%2FflfwGbM7mgv1kP1kkn4nQK%2Fimg.png" width = "70%"></center> -->

SVM은 두 개의 다른 클래스를 분류할 수 있는 여러가지 결정 경계(Decision Boundary)중에 가장 잘 분류할 수 있는 결정 경계를 찾는 것입니다.

**잘 분류한다는 것**(결정 경계의 조건)은 Support Vector로부터 거리가 가장 멀어야 합니다.(Margin이 가장 큰 값일 때)

용어들을 순차적으로 정리해보겠습니다.

## 결정 경계(Decision Boundary)

- 2차원의 결정 경계는 선, 3차원은 평면, 그 이상은 **초평면(Hyperplane)**이라고 부릅니다.
- Support Vector는 결정 경계와 가장 가까이 있는 데이터 Vector들을 의미합니다.

## 마진(Margin)

- 결정 경계와 서포트 벡터 사이의 거리


## 커널(Kernel)

### 1. 다항식(Polynomial)

<center><img src="http://aidev.co.kr/files/attach/images/188/028/001/aba92769caba048452e9acea299ac655.PNG"></center>

### 2. 방사 기저 함수(RBF: Radial Bias Function)

- Parameter: gamma

### 이상치(Outlier)


### 정리


## REFERENCE
[https://hleecaster.com/ml-svm-concept/](https://hleecaster.com/ml-svm-concept/)
[https://techblog-history-younghunjo1.tistory.com/78](https://techblog-history-younghunjo1.tistory.com/78)