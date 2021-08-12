---
sort: 2 
---

# InitPage 

- 6가지의 모듈로 나누어서 작업을 했습니다.

```
import pymysql # 데이터 베이스 연동
from os import system
# from msvcrt import getch
from time import sleep
from datetime import datetime

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

포트번호와 아이피가 헷갈리수 있는데, DB컨테이너를 다음과 같이 구동해봤다고 합시다.<br/>
`docker run --name mysql -p 13306:3306 -d -e MYSQL_ALLOW_EMPTY_PASSWORD=true mysql:latest`

`-p Host:Container` 옵션은 포트포워딩을 위한 옵션입니다.

 13306은 외부에서 찾아올 때 번지수, 3306은 내부에서의 번지수라고 이해하시면 됩니다. `-p 13306:3306` 옵션을 주게 되면 컨테이너의 3306번지수를 밖에는 13306으로 써놓겠다. 13306으로 찾아온 신호들을 내부의 3306으로 연결해 주겠다라는 뜻입니다. 하지만 충돌이 일어나지 않는다는 가정하에 `-p 3306:3306`으로 써주면 편하겠죠?

`-p 13306:3306`으로 컨테이너 포트포워딩을 했다고 가정하겠습니다.

|DB\Python |Windows | Linux |
|----------|-------|
|Windows | h:<br/>p: 13306 |  |
|Linux | h:  127.0.0.1<br/>p: | h:<br/>p: 13306 |

Windows/Windows 와 Linux/Linux는 동일합니다. <br>
Docker에서 container를 생성하게 되면 컨테이너마다 아이피가 할당되는데 <br>
`172.17.0.x` 이렇게 컨테이너 생성 시기 순으로 순차적으로 할당이 됩니다. <br?>
`docker inspect <option> <ID or Image name>`을 사용하게 되면 해당 컨테이너의 IP 주소를 확인하고 맞추어 연결할 수 있습니다. 또한, 아이피를 고정으로 할당하는 방법도 있습니다.

Windows/Linux 포트번호는 조금은 복잡합니다.<br/>
```
Windows(host) -> Linux(guset)
                 Linux(host) -> DB server(guset)
```
이런식으로 포트포워딩을 해야합니다. 그렇다면
```
13306 : 3306
        3306 : 3306
```
이렇게 설정해주고 나서 연결을 해주면 됩니다.
```
conn = pymysql.connect(
    host = '127.0.0.1', 
    user = 'root', 
    password='', 
    port = 13306, 
    db = 'e_commerce', 
    charset = 'utf8')
```
<br/>
## class member
---

- 회원가입 시 입력받은 아이디/이메일/비밀번호를 토대로 클래스를 생성 후 출력한다.

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
<br/>
## Init_Display()
---

`from time import sleep`<br/>
`from os import system`<br/>
- 프로그램 실행시 초기화면으로 프로그램 이름/버전과 선택할수 있는 3가지의 기능이 보여진다.
- sleep(n) n초의 시간을 대기한다.<br/>
- system('cls') 콘솔화면의 내용을 지운다
- Linux의 경우 system('clear')

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
<br/>
## Main_Page()
---

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
    
    #Special keys (arrows, f keys, ins, del, etc.)
    if key == 0: 
        key = ord(getch())
        if key == 80: # Down arrow
            mum += 1 
            if mum > 2: mum = 0;

        elif key == 72: # Up arrow
            mum -= 1 
            if mum < 0: mum = 2;

    # Enter
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

<img src = "https://user-images.githubusercontent.com/76420201/104425234-c3fc2f00-55c3-11eb-8f90-7ee102b3742a.GIF" width="50%">

getch()라는 함수로 사용자의 키보드 입력(↑, ↓, Enter)을 받는데 Unix기반 OS와 windows 함수를 다르게 정의 해줘야 한다.

```
class _Getch:
    """Gets a single character from standard input.  Does not echo to the
    screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()

# os -> unix
class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

# os -> windows
class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

# 함수 재정의
getch = _Getch()

```

`getch = _Getch()` 객체를 생성하게 되면 실행환경 OS에 따라서 적용이 됩니다.

그리고!! 윈도우에서의 방향키값과 리눅스에서의 방향키값이 다르더군요.(Enter는 동일합니다)   

| |↑|↓|
|--|--|--|
|Windows|0 72| 0 80|
|Linux|27 91 65| 27 91 66|
|Enter| 13 |

<!-- 
- Windows<br/>
위 : 0 72<br/>
아래 : 0 80 <br/>

- Linux<br/>
위 : 27 91 65<br/>
아래 : 27 91 66<br/> -->

리눅스에서 사용할때는 이렇게 입력받아야 합니다.
```
key = ord(getch())
if key == 27:
    key = ord(getch())
    if key == 91: #Down arrow
        key = ord(getch())
        if key == 66:
            mum += 1
            if mum > 2: mum = 0       

        elif key == 65: #Up arrow
            mum -= 1
            if mum < 0: mum = 2
```
<br/>
## Login_Page()
---

- 사용자로부터 ID/PW 입력받고 DB member에서 회원 조회`SELECT`
- 회원일 경우 회원모드로 전환
- admin/admin1234 일 경우 관리자모드로 전환

```
system('clear')
print("Login page\n")

id = input("      ID: ")
pw = input("Password: ")

cursor = conn.cursor()

## DB member 조회
sql_select = """select pw from member where id = '{}'""".format(id)

cursor.execute(sql_select)
result = cursor.fetchone()

# admin 계정일경우
if id == 'admin' and pw == 'admin1234':
    cursor.close()
    Admin_Mode()

# result값이 존재하고 회원일 경우
elif result and result[0] == pw:
    cursor.close()
    Member_Mode(id)

# 테이블에 존재하지 않을때
else:
    print("아이디와 비밀번호가 일치하지 않습니다.")
    sleep(3)

    cursor.close()
    return 0
```
<br/>
## Singup_page()
---

- 사용자로부터 아이디/이메일/비밀번호를 입력받아서 회원가입`INSERT`
- DB member에 이미 존재하는`SELECT` 아이디일 경우 실패

```
def Singup_Page():

    while(1):
        system('cls')
        print("-Sign up-\n")
        sleep(0.5)

        new_id = input("아이디: ")
        new_email = input("이메일: ")
        new_pwd = input("비밀번호: ")
        confirm_pwd = input("비밀번호 확인: ")

        if new_pwd == confirm_pwd: 

            cursor = conn.cursor()

            # 중복된 아이디가 존재한다면 다시
            sql_search = '''SELECT * FROM member where id = '{}';'''.format(new_id)  
            result = cursor.execute(sql_search)

            if result:
                print("이미 존재하는 아이디 입니다.")
                sleep(3)
                continue

            else:
                new_member = member(new_id, new_email, new_pwd)
                
                # DB member 테이블에 INSERT
                sql_insert = '''
                INSERT INTO member (id, email, pw, c_date)
                values(%s, %s, %s, %s)
                '''

                values = (new_member.id, new_member.email, new_member.pwd, new_member.create_date)
                cursor.execute(sql_insert, values)
                conn.commit()
                cursor.close()

                print("회원가입이 되었습니다.")
                print(new_member)
                sleep(5)
                break

        else:
            print("\n비밀번호를 확인해주세요!!\n")
            sleep(3)
            system('cls')
            break
```

<img src= "https://user-images.githubusercontent.com/76420201/104859877-8b65a800-596b-11eb-8a2d-4713fda5b230.GIF" width = "50%">