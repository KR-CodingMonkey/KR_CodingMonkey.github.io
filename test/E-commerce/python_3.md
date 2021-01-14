# python_3

1. 전체 회원 목록 조회
2. 전체 주문 목록과 회원별 주문 목록을 조회할 수 있다
3. 상품목록에 상품을 추가할 수 있다.
4. 가장 많은 금액을 주문한 사용자 목록을 확인할 수 있다.
5. 가장 많이 주문된 상품 목록을 확인할 수 있다.

---

## def Admin_Mode()

초기화면 생성
```
def Admin_Mode():

    mum = 0;

    while(1):

            
        system('cls')
        print("┌────────────────────────────┐")
        print("    Administrator Mode v0.1")
        print("└────────────────────────────┘")

        mum = mum % 6;
        if mum == 0: print("\t▶ ", end = '')
        else: print("\t▷ ", end = '')
        print("전체회원 목록")
        if mum == 1: print("\t▶ ", end = '')
        else: print("\t▷ ", end = '') 
        print("주문 목록")
        if mum == 2: print("\t▶ ", end = '')
        else: print("\t▷ ", end = '')
        print("상품 추가")
        if mum == 3: print("\t▶ ", end = '')
        else: print("\t▷ ", end = '')
        print("VIP고객 리스트")
        if mum == 4: print("\t▶ ", end = '')
        else: print("\t▷ ", end = '')
        print("인기 상품 리스트")
        if mum == 5: print("\t▶ ", end = '')
        else: print("\t▷ ", end = '')
        print("로그아웃\n")

        key = ord(getch())    
        if key == 0: 
            key = ord(getch())
            if key == 80: #Down arrow
                mum += 1 
                if mum > 5: mum = 0;

            elif key == 72: #Up arrow
                mum -= 1 
                if mum < 0: mum = 5;
```
---

### 전체 회원 목록 조회

```
        elif key == 13:
            # 전체 회원 목록
            if mum == 0:
                system("cls")
                print("-회원 목록 조회-")
                cursor = conn.cursor()
                
                # 전체 회원 조회하기
                sql_select = "SELECT * FROM member"
                cursor.execute(sql_select)
                result = cursor.fetchall()
            
                strFormat = '%-20s%-20s%-20s%-20s\n'
                strOut = strFormat % ('ID', "email", 'password', 'create_date')

                for row_data in result:
                    strOut += strFormat % (row_data[0], row_data[1], row_data[2], row_data[3])
                
                print(strOut)
                cursor.close()
                exit = input("뒤로가려면 아무키나 눌러주세요.")

```

---

### 전체 주문 내역

```
            # 주문 목록
            elif mum == 1: 
                system('cls')
                cursor = conn.cursor(pymysql.cursors.DictCursor) # 딕셔너리 형태

                while True:
                    print("1: 전체 주문 목록\n2: 회원별 주문 목록")
                    num = input("원하시는 메뉴를 선택해주세요(1~2): ")

                    if num == '1':
                        system('cls')
                        print("전체 주문 목록\n")
                        sql_select = "SELECT * FROM order_list"
                        break;

                    elif num == '2':
                        system('cls')
                        member_id = input("회원의 아이디를 입력하세요: ")
                        sql_select = "SELECT * FROM order_list where memberID = '{}'".format(member_id)
                        print()
                        break;

                    else:
                        system('cls')
                        continue

                # 구매내역 조회하기
                cursor.execute(sql_select)
                select_result = cursor.fetchall()

                strFormat = '%-20s%-20s%-20s%-20s%-20s%-30s\n'
                strOut = strFormat % ('Order Number','Member ID', 'Product Name', 'Ordered Quantity', 'total Price', 'Ordered Date') + '\n'

                for row_data in select_result:
                    strOut += strFormat % (row_data['order_id'], row_data['memberID'], row_data['product_name'], row_data['order_qty'], row_data['total_price'], row_data['c_date'])
                
                print(strOut)
                exit = input("뒤로가려면 아무키나 눌러주세요.")
                cursor.close()

```
---

### 상품 추가/업데이트

