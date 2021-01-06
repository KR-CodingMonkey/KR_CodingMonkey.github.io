# 단어 개수 세기

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