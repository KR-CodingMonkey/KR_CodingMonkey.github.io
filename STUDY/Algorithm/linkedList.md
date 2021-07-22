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