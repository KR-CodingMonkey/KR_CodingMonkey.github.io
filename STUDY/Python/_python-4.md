# python csv parsing

```
import csv

# csv파일 읽기
file = open('C:\\test\\covid19.csv', 'r')
read_file = csv.reader(file)

max, min = 0, 999999
max_city, min_city = '', ''

strFormat = '%s\t%s\t%s\t%s\t%s\n' # 형식 정하기
strOut = strFormat % ('시도', "계", ' 10월', ' 11월', ' 12월')
isbool = True

for line in read_file:

    # 첫째줄 pass
    if isbool:
        isbool = False
    
    else:
        num = [0] * 3
        for i in range(3):

            # ex) (str)12,345 -> (int)12345
            if ',' in line[i+2]:
                a, b = map(int, line[i + 2].strip().split(','))
                num[i] = a * 1000 + b 

            # ex) '-' -> 0
            elif '-' in line[i+2]:
                line[i+2] = ' 0'
                num[i] = 0
            
            else:
                num[i] = int(line[i+2].strip())

        # 합계
        total = num[0] + num[1] + num[2]
        strOut += strFormat % (line[1], total, line[2], line[3], line[4])

        if max < total:
            max = total
            max_city = line[1]

        elif min > total:
            min = total
            min_city = line[1]
            
print(strOut)
print('''{0}에서 {1}명으로 확진자가 가장 많이 발생하였으며,\n{2}에서 {3}명으로 확진자가 가장 적게 발생하였습니다.
'''.format(max_city, max, min_city, min))

file.close()
```

<img src="https://user-images.githubusercontent.com/76420201/104859674-4d1bb900-596a-11eb-8bab-f2f255db6dbd.GIF" width = "70%" >


---
