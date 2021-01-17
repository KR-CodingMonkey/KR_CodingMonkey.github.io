# re 모듈 사용법

## 정규 표현식

```python
import re

re.search(r'abc', '123abcABC')
```
```
<re.Match object; span=(3, 6), match='abc'>
```

- Meta Characters

1. [] 문자들의 범위를 나타내기 위해 사용

| | |
|-|-|
|[abck] | a or b or c or k |
|[abc.^] | a or b or c or . or ^ |
|[a-d] | -와 함께 사용되면 해당 문자 사이의 범위에 속하는 문자 중 하나 |
|[0-9] | 모든 숫자 |
|[a-z] | 모든 소문자 |
|[A-Z] | 모든 대문자 |
|[a-zA-Z0-9] | 모든 알파벳 문자 및 숫자 |
|[^0-9] | ^가 맨 앞에 사용 되는 경우 해당 문자 패턴이 아닌 것과 매칭 (유사 Not)|





2. (마침표) . 모든 문자를 의미

3. \

| | |
|-|-|
|\d | 숫자를 [0-9]와 동일 |
|\D | 숫자가 아닌 문자 [^0-9]와 동일 |
|\s | 공백 문자(띄어쓰기, 탭, 엔터 등) |
|\S | 공백이 아닌 문자 |
|\w | 알파벳대소문자, 숫자 [0-9a-zA-Z]와 동일 |
|\W | non alpha-numeric 문자 [^0-9a-zA-Z]와 동일 |
|\t, \n, \r | tab, newline, return |

## 단어 개수 세기

[어린왕자](https://github.com/KR-CodingMonkey/KR-CodingMonkey.github.io/blob/develop/assets/the_little_prince.txt)의 모든 단어의 갯수 카운트하기

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
