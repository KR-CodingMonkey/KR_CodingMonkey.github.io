# python 코드

6가지의 모듈로 나누어서 작업을 했음

```
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

회원가입시 입력받은 아이디/이메일/비밀번호를 토대로 클래스를 생성후 출력한다.

---

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