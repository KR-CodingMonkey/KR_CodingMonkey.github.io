
# 숫자야구

```python
import random

my_num = 0
count = 0
random_num = random.randint(1, 100)
#print(random_num)

while(my_num != random_num):
    my_num = int(input())
    #print(my_num)
    count += 1

    if my_num > random_num:
        print("보다 작은 수를 입력")
    else:
        print("보다 큰 수를 입력")
    # print((lambda x : "High" if x > random_num else "Low")(my_num))

print("count = {}".format(count))

if count <= 5:
    print("천재")
elif count <= 10:
    print("보통")
else:
    print("바보")

```