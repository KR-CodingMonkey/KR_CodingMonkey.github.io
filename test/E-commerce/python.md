# python 코드

6가지의 모듈로 나누어서 작업을 했음

```
import pymysql # 데이터 베이스 연동
from os import system # system('cls') or system('clear')
# from msvcrt import getch
from time import sleep # sleep()
from datetime import datetime # datetime.now()

class member:

def Init_Display():

def Main_page():

def Login_Page():

def Signup_Page():

def Admin_Mode():

def Member_Mode(id:str):

if __name__ == '__main__'
    global conn

    conn = pymysql.connect(
        host = '127.0.0.1', 
        user = 'root', 
        password='', 
        port = 13306, 
        db = 'e_commerce', 
        charset = 'utf8')

    # conn = pymysql.connect(
    #     host = '172.17.0.2', 
    #     user = 'root', 
    #     password='', 
    #     port = 3306, 
    #     db = 'e_commerce', 
    #     charset = 'utf8')

    Init_Display()
    Main_Page()

    conn.close()
```
---

### class member

class는 쓰지 않아도 됐지만 써봤음

```
class member:
    def __init__(self, id, email, pwd):
        self.id = id
        self.email = email
        self.pwd = pwd
        self.create_date = str(datetime.now())

    def __str__(self):
        return "\nID          = " + self.id + "\nEmail       = " + self.email + \
        "\nPassword    = " + self.pwd + "\nCreate Date = " + self.create_date + "\n"
```

회원가입 시 입력받은 아이디/이메일/비밀번호를 토대로 클래스를 생성 후 출력한다.

---

### Init_Display()

프로그램 실행시 초기화면으로 프로그램 이름/버전과 선택할수 있는 3가지의 기능이 보여진다.
```
mm = 0.5;
system('cls')

print("┌────────────────────────────┐")
print("└────────────────────────────┘")

sleep(mm);
system('cls')
print("┌────────────────────────────┐\n")
print("└────────────────────────────┘")
sleep(mm);

system('cls')
print("┌────────────────────────────┐")
print("        e-commerce v0.1")
print("└────────────────────────────┘")
sleep(mm);
```

`from time import sleep`<br/>
`from os import system`<br/>
sleep(n) n초의 시간을 대기한다.   system('cls') 콘솔화면의 내용을 지운다

---

### Main_Page()

```
mum = 0;

while(1):    
    system('cls')
    print("┌────────────────────────────┐")
    print("        e-commerce v0.1")
    print("└────────────────────────────┘")

    mum = mum % 3;
    if mum == 0: print("\t ▶ ", end = '')
    else: print("\t ▷ ", end = '')
    print("로그인")
    if mum == 1: print("\t ▶ ", end = '')
    else: print("\t ▷ ", end = '') 
    print("회원가입")
    if mum == 2: print("\t ▶ ", end = '')
    else: print("\t ▷ ", end = '')
    print("종료")

    key = ord(getch())    
    if key == 0: #Special keys (arrows, f keys, ins, del, etc.)
        key = ord(getch())
        if key == 80: #Down arrow
            mum += 1 
            if mum > 2: mum = 0;

        elif key == 72: #Up arrow
            mum -= 1 
            if mum < 0: mum = 2;

    elif key == 13:
        if mum == 0:
            # 로그인 메뉴 (1.관리자, 2.회원)
            Login_Page()
        elif mum == 1: 
            # 회원가입 메뉴
            Singup_Page()
        else:
            # 종료
            break
```


---