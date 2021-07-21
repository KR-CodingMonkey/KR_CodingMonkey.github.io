
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

- 우선 순위가 다른 연산자를 사용하는 경우 우선 순위가 가장 낮은 연산자 주위에 공백을 추가

```python
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
```
### Comments

- 코드와 모순되는 주석은 주석이 없는 것보다 나쁨.<br/> 코드가 변경될 때 항상 주석을 최신 상태로 유지하는 데 우선 순위를 두어야함

- 불필요한 주석은 달지 않는다

### Naming Convention

- 변수명에서 _(밑줄)은 위치에 따라 다음과 같은 의미가 있습니다.
    - _single_leading_underscore: 내부적으로 사용되는 변수를 일컫습니다.
    - single_trailing_underscore_: 파이썬 기본 키워드와 충돌을 피하려고 사용합니다.
    - __double_leading_underscore: 클래스 속성으로 사용되면 그 이름을 변경합니다. </br>
    (ex. FooBar에 정의된 __boo는 _FooBar__boo로 바뀝니다.)

    - __double_leading_and_trailing_underscore__: 마술(magic)을 부리는 용도로 사용되거나 사용자가 조정할 수 있는 네임스페이스 안의 속성을 뜻합니다. 이런 이름을 새로 만들지 마시고 오직 문서대로만 사용하세요.

- 소문자 L, 대문자 O, 대문자 I는 변수명으로 사용하지 마세요. 어떤 폰트에서는 가독성이 굉장히 안 좋습니다.
- 모듈(Module) 명은 짧은 소문자로 구성되며 필요하다면 밑줄로 나눕니다.
    - 모듈은 파이썬 파일(.py)에 대응하기 때문에 파일 시스템의 영향을 받으니 주의하세요.
    - C/C++ 확장 모듈은 밑줄로 시작합니다.
- 클래스 명은 카멜케이스(CamelCase)로 작성합니다.
    - 내부적으로 쓰이면 밑줄을 앞에 붙입니다.
    - 예외(Exception)는 실제로 에러인 경우엔 “Error”를 뒤에 붙입니다.
- 함수명은 소문자로 구성하되 필요하면 밑줄로 나눕니다.
    - 대소문자 혼용은 이미 흔하게 사용되는 부분에 대해서만 하위호환을 위해 허용합니다.
- 인스턴스 메소드의 첫 번째 인자는 언제나 self입니다.
- 클래스 메소드의 첫 번째 인자는 언제나 cls입니다.
- 메소드명은 함수명과 같으나 비공개(non-public) 메소드, 혹은 변수면 밑줄을 앞에 붙입니다.
- 서브 클래스(sub-class)의 이름충돌을 막기 위해서는 밑줄 2개를 앞에 붙입니다.
- 상수(Constant)는 모듈 단위에서만 정의하며 모두 대문자에 필요하다면 밑줄로 나눕니다.

### Programming Recommendations
