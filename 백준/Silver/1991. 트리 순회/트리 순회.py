import sys
input = sys.stdin.readline

def preorder(n):
    if n != '.':
        res.append(n)
        preorder(tree[n][0])
        preorder(tree[n][1])

def inorder(n):
    if n != '.':
        inorder(tree[n][0])
        res.append(n)
        inorder(tree[n][1])

def postorder(n):
    if n != '.':
        postorder(tree[n][0])
        postorder(tree[n][1])
        res.append(n)

tree = {}
n = int(input())
for _ in range(n):
    line = input().split()
    tree[line[0]] = [line[1],line[2]]

root = 'A'
res = []
preorder(root)
sys.stdout.write(''.join(res) + '\n')

res = []
inorder(root)
sys.stdout.write(''.join(res) + '\n')

res = []
postorder(root)
sys.stdout.write(''.join(res))