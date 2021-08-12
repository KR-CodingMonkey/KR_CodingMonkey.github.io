---
sort: 3 
---

# Member Mode
---

회원 모드는 네가지 메뉴가 제공된다.<br/> <br/>
1. 상품 목록 조회<br/>
2. 주문 내역<br/>
3. 나의 정보<br/>
4. 로그아웃<br/>

<br/>
## Member_Mode(id:str)

- 동일하게 사용자 메뉴를 만들어주고 키입력을 받습니다.

```
mum = 0
    while(1):    
        system('cls')
        print("┌─────────────────────────────┐")
        print("        Member Mode v0.1")
        print("└─────────────────────────────┘")

        mum = mum % 4;
        if mum == 0: print("\t▶ ", end = '')
        else: print("\t▷ ", end = '')
        print("상품 목록 조회")
        if mum == 1: print("\t▶ ", end = '')
        else: print("\t▷ ", end = '') 
        print("주문한 상품 조회")
        if mum == 2: print("\t▶ ", end = '')
        else: print("\t▷ ", end = '')
        print("나의 정보")
        if mum == 3: print("\t▶ ", end = '')
        else: print("\t▷ ", end = '')
        print("로그아웃\n")
```
<br/>

### 상품 목록
- 상품 목록을 출력하고 아랫줄에 구매할 상품의 아이디/수량을 입력받는다<br/>
- DB item테이블을 조회`SELECT`해서 재고가 더 많다면 주문<br/>
- 상품 목록에서 주문량을 반영해 업데이트`UPDATE`<br/>
- DB order_list 테이블에 주문내역(사용자ID/제품ID 등)을 추가한다`INSERT`

```
        key = ord(getch())    
        if key == 0: 
            key = ord(getch())
            if key == 80: #Down arrow
                mum += 1 
                if mum > 3: mum = 0;

            elif key == 72: #Up arrow
                mum -= 1 
                if mum < 0: mum = 3;

        # 상품 목록
        elif key == 13:
            if mum == 0:
                
                cursor = conn.cursor(pymysql.cursors.DictCursor) # 딕셔너리 형태

                while True:
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
 
                    # fix-it
                    print("상품 구매")
                    order_product_id = input("제품번호(exit -> q): ")  # 주문할 제품번호
                    if order_product_id == 'q':
                        break
                    
                    try:
                        order_product_qty = int(input("제품 수량: ")) # 주문할 제품수량
                    
                    except ValueError:
                        print("숫자를 입력해주세요!!")
                        sleep(4)
                        continue
                        
                    # 상품 재고 조회
                    sql_item_search = "SELECT * FROM item where product_id = '{}'".format(order_product_id)
                    cursor.execute(sql_item_search)
                    search_result = cursor.fetchone() # 회원이 고른 상품 정보

                    if not search_result:
                        print("존재하지 않는 상품입니다.")
                        sleep(3)
                        continue

                    extra_qty = search_result['product_qty'] - order_product_qty # DB 남는 재고

                    if extra_qty >= 0:
                        total_price = order_product_qty * search_result['product_price']
                        print("Total price : %d" % total_price)
                        cf = input("정말로 구매하시겠습니까?(y/n): ")

                        if cf == 'y':
                            # item update
                            sql_item_update = "update item set product_qty = {0} \
                                where product_id = '{1}'".format(extra_qty, order_product_id)
                            update_result = cursor.execute(sql_item_update)

                            # order_list update
                            sql_orderList_insert = "insert into order_list(memberID, item_id, product_name, order_qty,total_price,c_date)\
                                 values(%s, %s, %s, %s, %s, %s)"
                            values = (id, order_product_id, search_result['product_name'],order_product_qty, total_price, datetime.now())
                            insert_result = cursor.execute(sql_orderList_insert, values)
    
                            if update_result and insert_result:
                                print("구매가 완료되었습니다.")
                                conn.commit()
                                sleep(3)
                            else:
                                print("주문이 정상처리 되지 않았습니다. 다시 시도해주세요")
                                sleep(3)

                        else:
                            print("주문이 취소되었습니다.")
                            sleep(3)
                                
                    else:
                        # 재고 부족시
                        print("재고가 부족합니다.")
                        sleep(3)

                    break;

                cursor.close()  
```
<img src="https://user-images.githubusercontent.com/76420201/104859879-8bfe3e80-596b-11eb-8c98-c4ac3a54f79e.GIF" width = "70%">

<br/>

### 주문 내역
- DB order_list 테이블에서 memberID를 키값으로 조회`SELECT`

