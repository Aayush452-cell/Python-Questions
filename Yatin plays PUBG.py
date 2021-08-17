from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getnode(data):
    newNode = Node(data)
    newNode.data = data
    newNode.left = None
    newNode.right = None
    return newNode


def LevelOrder(root, data):
    if (root == None):
        root = getnode(data)
        return root

    if (data <= root.data):
        root.left = LevelOrder(root.left, data)
    else:
        root.right = LevelOrder(root.right, data)

    return root


def constructBST(arr, n):
    if (n == 0):
        return None
    root = None
    for i in range(0, n):
        root = LevelOrder(root, arr[i])
    return root


def countLeftMostCorner(root):
    if root == None:
        return 0

    q = deque()
    q.append(root)
    cnt = 0
    while q:
        n = len(q)
        for i in range(n):
            temp = q[0]
            q.popleft()
            if i == 0:
                cnt += 1

            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
    print(cnt)


t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    arr = [int(item) for item in input().split()]
    root = constructBST(arr, n)
    countLeftMostCorner(root)
