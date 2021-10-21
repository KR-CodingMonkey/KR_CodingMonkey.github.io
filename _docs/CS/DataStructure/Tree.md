---
title: 트리(Tree)
tags: 
 - Tree
 - Binary Tree
 - AVL Tree
description: 트리(Tree)
permalink: docs/CS/DataStructure/Tree
---

# 트리(Tree)

- 정점과 간선을 이용해 사이클을 이루지 않도록 구성한 Graph의 특수한 형태로, 계층이 있는 데이터를 표현하기에 적합하다.

- 트리 중 이진 트리 형태의 구조로, 탐색(검색) 알고리즘 구현을 위해 많이 사용됨 

1. 이진 트리
2. 이진 탐색 트리
3. AVL 트리


## 이진 트리(Binary Tree)
- 각 노드가 최대 두 개의 자식을 갖는 트리
- 이진 트리의 순회는 재귀 호출을 사용한다. 따라서 전위, 중위, 후위 순회를 간단하게 구현할 수 있다. 순회란 모든 원소를 빠트리거나 중복하지 않고 처리하는 연산을 의미한다.

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

## 스레드 이진 트리
- 이진 트리의 위 특징 때문에 시스템 혹은 외부 스택을 관리해야하며 하위 레벨로 내려갈수록 재귀 호출의 깊이가 깊어져 비효율적일 수 있다. 스레드 이진 트리는 재귀 호출 없이 순회할 수 있도록 구현된 트리이다.

## 이진 탐색 트리
- 모든 왼쪽 자식들 <= n < 모든 오른쪽 자식들 (모든 노드 n에 대해서 반드시 참)
- 용도: 데이터 탐색 -> 탐색 속도 logN

<img src='https://blog.penjee.com/wp-content/uploads/2015/11/binary-search-tree-sorted-array-animation.gif'>

```python
def insert(self, node:Node, data):
    if node is None:
        node = Node(data)
    else:
        if node.data > data:    node.left = self.insert(node.left, data)
        elif node.data < data:  node.right = self.insert(node.right, data)
    return node
```

## AVL 트리


## Reference

1. https://blex.me/@baealex/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%9C-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%ED%8A%B8%EB%A6%AC

2. https://www.fun-coding.org/Chapter10-tree.html