```
            # 상품 추가
            elif mum == 2:
                cursor = conn.cursor(pymysql.cursors.DictCursor) # 딕셔너리 형태
                system('cls')

                print("상품 목록\n")
                sql_select = "SELECT * FROM item"
                cursor.execute(sql_select)
                result = cursor.fetchall()
            
                strFormat = '%-20s%-20s%-20s%-20s\n'
                strOut = strFormat % ('ID', "name", 'price', 'quantity') + '\n'
                for row_data in result:
                    strOut += strFormat % (row_data['product_id'], row_data['product_name'], row_data['product_price'], row_data['product_qty'])

                print(strOut)
                cursor.close()

                while True:
                    print("새로 추가/업데이트할 상품정보를 입력하세요(exit -> q).")

                    product_id = input("상품 ID: ")
                    product_name = input("상품이름: ")
                    product_price = input("가격 : ")
                    product_qty = input("수량 : ")
                    product_update_date = datetime.now()

                    if product_id == 'q' or product_name == 'q' or product_price =='q' or product_qty == 'q':
                        break

                    try:
                        product_price = int(product_price)
                        product_qty = int(product_qty)
                    
                    except ValueError:
                        print("형식이 올바르지 않습니다.")
                        sleep(3)
                        continue
                    
                    cursor = conn.cursor()
                    sql_item_search = "select * from item where product_id = '{}'".format(product_id)
                    cursor.execute(sql_item_search)
                    search_result = cursor.fetchone()

                    if search_result:
                        cf = input("이미 있는 상품입니다. 업데이트 하시겠습니까?(y/n)")

                        if cf == 'y':
                            sql_update = "update item set product_price = {}, product_qty = {} where product_id = '{}'".format(product_price, product_qty, product_id)
                            update_result = cursor.execute(sql_update)
                            
                            if update_result:
                                print("\n업데이트 되었습니다.")
                                sleep(3)
                                conn.commit()
                             
                            else:
                                print("\n업데이트가 되지 않았습니다. 다시 시도해주세요.")
                                sleep(3)
                        cursor.close()
                        break

                    else:
                        confirm = input("확인하신 내용이 맞습니까?(y/n): ")
                        if confirm == 'y':
                            # DB 업데이트
                            # DB item 테이블에 INSERT

                            sql_insert = '''
                            INSERT INTO item (product_id, product_name, product_price, product_qty, c_date)
                            values(%s, %s, %s, %s, %s)
                            '''
                            values = (product_id, product_name, product_price, product_qty, product_update_date)
                            
                            result_insert = cursor.execute(sql_insert, values)

                            # 상품이 잘 등록 되었다면
                            if result_insert:
                                conn.commit()
                            
                                print("\n상품이 등록되었습니다.")
                                sleep(3)
                            
                            else :
                                print("\n상품등록에 실패하였습니다.")
                                sleep(3)
                            
                            cursor.close()
                            break
                    
                        # y를 누르지 않았을때
                        else:
                            print("취소 되었습니다")
                            sleep(3)
                            cursor.close()
                            break
```
---

### VIP 고객 리스트

```
            elif mum == 3: 

                system('cls')
                print("VIP 고객 리스트\n")
                cursor = conn.cursor()
                
                sql_member_total = "select memberID, sum(total_price) as total from order_list Group by memberID order by sum(total_price) desc"
                cursor.execute(sql_member_total) # 구매한 총 가격
                vip_list = cursor.fetchall()
                
                strFormat = '%-20s%-20s'
                strOut = strFormat % ('Member ID', 'total Price') + '\n\n'
                
                count = 0
                for vip in vip_list:
                    strOut += strFormat % (vip[0], vip[1]) + '\n'

                    # 상위 5종목만 표시
                    if count > 5:
                        break;
                    else:
                        count += 1
                
                print(strOut)
                exit = input("뒤로가려면 아무키나 누르세요.\n")
                cursor.close()
```

---

### 인기 상품 리스트
```
            elif mum == 4: 
                system('cls')
                print("인기 상품 리스트")
                cursor = conn.cursor()
                
                sql_member_total = "select item_id, sum(order_qty) as total_qty from order_list Group by item_id order by sum(order_qty) desc"
                cursor.execute(sql_member_total) # 구매한 총 가격
                best_list = cursor.fetchall()
                
                strFormat = '%-20s%-20s'
                strOut = strFormat % ('Item ID','sold quantity') + '\n\n'

                count = 0
                for best in best_list:
                    strOut += strFormat % (best[0], best[1]) + '\n'
                    
                    # 상위 5종목만 표시
                    if count > 5:
                        break;
                    else:
                        count += 1

                print(strOut)
                exit = input("뒤로가려면 아무키나 누르세요.\n")
                cursor.close()

```

---

### 로그아웃
```
            else:
                # 로그아웃
                break


```