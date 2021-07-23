# Linked List

Node 구현
- 파이썬에서 링크드 리스트 구현시, 클래스를 활용

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
    
    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
    
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if data == self.head.data:
            temp = self.head
            self.head = self.head.next
            del temp

        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    break
                
                node = node.next

    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                return data
            else:
                node = node.data

```

문제: [표 편집](https://programmers.co.kr/learn/courses/30/lessons/81303)

```python
class row:
    def __init__(self,left,right):
        self.val='O'
        self.left=left
        self.right=right

    def __repr__(self):
        return f'({self.val},{self.left},{self.right})'

def solution(n, k, cmd):
    cur=k
    table=[row(i-1,i+1) for i in range(n)]
    stack=[]
    for line in cmd:
        e=line.split()
        if e[0] == 'C':     # DELETE
            # 삭제 목록에 넣어준다
            stack.append(cur)
            # 양쪽에 연결을 이어준다.
            if table[cur].left == -1:
                table[table[cur].right].left = table[cur].left
            elif table[cur].right == n:
                table[table[cur].left].right = table[cur].right
            else:
                table[table[cur].left].right = table[cur].right
                table[table[cur].right].left = table[cur].left
            # current값을 update한다.
            table[cur].val='X'
            if table[cur].right == n:
                cur = table[cur].left
            else:
                cur= table[cur].right
        elif e[0] == 'Z':   # UNDO
            last_row=stack.pop()
            # 다시 연결을 이어 준다.
            if table[last_row].left == -1:
                table[table[last_row].right].left =last_row
            elif table[last_row].right == n:
                table[table[last_row].left].right = last_row
            else:
                table[table[last_row].right].left = last_row
                table[table[last_row].left].right = last_row
            # table 상태 update
            table[last_row].val='O'
        elif e[0] == 'D':   # DOWN
            for _ in range(int(e[1])):
                cur = table[cur].right
        elif e[0] == 'U':   # UP
            for _ in range(int(e[1])):
                cur = table[cur].left
    return ''.join(map(lambda x: x.val,table))
```