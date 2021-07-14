# Pymysql

```python
# 1.Mysql에서 member 테이블에 아래 작업 실행
# 사용자 추가
# 사용자 수정/삭제
# 사용자 검색
```


```python
import pymysql

conn = pymysql.connect(
    host = '127.0.0.1', 
    user = 'root', 
    password='', 
    port = 13306, 
    db = 'mydb', 
    charset = 'utf8')

cursor = conn.cursor()

sql = '''
CREATE TABLE member2(
num INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(20) NOT NULL,
email VARCHAR(20) NOT NULL,
c_date DATETIME
);
'''
```


```python
tables = cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)
```


```python
cursor.execute(sql)
```


```python
conn.commit()
cursor.execute("SHOW TABLES")

cursor.close()
conn.close()
```

## DB INSERT


```python
# DB insert

import pymysql

conn = pymysql.connect(
    host = '127.0.0.1', 
    user = 'root', password='', 
    port = 13306, 
    db = 'mydb', 
    charset = 'utf8')

cursor = conn.cursor()
```


```python
sql_insert = '''INSERT INTO member2 (num, name, email, c_date)\
values(null, "Administrator", "admin@test.com", NOW())'''

cursor.execute(sql_insert)
```




    1




```python
conn.commit()

cursor.close()
conn.close()
```

## DB SELECT


```python
# DB select

import pymysql

conn = pymysql.connect(
    host = '127.0.0.1', 
    user = 'root', 
    password='', 
    port = 13306, 
    db = 'mydb', 
    charset = 'utf8')

cursor = conn.cursor()
```


```python
sql = "SELECT * FROM member2"
cursor.execute(sql)
```




    1




```python
result = cursor.fetchall()
for row_data in result:
    print(row_data)
```

    (3, 'Administrator', 'user1@test.com', datetime.datetime(2021, 1, 8, 0, 0))
    


```python
cursor.close()
conn.close()
```

## DB UPDATE


```python
# DB select

import pymysql

conn = pymysql.connect(
    host = '127.0.0.1', 
    user = 'root', 
    password='', 
    port = 13306, 
    db = 'mydb', 
    charset = 'utf8')

cursor = conn.cursor()
```


```python
sql_update = "UPDATE member2 SET email = 'user1@test.com' WHERE num = 3"
cursor.execute(sql_update)
```




    1




```python
conn.commit()
cursor.close()
conn.close()
```

## DB DELETE


```python
# DB Delete

import pymysql

conn = pymysql.connect(
    host = '127.0.0.1', 
    user = 'root', 
    password='', 
    port = 13306, 
    db = 'mydb', 
    charset = 'utf8')

cursor = conn.cursor()
```


```python
sql_delete = "DELETE FROM member2 WHERE num = 4"
cursor.execute(sql_delete)
```




    1




```python
conn.commit()

cursor.close()
conn.close()
```


```python

```
