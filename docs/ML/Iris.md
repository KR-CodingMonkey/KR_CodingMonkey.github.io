---
title: Iris Classification
tags: 
 - Machine Learning
 - Iris
 - Supervised Learning
 - 인공지능(AI)
description: Iris Classification
permalink: Iris
---

# Iris Classification

## 개요 

- 간단한 예제이므로, 전체적인 프로세스를 익히는 데 도움이 된다.
- 붓꽃의 sepal(꽃받침)과 petal(꽃잎)의 길이를 학습하고 setosa, versicolor, virginica 이 3가지 종류로 분류

![iris](https://user-images.githubusercontent.com/76420201/130013225-badbc9a4-6217-484f-80ac-fd1ec9cb92b0.jpg)


## 지도 학습(Supervised Learning)

- 정답을 알려주며 학습
- 분류 결정값이 사전에 정의 되어야 함

## Code

### 데이터셋 불러오기

```python
import sklearn
from sklearn.datasets import load_iris

print(sklearn.__version__)
# 0.24.2

# 데이터셋은 딕셔너리와 유사한 Bunch 클래스의 객체. Key:Value 형태를 지니고 있다.
# data.key 또는 data['key']
iris_dataset = load_iris()

print(iris_dataset.keys())
# dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename'])
```
- 데이터셋의 각 키값을 확인 

```python 
iris_label = iris_dataset.target
print(iris_label[[0, 50, 100]])
# array([0, 1, 2])

print(iris_dataset['target_names'])
# array(['setosa', 'versicolor', 'virginica'], dtype='<U10')

iris_data = iris_dataset.data
print(iris_data.shape)
# (150, 4)
```

### 데이터 전처리

데이터를 탐색하면서 이상치나 결측치를 발견할 수 있다. 예를 들어 값의 단위가 다르다거나 데이터와 연관이
없는 이상한 값들이 들어있을 수 있다.

**산점도 그래프**라는 시각화 방법을 통해서 종별로 그룹화하여 데이터를 조사합니다. **산점도**는 직교 좌표계를 이용해 좌표상의 점들을 표시함으로써 두 개 변수 간의 관계를 나타내는 그래프 방법입니다.

```python
sns_data = iris_df.copy()

replace_label = {0: 'setosa', 1:'versicolor', 2:'virginica'}
sns_data.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "label"] 

sns_data['label'] = sns_data['label'].map(replace_label)
print(sns_data.head(5))
```

```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.pairplot(sns_data, hue='label', height=2, palette='colorblind')

plt.show()
```

![sns](https://user-images.githubusercontent.com/76420201/130068456-5c67609b-c139-414e-8219-1a9010f8104f.GIF)

- 꽃잎과 꽃받침의 길이에 따라 종이 잘 구분되는 것을 볼 수 있다


### 데이터셋 분리

```python
from sklearn.model_selection import train_test_split

# train_test_split(독립변수, 종속변수, 데이터 비율, 난수생성기)
X_train, X_test, y_train, y_test = train_test_split(iris_data, iris_label, random_state=1)

print(X_train.shape) # (112, 4)
print(X_test.shape) # (38, 4)
```

### 모델 학습하기

- 아이리스 학습데이터를 이용해 모델을 학습

```python
from sklearn.tree import DecisionTreeClassifier

# 객체 생성 random_state : 난수 생성기
model = DecisionTreeClassifier(random_state=20)

# 학습
model.fit(X_train, y_train)
```

# 모델 평가하기
- sklearn의 tree 모듈을 활용해 결정트리모델의 트리구조를 확인할 수 있다

```python
from sklearn import tree

plt.figure(figsize=(20,15))
tree.plot_tree(model,
               class_names=iris_dataset.target_names,
              feature_names=iris_dataset.feature_names,
              impurity=True,
              filled=True,
              rounded=True)

plt.show()
```

![tree1](https://user-images.githubusercontent.com/76420201/130347653-420f304e-a66f-44f6-9ad8-f1d74ee97709.GIF)


```python
# 모델 평가하기
print(model.score(X_train, y_train))
print(model.score(X_test, y_test))

# 1.0
# 0.9736842105263158
```

- 위에 결정트리는 학습데이터에 과적합(over-fitting)이 되어 있기 때문에 모델 성능에 영향을 줄 수 있다.
- 과적합 문제를 해결하기 위해 하이퍼파라미터 값을 조절함으로써 모델을 개선
- 현재 모델 일반화 성능에 변화는 없지만 중요!

```python
# 객체 생성 max_depth: 트리의 최대 깊이 (값이 클수록 모델의 복잡도가 올라간다)
model = DecisionTreeClassifier(max_depth=3, random_state=20)

# 학습
model.fit(X_train, y_train)

plt.figure(figsize=(20,15))
tree.plot_tree(model,
               class_names=iris_dataset.target_names,
              feature_names=iris_dataset.feature_names,
              impurity=True,
              filled=True,
              rounded=True)

plt.show()
```
![tree2](https://user-images.githubusercontent.com/76420201/130347664-c9f3f27b-bc80-4e44-a4ac-76a5168000e9.GIF)

```python
print(model.score(X_train, y_train))
print(model.score(X_test, y_test))

# 0.9821428571428571
# 0.9736842105263158
```

### 특성 중요도

- 결정트리 모델에 각 특성의 중요도를 평가
- 특성 중요도 전체의 합은 1

```python
for name, value in zip(iris_dataset.feature_names , model.feature_importances_):
    print('{} : {:.3f}'.format(name, value))

'''
sepal length (cm) : 0.000
sepal width (cm) : 0.000
petal length (cm) : 0.606
petal width (cm) : 0.394
'''
```

```python
# 특성 중요도 시각화
sns.barplot(x=model.feature_importances_, y=iris_dataset.feature_names)

plt.show()
```

![importance](https://user-images.githubusercontent.com/76420201/130403451-05504026-17ca-4a65-952c-ae37eb8e2cf2.GIF)