```                 
            elif mum == 1: 
                system('cls')
                print("구매 내역\n")
                cursor = conn.cursor(pymysql.cursors.DictCursor) # 딕셔너리 형태

                # 구매내역 조회하기
                sql_select = "SELECT * FROM order_list where memberID = '{}'".format(id)
                cursor.execute(sql_select)
                select_result = cursor.fetchall()

                strFormat = '%-20s%-20s%-20s%-20s%-30s\n'
                strOut = strFormat % ('Order Number','Product Name', 'Ordered Quantity', 'total Price', 'Ordered Date') + '\n'

                for row_data in select_result:
                    strOut += strFormat % (row_data['order_id'], row_data['product_name'], row_data['order_qty'], row_data['total_price'], row_data['c_date'])
                
                print(strOut)
                exit = input("\n뒤로가려면 아무키나 눌러주세요.")
                cursor.close()
```
<br/>

### 나의 정보

- 초기화면에 나의정보 출력`SELECT`
- 메뉴선택을 input()으로 받음
- 정보수정`UPDATE` 회원탈퇴`DELETE`
- 아이디 수정 시 이미 존재하는 아이디인지 조회`SELECT` 후 수정`UPDATE`
- 아이디 수정 성공 시 order_list내에 동일한 아이디 모두 수정`UPDATE`

```
            elif mum == 2: 
                system('cls')
                print("나의 정보\n")
                cursor = conn.cursor()

                sql_select = "select * from member where id = '{}'".format(id)

                cursor.execute(sql_select)
                result = cursor.fetchone()

                # 개인정보 출력
                strFormat = '%-20s%-20s%-20s%-20s\n'
                strOut = strFormat % ('ID', "email", 'password', 'create_date')
                strOut += '\n' + strFormat % (result[0], result[1], result[2], result[3])
                print(strOut)

                change_info = input("1) 회원정보 변경\n2) 회원탈퇴\n3) 나가기\n\n원하시는 작업을 선택해주세요(1~3): ")
                
                # 나의 정보 수정하기
                if change_info == '1':
                    while True:
                        system('cls')
                        print("-나의 정보-")
                        print(strOut)

                        print("1) ID \n2) email \n3) password \n4) 나가기")
                        num = input("\n변경하고 싶은 나의정보를 선택하세요(1~3): ")

                        if num == '1':
                            new_id = input("새로운 아이디를 입력하세요: ")
                            sql_select = "select * from member where id = '{}'".format(new_id)
                            
                            # 새로운 ID 가능 여부 조회
                            cursor.execute(sql_select)
                            isExist = cursor.fetchall()

                            if isExist:
                                print("이미 존재하는 아이디 입니다.")
                                sleep(3)

                            else:
                                sql_update = "update member set id = '{}' where id = '{}'".format(new_id, id)
                                result_update = cursor.execute(sql_update)

                                # 구매내역 아이디 바꿔주기
                                sql_orderList_update = "update order_list set memberID = '{}' where memberID = '{}'".format(new_id, id)
                                result_orderList_update = cursor.execute(sql_orderList_update)

                                id = new_id

                                if result_update and result_orderList_update:
                                    print("아이디가 변경되었습니다!")
                                    conn.commit()

                                else:
                                    print("아이디 변경에 실패하였습니다. 다시 시도해 주세요.")
                                
                                sleep(3)
                                break;

                        elif num == '2':
                            new_email = input("새로운 이메일을 입력하세요: ")
                            sql_update = "update member set email = '{}' where id = '{}'".format(new_email, id)
                                        
                            cursor.execute(sql_update)
                            print("이메일이 변경되었습니다.")

                            conn.commit()
                            sleep(3)
                            break

                        elif num == '3':
                            new_password = input("새로운 비밀번호를 입력하세요: ")
                            confirm_password = input("비밀번호를 확인해주세요: ")

                            if new_password == confirm_password:
                                sql_update = "update member set pw = '{}' where id = '{}'".format(new_password, id)

                                cursor.execute(sql_update)
                                        
                                print("비밀번호가 변경되었습니다.")
                                conn.commit()
                                sleep(3)
                                break

                        elif num == 4:
                            break;

                        else: 
                            continue
                    
                # 회원 탈퇴
                elif change_info == '2':
                    confirm = input("회원탈퇴를 하시겠습니까?(y/n): ")

                    if confirm == 'y':
                        sql_delete = "delete from member where id = '{}'".format(id)
                        result = cursor.execute(sql_delete)
                        # print(result[0])

                        if result:
                            #system('cls')
                            print("\n그동안 이용해 주셔서 감사합니다..")
                            
                            conn.commit()
                            sleep(3)
                            return 0

                        else :
                            print("회원탈퇴 실패하였습니다. 다시 진행해 주세요.")
                            sleep(3)
                            return 0

                # 뒤로가기
                elif change_info == '3':
                    pass

                else:
                    pass

                cursor.close()
```
<br/>
### 로그아웃

```
            else:
                # 로그아웃
                break
```
