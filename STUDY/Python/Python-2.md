# re 모듈 사용법

## 정규 표현식
Meta Characters

| | |
|-|-|
|a-zA-Z] | 알파벳 모두 |
|[0-9] | 숫자 |
|\d | 숫자와 매치, [0-9]와 동일한 표현식이다. |
|\D | 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다. |
|\s | whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다. |
|\S | whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다. |
|\w | 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식이다. |
|\W | 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식이다. |

## 단어 개수 세기

모든 단어의 갯수 카운트하기

```note
대소문자 주의

  ex) You you, The the

```

```python
import re # To use refindall func

# file = open('the_little_prince_test.txt', 'r')
file = open('the_little_prince.txt', 'r')

new_line = file.read().strip().lower() # 소문자로 변환
words = re.findall(r"[\w']+", new_line) # 단어로 나누기 -> list

file.close() # 파일 종료

count_words = dict() # {word : count}
words.sort() # 정렬

# 딕셔너리에 저장
for word in words:
    count_words[word] = count_words.get(word, 0) + 1

# print(count_words)
for word, count in count_words.items():
    print("{0} : {1}".format(word, count))
```


<img src="https://user-images.githubusercontent.com/76420201/104839352-c8964f80-5903-11eb-98c8-15b1406011f0.GIF" width = "60%">
