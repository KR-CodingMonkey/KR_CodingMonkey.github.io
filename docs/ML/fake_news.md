---
title: Fake News Detection
tags: 
 - Machine Learning
 - github
 - fake news
 - big data
 - 인공지능(AI)
description: Fake News Detection
permalink: Fake_news
---

# Fake News Detection
**데이터 셋** : [FAKE NEWS DATASET](https://www.kaggle.com/c/fake-news/data)

`Data Description`

- train.csv: A full training dataset with the following attributes:
    - id: unique id for a news article
    - title: the title of a news article
    - author: author of the news article
    - text: the text of the article; could be incomplete
    - label: a label that marks the article as potentially unreliable
        - 1: unreliable
        - 0: reliable

- test.csv: A testing training dataset with all the same attributes at train.csv without the label.
- submit.csv: A sample submission that you can

## Introduction

'가짜 뉴스' : 신뢰할 수 없는 출처에서 나오는 잘못된 뉴스

무분별한 가짜 뉴스들이 생산되는 가운데 이를 판별하기 위한 많은 기술들이 연구되어 있다.
가짜뉴스의 표현은 표준 뉴스와 구별되며, 기계학습은 이런 차이를 감지할 수 있다는 생각에서 출발한다. 

- 가짜 뉴스 판별 기술

|기술|장점|단점|
|:------------------------:|:----:|:----:|
|언어적 특징 기반 접근법|언어에는 다양한 형태들과 기법들이 있으며, 대표적으로 구두점, 심리 언어적 특징, 가독성, 구문 등을 활용|어휘를 생성한 규칙에 과도하게 의존|
|문서 형태 분석 기법|정확하게 문서형태를 가지고 있으며, 명확성이 떨어질수록 분류하기 쉽다.|자유 형태를 가지고 쓰인 뉴스는 분류하기 힘들다.|
|출처 신뢰도 검증 기술|잘 알려져 있거나 믿을 수 있는 언론사와 옐로저널리즘의 요약본들을 구분하여 출처 신뢰도를 판단|특정 사이트나 사람을 일반화하는것이기에 확실한 검정이없다면 뉴스를 분류하기에는 적합하지 않다.|
|콘텐츠 교차 검증|유사성 비교외에도 최소 두 가지 판단 방법으로 가짜뉴스여부를 판별|다른 방법보다 검정 방법을 더 섞기때문에 시간이 오래 걸림|
|딥러닝 기술|가짜뉴스에 대한정보가 많으면 많을수록 실시간 성능 개선이 가능하다.|성과가 통계적 의미로 검증이 확실한지는 아직 미지수|


<!-- 출처신뢰도검증 기술은 뉴스기사가 게시된 웹사이트나 출처라고 정의할 수 있는 웹사이트에 관한 데이터베이스 바탕으로 별도로 신뢰성을 확인하여 가짜뉴스를 판별하는 방식이다. 이 방식은 가짜뉴스를 생성하는 곳은 지속적으로 가짜뉴스를 생성하는 습성이 있으며, 진짜뉴스를 생성하는 곳은 지속적으로 진짜뉴스를 게시하는 습성이
있다는 관찰결과를 바탕으로 작동한다. 따라서 잘 알려져 있거나 믿을 수 있는 언론사와 옐로저널리즘의 요약본들을 구분하여 출처 신뢰도를 판단한다고도 볼 수 있다. 내용 안에 포함되어 있는 사진 및 문서, 상기되어 있는 출처에 대한 데이터베이스 기반 신뢰성 검증을 실행하는 경우도 포함 될 수 있다. -->

## Code

```python
import pandas as pd
import numpy as np
import nltk
import re

from tensorflow.keras.layers import Embedding,LSTM,Dense,Dropout
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.text import one_hot

# data load
df = pd.read_csv('./train.csv')
test = pd.read_csv('./test.csv')

# filling NULL values with '' string
df = df.fillna('')
test = test.fillna('')

df['total'] = df['title'] + df['author']
test['total'] = test['title'] + test['author']

X = df.drop('label', axis=1)
y = df['label']

#Choosing vocabulary size to be 5000 and copying data to msg for further cleaning
voc_size = 5000
msg = X.copy()
msg_test = test.copy()

from nltk.corpus import stopwords
nltk.download('stopwords')

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
corpus = []

#Applying stemming and some preprocessing
for i in range(len(msg)):
    review = re.sub('[^a-zA-Z]', ' ', msg['total'][i])
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    corpus.append(review)

corpus_test = []
for i in range(len(msg_test)):
    review = re.sub('[^a-zA-Z]', ' ', msg_test['total'][i])
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    corpus_test.append(review)

# Converting to one hot representation
onehot_rep = [one_hot(words, voc_size) for words in corpus]
onehot_rep_test = [one_hot(words, voc_size) for words in corpus_test]

#Padding Sentences to make them of same size
embedded_docs = pad_sequences(onehot_rep, padding='pre', maxlen=25)
embedded_docs_test = pad_sequences(onehot_rep_test, padding='pre', maxlen=25)

#We have used embedding layers with LSTM
model = Sequential()
model.add(Embedding(voc_size, 40, input_length=25))
model.add(Dropout(0.3))
model.add(LSTM(100))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())
'''
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
embedding (Embedding)        (None, 25, 40)            200000    
_________________________________________________________________
dropout (Dropout)            (None, 25, 40)            0
_________________________________________________________________
lstm (LSTM)                  (None, 100)               56400
_________________________________________________________________
dense (Dense)                (None, 64)                6464
_________________________________________________________________
dropout_1 (Dropout)          (None, 64)                0
_________________________________________________________________
dense_1 (Dense)              (None, 1)                 65
=================================================================
Total params: 262,929
Trainable params: 262,929
Non-trainable params: 0
_________________________________________________________________
'''

X_final = np.array(embedded_docs)
y_final = np.array(y)
test_final = np.array(embedded_docs_test)

model.fit(X_final, y_final, epochs=20, batch_size=64)

# y_pred = model.predict_classes(test_final)
y_pred = model.predict(test_final)
print(y_pred)
y_pred = (y_pred > 0.5).astype('int32')

final_sub = pd.DataFrame()
final_sub['id'] = test['id']
final_sub['label'] = y_pred
# final_sub.to_csv('final_sub.csv', index=False)
print(final_sub.head())
```

<!-- 데이터 전처리에서 다음 단계를 따릅니다. 
1. 먼저 영어 문자를 제외한 모든 시퀀스가 ​​문자열에서 제거됩니다. 
2. 다음으로, 대문자와 소문자에 대한 잘못된 예측이나 모호성을 피하기 위해 문자열의 모든 문자를 소문자로 변환합니다. 
3. 다음으로 모든 문장을 단어로 토큰화합니다. 
4. 빠른 처리를 위해 토큰화된 단어에 형태소 분석을 적용합니다. 
5. 다음으로 단어를 결합하여 말뭉치에 저장합니다. -->

## References

1. Yoonjin Hyun, “Text Analytics-based Fake News Detection Methodology Using News and Social Data”, Ph.D Thesis, Graduate School of Buisness IT, Kookmin University, Feb. 2019

2. 이혜진(HyeJin Lee),김진영(Jinyoung Kim),and 백주련(Juryon Paik). "가짜뉴스 판별 기법 및 해결책 고찰." 한국컴퓨터정보학회 학술발표논문집 28.1 (2020): 37-39.