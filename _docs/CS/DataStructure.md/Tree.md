---
title: 트리(Tree)
tags: 
 - Tree
description: 트리(Tree)
permalink: docs/CS/DataStructure/Tree
---

# 트리(Tree)

- 정점과 간선을 이용해 사이클을 이루지 않도록 구성한 Graph의 특수한 형태로, 계층이 있는 데이터를 표현하기에 적합하다.

- 트리 중 이진 트리 형태의 구조로, 탐색(검색) 알고리즘 구현을 위해 많이 사용됨 


## 이진 트리(Binary Tree)

```python
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)
        

class BinaryTree():
    def __init__(self, root):
        self.root = root

    def insert(self, node:Node, data):
        if node is None:
            node = Node(data)
        else:
            if node.data > data:    node.left = self.insert(node.left, data)
            elif node.data < data:  node.right = self.insert(node.right, data)
        return node

    # DLR
    def preorder(self, node:Node, result:list):
        result.append(node.data)
        if node.left:   self.preorder(node.left, result)
        if node.right:  self.preorder(node.right, result)
        return result

    # LDR
    def inorder(self, node:Node, result:list):
        if node.left:   self.inorder(node.left, result)
        result.append(node.data)
        if node.right:  self.inorder(node.right, result)
        return result

    # LRD
    def postorder(self, node:Node, result:list):
        if node.left:   self.postorder(node.left, result)
        if node.right:  self.postorder(node.right, result)
        result.append(node.data)
        return result
```

## 이진 탐색 트리

## AVL 트리
