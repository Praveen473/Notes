#---------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------
# a=[["aa","aa","b"],["aa","aa","c"],["ab","a","c"]]
# for i in range(3):
#     for j in range(3):
#         print(a[i][j])
# dict={}
# for i in range(3):
#     for j in range(3):
#         element=a[i][j]
#         dict[element]=dict.get(element,0)+1 // dict[a[i][j]]=dict.get(a[i][j],0)+1
# for i in dict:
#     print(i,dict[i])
#---------------------------------------------------------------------------------------------------------------
#question
"""Takes an m x n matrix (2D list) of characters or strings.
For each cell in the grid:
Checks its neighbors in diagonal, horizontal, and vertical directions.
If any neighbor has the same value as the current cell, return False.
If more than one duplicates among neighbors are found for all cells, return True."""
from logging import exception
# a=[["aa","aa","b"],["aa","aa","c"],["ab","a","c"]]
# dir=[(0,1),(1,0),(1,1)]
# for i in range(3):
#     for j in range(3):
#         dict={}
#         for dx,dy in dir:
#             nx,ny=i+dx,j+dy
#             if 0<=nx<3 and 0<=ny<3:#------------------important for checking out of bounds--------------------------
#                 dict[a[i][j]]=dict.get(a[i][j],0)+1
#         for kk,v in dict.items():
#             if v>4:
#                 print("False")
# print("True")
#--------------------------------------------------------------------------------------------------------------------
# a=[["aa","cc","b"],["a","zz","b"],["ab","a","c"]]
# dir=[(0,1),(1,0),(1,1)]
# for i in range(1):
#     for j in range(3):
#         if i+1<3 and a[i][j]==a[i+1][j]:
#             print(i+1,j, a[i][j])
#         if j+1<3:
#             print(i,j+1,"valid")
#         if i+1<3 and j+1<3:
#             print(i+1,j+1,"valid")
#--------------------------------------------------------------------------------------------------------------------
# """from collections import defaultdict
# def process_codes(s):
#     seen = set()
#     count = defaultdict(int)
#     duplicate = set()
#     i = 0
#     while i < len(s):
#         stream = s[i].upper()
#         code = s[i+1:i+3]
#         tag = stream + code
#         if tag in seen:
#             duplicate.add(stream)
#         else:
#             seen.add(tag)
#             count[stream] += 1
#         i += 3
#     result = []
#     for key in ['S', 'C', 'H', 'D']:
#         if key in duplicate:
#             result.append("duplicate")
#         else:
#             result.append(str(13 - count.get(key, 0)))
#     print(" ".join(result))"""
#--------------------------------------------------------------------------------------------------------------------
#odd even inorder rotation
# def rotate(i,a):
#         for j in range(i+1,len(a)):
#             if a[j]%2==0:
#                 temp=a[i]
#                 a[i]=a[j]
#                 a[j]=temp
#                 break
#         return a
# a=[1,2,3,6,5]
# for j in range(len(a)):
#
#     if a[j]%2!=0:
#             rotate(j,a)
# for i in a:
#     print(i,end=' ')
# print(" ")
#-------------------------------------------------------------------------------------------------------------------
#odd even inorder rotation effective
# a = [1, 2, 3, 6, 5]
# even_index = 0
# for i in range(len(a)):
#     if a[i] % 2 != 0:
#         # Find the next even number after index i
#         for j in range(i + 1, len(a)):
#             if a[j] % 2 == 0:
#                 a[i], a[j] = a[j], a[i]
#                 break
# print(*a)-shorthand
#-------------------------------------------------------------------------------------------------------------------
#sorted odd even
# a=[1,2,3,6,5]
# even=sorted([i for i in a if i%2==0])
# odd=sorted([i for i in a if i%2!=0])
# res=even+odd
# print(res)
#__________________________________________________________________________________________________________________
#second largest
# a=[1,2,3,4,0,7,9,2]
# fir=a[0]
# sec=a[1]
# for i in range(2,len(a)-1):
#     if a[i]<sec:
#         if a[i]<fir:
#             sec=fir
#             fir=a[i]
#         else: sec=a[i]
# print(fir,sec)
#__________________________________________________________________________________________________________________
#two sum
# def twoSum(nums, target):
#     num_map = {}  # Step 1: Create an empty dictionary to store number -> index
#
#     for i, num in enumerate(nums):  # Step 2: Loop through the list
#         complement = target - num  # Step 3: Calculate what number we need to reach the target
#
#         if complement in num_map:  # Step 4: Check if that number is already in the dictionary
#             return [num_map[complement], i]  # Step 5: If yes, return the stored index and current index
#
#         num_map[num] = i  # Step 6: Else, store the current number with its index in the dictionary
#__________________________________________________________________________________________________________________
#combination two sum
#two combination important
# def call(arr, tar, res, index):
#     current_sum = sum(res)
#     if current_sum > tar:
#         return
#     if current_sum == tar:
#         print(res)
#         return
#     #without loop
#     if index >= len(arr):
#         return
#     #for i in range(index, len(arr)):
#     call(arr, tar, res + [arr[index]], index + 1)
#     call(arr, tar, res, index + 1)
# a=[1,2,3,4,5]
# t=7
# index=0
# call(a,t,[],0)
#_______________________________________________________________________________________________________________
# def call(a):
#     if a==10:
#         raise exception("give a number less than 10")
# call(9)
#__________________________________________________________________________________________________________________


