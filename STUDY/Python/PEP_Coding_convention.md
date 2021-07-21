
# PEP Coding Convention

## PEP(Python Enhance Proposal)
- 파이썬을 개선하기 위한 개선 제안서를 뜻함

## Coding Convention
- 프로그램 코드를 작성할 때 사용되는 일종의 기준
- [PEP8](https://www.python.org/dev/peps/pep-0008/)

### Code Lay-out

- 들여쓰기는 4개의 공백을 사용
- 연속 라인은 요소를 수직적으로 정렬

```python
# 여는 구분 기호에 맞춰 정렬됩니다. 
foo = long_function_name(var_one, var_two, 
                        var_three, var_four) 

# 나머지와 인수를 구별하기 위해 4개의 공백(추가 수준의 들여쓰기)을 추가합니다. 
def long_function_name( 
    var_one, var_two, var_three, 
    var_four): 
print(var_one) 
```

- Python 표준 라이브러리는 보수적이며 줄을 79자로 제한(주석은 72자)

```python
# easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

- 최상위(top-level) 함수와 클래스 정의는 2줄씩 띄움
- 클래스 내의 메소드 정의는 1줄씩 띄움

### Whitespace in Expressions and Statements
- 불필요한 공백은 지움
```python
# 괄호, 대괄호 또는 중괄호 바로 안에
spam(ham[1], {eggs: 2})

# 쉼표와 다음 닫는 괄호 사이
foo = (0,)

# 쉼표, 세미콜론 또는 콜론 바로 앞
if x == 4: print x, y; x, y = y, x
```

### Comments

### Naming Convention

### Programming Recommendations
