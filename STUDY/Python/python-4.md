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


```
import csv

total = dict()
loc_max = None
loc_min = None

def check_num(value:str) -> int:
    if value == '-':
        return 0
    else:
        try:
            return int(value)
        except:
            return 0

def f1(x):
    return total[x]

def main():
    with open('covid19.csv', 'r', encoding='utf-8') as covid19:
        csv_reader = csv.reader(covid19)
        next(csv_reader)
        
        print("%s %9s %9s %9s %9s" % ('시도', '계', '10월', '11월', '12월'))
        for row in csv_reader:
            oct = check_num(row[2])
            nov = check_num(row[3])
            dec = check_num(row[4])
            sum = oct + nov + dec

            total[row[1]] = sum
            print("%s %10s %10s %10s %10s" % (row[1], format(sum, ','), format(oct, ','), format(nov, ','), format(dec, ',')))

    loc_max = max(total.keys(), key=f1)
    loc_min = min(total.keys(), key=(lambda k: total[k]))

    print("{0}에서 {1}명으로 확진자가 가장 많이 발생했으며,".format(loc_max, format(total[loc_max], ',')))
    print("{0}에서 {1}명으로 확진자가 가장 적게 발생했습니다.".format(loc_min, format(total[loc_min], ',')))

main()
```