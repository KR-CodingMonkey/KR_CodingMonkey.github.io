{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1.Mysql에서 member 테이블에 아래 작업 실행\n",
    "# 사용자 추가\n",
    "# 사용자 수정/삭제\n",
    "# 사용자 검색"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pymysql\n",
    "\n",
    "conn = pymysql.connect(\n",
    "    host = '127.0.0.1', \n",
    "    user = 'root', \n",
    "    password='', \n",
    "    port = 13306, \n",
    "    db = 'mydb', \n",
    "    charset = 'utf8')\n",
    "\n",
    "cursor = conn.cursor()\n",
    "\n",
    "sql = '''\n",
    "CREATE TABLE member2(\n",
    "num INT PRIMARY KEY AUTO_INCREMENT,\n",
    "name VARCHAR(20) NOT NULL,\n",
    "email VARCHAR(20) NOT NULL,\n",
    "c_date DATETIME\n",
    ");\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "tables = cursor.execute(\"SHOW TABLES\")\n",
    "\n",
    "for table in cursor:\n",
    "    print(table)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "cursor.execute(sql)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [],
   "source": [
    "conn.commit()\n",
    "cursor.execute(\"SHOW TABLES\")\n",
    "\n",
    "cursor.close()\n",
    "conn.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## DB INSERT"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "metadata": {},
   "outputs": [],
   "source": [
    "# DB insert\n",
    "\n",
    "import pymysql\n",
    "\n",
    "conn = pymysql.connect(\n",
    "    host = '127.0.0.1', \n",
    "    user = 'root', password='', \n",
    "    port = 13306, \n",
    "    db = 'mydb', \n",
    "    charset = 'utf8')\n",
    "\n",
    "cursor = conn.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 133,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sql_insert = '''INSERT INTO member2 (num, name, email, c_date)\\\n",
    "values(null, \"Administrator\", \"admin@test.com\", \"2021-01-08\")'''\n",
    "\n",
    "cursor.execute(sql_insert)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {},
   "outputs": [],
   "source": [
    "conn.commit()\n",
    "\n",
    "cursor.close()\n",
    "conn.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## DB SELECT"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 170,
   "metadata": {},
   "outputs": [],
   "source": [
    "# DB select\n",
    "\n",
    "import pymysql\n",
    "\n",
    "conn = pymysql.connect(\n",
    "    host = '127.0.0.1', \n",
    "    user = 'root', \n",
    "    password='', \n",
    "    port = 13306, \n",
    "    db = 'mydb', \n",
    "    charset = 'utf8')\n",
    "\n",
    "cursor = conn.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 171,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 171,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sql = \"SELECT * FROM member2\"\n",
    "cursor.execute(sql)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 172,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(3, 'Administrator', 'user1@test.com', datetime.datetime(2021, 1, 8, 0, 0))\n"
     ]
    }
   ],
   "source": [
    "result = cursor.fetchall()\n",
    "for row_data in result:\n",
    "    print(row_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 173,
   "metadata": {},
   "outputs": [],
   "source": [
    "cursor.close()\n",
    "conn.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## DB UPDATE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "metadata": {},
   "outputs": [],
   "source": [
    "# DB select\n",
    "\n",
    "import pymysql\n",
    "\n",
    "conn = pymysql.connect(\n",
    "    host = '127.0.0.1', \n",
    "    user = 'root', \n",
    "    password='', \n",
    "    port = 13306, \n",
    "    db = 'mydb', \n",
    "    charset = 'utf8')\n",
    "\n",
    "cursor = conn.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 154,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 154,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sql_update = \"UPDATE member2 SET email = 'user1@test.com' WHERE num = 3\"\n",
    "cursor.execute(sql_update)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "metadata": {},
   "outputs": [],
   "source": [
    "conn.commit()\n",
    "cursor.close()\n",
    "conn.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## DB DELETE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "metadata": {},
   "outputs": [],
   "source": [
    "# DB Delete\n",
    "\n",
    "import pymysql\n",
    "\n",
    "conn = pymysql.connect(\n",
    "    host = '127.0.0.1', \n",
    "    user = 'root', \n",
    "    password='', \n",
    "    port = 13306, \n",
    "    db = 'mydb', \n",
    "    charset = 'utf8')\n",
    "\n",
    "cursor = conn.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 168,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 168,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sql_delete = \"DELETE FROM member2 WHERE num = 4\"\n",
    "cursor.execute(sql_delete)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "metadata": {},
   "outputs": [],
   "source": [
    "conn.commit()\n",
    "\n",
    "cursor.close()\n",
    "conn.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