#_______________________________________________________________________________________________________________




#__________________________________________________________________________________________________________________
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class ll:
#     def creating(self,head):
#         n=Node(head[0])
#         curr=n
#         for i in head[1:]:
#             curr.next=Node(i)
#             curr=curr.next
#         return n
#     def printll(self,head):
#         while head!=None:
#             print(head.data)
#             head=head.next
#
#     def reverse(self,curr):
#         prev=None
#         while curr:
#             nextnode=curr.next
#             curr.next=prev
#             prev=curr
#             curr=nextnode
#         return prev
# l=ll()
# a=[1,4,3,5]
# c=l.creating(a)
# l.printll(c)
# d=l.reverse(c)
# l.printll(d)

#__________________________________________________________________________________________________________________
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# class BST:
#     # Insert a value into the BST
#     def insert(self, root, key):
#         if root is None:
#             return Node(key)
#         if key<root.data:
#             root.left=self.insert(root.left,key)
#         else:
#             root.right=self.insert(root.right,key)
#         return root
#
#     # In-order traversal (prints sorted elements)
#     def inorder(self, root):
#         if root:
#             self.inorder(root.left)
#             print(root.data, end=" ")
#             self.inorder(root.right)
#
#
# # Main code
# arr = [1,2,5,4,3]#list(map(int, input("Enter elements of the array separated by space: ").split()))
# bst = BST()
# root = None
#
# # Insert each element into BST
# for num in arr:
#     root = bst.insert(root, num)
#
# print("In-order Traversal of BST:")
# bst.inorder(root)
#__________________________________________________________________________________________________________________
# a="asdfg"
# for i in range(len(a)-1,-1,-1):
#     print(a[i])
# print(a[::-1])
#__________________________________________________________________________________________________________________
#building graph

# from collections import deque
# class graph:
#     def bfs(self,g,start):
#         visited=set()
#         queue=deque([start])
#         print(queue)
#         visited.add(start)
#         while queue:
#             que=queue.popleft()
#             for nei in g[que]:
#                 if nei not in visited:
#                     visited.add(nei)
#                     queue.append(nei)
#         print("BFS\n")
#         print(*visited)
#
#     def dfs(self,g,start,vis=None):
#         if vis is None:
#             vis=set()
#         vis.add(start)
#         print(vis,end=' ')
#         for nei in g[start]:
#             if nei not in vis:
#                 self.dfs(g, nei, vis)
#         return vis
#
#     def build(self):
#         a=int(input())
#         b=int(input())
#         g={}
#         for i in range(a):
#             g[i]=[]
#         for _ in range(b):
#             u,v=map(int,input().split())
#             g[u].append(v)
#             g[v].append(u)
#         for node in g:
#             print(f"{node} --> {g[node]}")
#         return g
# a=graph()
# res=a.build()
# a.bfs(res,0)
# vis=set()
# res1=a.dfs(res,0,vis)
#print(*res1)

#minimum spanning tree


#shorest path



# a=[1,2,3,4,5]
# t=7
# res={}
# for i in range(len(a)):
#     c=t-a[i]
#     if c not in res:
#         res[a[i]]=c
#     if c in res:
#         print("found",c,a[i],res)

# a = [1, 2, 3, 4, 5]
# t = 7
# res = {}  # store value: index
# for i in range(len(a)):
#     c = t - a[i]
#     if c in res:
#         print(f"Found pair: ({c}, {a[i]})")  # print the pair that sums to t
#         break
#     res[a[i]] = i  # store current number for future lookups
# print(res)

#__________________________________________________________________________________________________________________
#Binary Tree
# class Tree:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
# def build_btree(arr):
#     root=Tree(arr[0])
#     queue=[root]
#     i=1
#     while i<len(arr):
#         root1=queue.pop(0)
#         if i<len(arr):
#             root1.left=Tree(arr[i])
#             queue.append(root1.left)
#             i=i+1
#         if i<len(arr):
#             root1.right=Tree(arr[i])
#             queue.append(root1.right)
#             i=i+1
#     return root
# #pre order
# def print1(res):
#     if res!=None:
#         print(res.val)
#         print1(res.left)
#         print1(res.right)
# def isBalanced(root):
#     def dfs(node):
#         if not node:
#             return 0  # height of an empty tree is 0
#         left = dfs(node.left)
#         if left == -1:
#             return -1  # left subtree is unbalanced
#         right = dfs(node.right)
#         if right == -1:
#             return -1  # right subtree is unbalanced
#         if abs(left - right) > 1:
#             return -1  # current node is unbalanced
#         return 1 + max(left, right)  # return height of this node's subtree
#
#     return dfs(root) != -1
#
#
#
# def search(res,t):
#     if res==None:
#         return False
#     if res.val==t:
#         return True
#     return search(res.left,t) or search(res.right,t)
#
# arr=list(map(int,input().split(' ')))
# res=build_btree(arr)
# print1(res)
# res=isBalanced(res)
# a=search(res,5)
# print("found",a)

#__________________________________________________________________________________________________________________



#__________________________________________________________________________________________________________________
#Tree
# # Define the structure of a binary tree node
# class TreeNode:
#     def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# # Solution class with the hasPathSum method
# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         def path(node, current_sum):
#             if not node:
#                 return False
#
#             current_sum += node.val
#
#             # If it's a leaf node and the current sum equals the target sum
#             if not node.left and not node.right:
#                 return current_sum == targetSum
#
#             # Recursively check left and right subtrees
#             return path(node.left, current_sum) or path(node.right, current_sum)
#
#         return path(root, 0)
#
# # Helper to build a sample binary tree:
# #       5
# #      / \
# #     4   8
# #    /   / \
# #  11  13  4
# #  / \       \
# # 7   2       1
#
# # Construct the binary tree
# root = TreeNode(5)
# root.left = TreeNode(4)
# root.right = TreeNode(8)
#
# root.left.left = TreeNode(11)
# root.left.left.left = TreeNode(7)
# root.left.left.right = TreeNode(2)
#
# root.right.left = TreeNode(13)
# root.right.right = TreeNode(4)
# root.right.right.right = TreeNode(1)
#
# # Create solution instance and call the method
# sol = Solution()
# targetSum = 22
# print("Has path sum:", sol.hasPathSum(root, targetSum))  # Output: True


#__________________________________________________________________________________________________________________
#stack


#__________________________________________________________________________________________________________________
#queue


#__________________________________________________________________________________________________________________
#deque



#__________________________________________________________________________________________________________________
#permutation
# def per(arr,t,ar,res):
#     c = sum(ar)
#     if c>t:
#         return
#     if c==t:
#         res.add(tuple(ar))
#         return
#     for i in range(len(arr)):
#             per(arr,t,ar+[arr[i]],res)
#     return ar
#
# a=[1,2,3,4,5,6]
# t=7
# res=set()
# res1=per(a,t,[],res)
# print(res)
#

#__________________________________________________________________________________________________________________

"""✅ Reason:
Sets in Python can only store hashable (immutable) types, like:
int, float, str
tuple (if it only contains hashable elements)
But:
list is mutable and not hashable, so it cannot be added directly to a set."""
#res.add(ar)  ---res.add(tuple(ar))

# def find_combinations(arr, target, start=0, path=[], result=[]):
#     if sum(path) == target:
#         result.append(path)
#         return
#     if sum(path) > target:
#         return
#     for i in range(start, len(arr)):
#         find_combinations(arr, target, i + 1, path + [arr[i]], result)
#
# a = [1, 2, 3, 4, 5, 6]
# target = 7
# result = []
# find_combinations(a, target, result=result)
# print("Combinations:")
# for r in result:
#     print(r)

#__________________________________________________________________________________________________________________
#permutation
def find_permutations(arr, target, path, used, result):
    if sum(path) == target:
        result.append(path)
        return
    if sum(path) > target:
        return
    for i in range(len(arr)):
        if not used[i]:
            used[i] = True
            find_permutations(arr, target, path + [arr[i]], used, result)
            used[i] = False
'''In permutations where order matters, you want:
        if not used[i]:
            used[i] = True
            used[i] = False #used for stop repeatation
[1, 2] ✅
[2, 1] ✅
But NOT [1, 1]'''

a = [1, 2, 3, 4, 5, 6]
target = 7
result_perm = []
used = [False] * len(a)
find_permutations(a, target, [], used, result_perm)
print("\nPermutations:")
for r in result_perm:
    print(r)
#__________________________________________________________________________________________________________________

#2X2 matrix