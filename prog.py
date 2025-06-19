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
# print(*a)#shorthand
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


#______________________________________________________________________________________

# def find_pairs(arr, target):
#     seen = set()   #___________________________________Important___________________________________________________
#     for num in arr:
#         if target - num in seen:
#             print((num, target - num))
#         seen.add(num)
#
# find_pairs([3, 7, 5, 1, 9, 2, 8], 10)

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
# class stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,val):
#         self.stack.append(val)
#     def pop(self):
#         if len(self.stack)!=0:
#             self.stack.pop()
#     def print_stack(self):
#         print(self.stack)
#
#
# c=stack()
# c.push(10)
# c.push(20)
# c.push(30)
# c.push(40)
# c.print_stack()
# c.pop()
# c.print_stack()

# class stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,val):
#         mapping = {')': '(', ']': '[', '}': '{'}
#         if val in mapping.values():
#             self.stack.append(val)
#         else:
#             if not self.stack or self.stack[-1] != mapping[val]:
#                 print("not valid")
#             self.stack.pop()
#         print("valid")
#
# c=stack()
# s="()[]{]"
# for i in s:
#     c.push(i)


# mapping = {')': '(', ']': '[', '}': '{'}
# print(mapping.keys())
# print(mapping.values())
#print(mapping[val])
# mapping = {')': '(', ']': '[', '}': '{'}
# for key in mapping:
#     print(f"{key}{mapping[key]}")
# print(mapping[")"])
# val="("
# print("".join([k for k,v in mapping.items() if v==val]))#----------imp------------******************************************

# def call(s):
#     stack=[]
#     operator=("+","-","/","*")
#     for operation in s:
#         if operation in operator:
#             b=stack.pop()
#             a=stack.pop()
#             if operation == "+":
#                 stack.append(a+b)
#             if operation == "-":
#                 stack.append(a-b)
#             if operation == "*":
#                 stack.append(a*b)
#             if operation == "/":
#                 stack.append(a//b)
#         else:
#
#             stack.append(int(operation))
#             print(stack)
#     return stack
#
# tokens3 = ["10", "6", "9", "3", "/", "-", "*"]
# res=call(tokens3)
# print(res)
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
# def find_permutations(arr, target, path, used, result):
#     if sum(path) == target:
#         result.append(path)
#         return
#     if sum(path) > target:
#         return
#     for i in range(len(arr)):
#         if not used[i]:
#             used[i] = True
#             find_permutations(arr, target, path + [arr[i]], used, result)
#             used[i] = False
# '''In permutations where order matters, you want:
#         if not used[i]:
#             used[i] = True
#             used[i] = False #used for stop repeatation
# [1, 2] ✅
# [2, 1] ✅
# But NOT [1, 1]'''
#
# a = [1, 2, 3, 4, 5, 6]
# target = 7
# result_perm = []
# used = [False] * len(a)
# find_permutations(a, target, [], used, result_perm)
# print("\nPermutations:")
# for r in result_perm:
#     print(r)
#__________________________________________________________________________________________________________________

#2X2 matrix
# a=[]
# for i in range(2):
#     res=[]
#     for j in range(2):
#         res.append(j)
#     a.append(res)
# # print(*a)
#
#
# s=["h","e","l","l","o"]
# temp=0
# i=0
# j=len(s)-1
# while(i<j):
#     temp=s[j]
#     s[j]=s[i]
#     s[i]=temp
#     i+=1
#     j-=1
# print(s)

# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
# res=[]
# for i in range(len(nums1)):
#     for j in range(len(nums2)):
#         if nums1[i] == nums2[j]:
#             res.append(nums1[i])
#             nums2[j] = float('inf')
#             break
# print(res)

#________________________________________________________________________________________________________________
# res = ["compaign p1 4", "compaign 4", "compaign p1 4", "compaign p0 7"]
#
# def get_p_value(entry):
#     parts = entry.split()
#     for part in parts:
#         if part.startswith('p') and part[1:].isdigit():
#             return int(part[1:])  # Extract number after 'p'
#     return float('inf')  # If no pN is found, put it at the end
#
# sorted_res = sorted(res, key=get_p_value)
#
# print(sorted_res)

#________________________________________________________________________________________________________________






# a=str(10)
# print(a+str(0))
# s = "aaaaabbc"
# dict = {}
# for i in s:
#     dict[i] = dict.get(i,0)+1
# c=float('inf')
# print(c)


#---------------------logic---------------------------
# nums = [8,1,2,2,3]
# a = sorted(nums)
# dict = {}
# for i, num in enumerate(a):
#     if num not in dict:
#         dict[num] = i
# print(dict)
# res = []
# for i in nums:
#     res.append(dict[i])
# print(*res)


# def calc(x):
#     print("x value is",x)
#     if x <= 1:
#         return x
#     return calc(x - 1) + calc(x - 2)
# print("Number of ways:", calc(3))
# F(0) = 0  for f(5)=f(4)+f(3)
# F(1) = 1
# F(2) = 1
# F(3) = 2
# F(4) = 3
# F(5) = 5
# F(6) = 8

# res=["compaign p1 4","compaign 4","compaign p1 4","compaign p0 4"]
# for i in res:
#     c=i.split()
#     if "p" not in c[1]:
#         key1=int(c[1])
#         print(key1)
#
# # print(*a)
# # for i in res:
# #     c=i.split()
# #     print(c[1][0])

# "compaign p1 4","compaign 4","compaign p1 4","compaign p0 4"





#---------------------logic---------------------------
#particulat sort
# res = ["compaign p1 4", "compaign 4", "compaign p1 4", "compaign p0 4"]
# def get_p_value(k):
#     part=k.split()             #---------------------important---------------------------
#     for i in part:
#         if i.startswith('p') and i[1:].isdigit():
#             return int(i[1:])
#     return float('-inf')
# sort1=sorted(res,key=get_p_value)
# print(sort1)





#------------------------------------Casa Retail AI-------------------------------------------------
# def call(arr,work):
#     arr1=sorted(arr)
#     count=0
#     non_time = 0
#     for i in arr1:
#         time = 0
#         c=i.split()
#         process=c[1][0]
#         if process == "p":
#             time=int(c[2])
#             if time<work:
#                 count+=1
#             else:
#                 count+=call1(time,work)
#         else:
#             non_time=non_time+int(c[1])
#     return count+non_time
#
# def call1(time,work1):
#     count=0
#     while time>0:
#         time=time-work1
#         count+=1
#     return count
# a,b=map(int,input().split())
# work=b*2
# comp=[]
# for i in range(a):
#     comp.append(input())
# res=call(comp,work)
# print(res)

#---------------------logic----------------------------------------------------------------------------------
#using dict
# res = ["compaign p1 4", "compaign 4", "compaign p1 4","compaign p1 7", "compaign p0 7","compaign 3"]
# def call(arr,work):
#     #arr1=sorted(arr)
#     count=0
#     non_time = 0
#     dict={}
#     v=0
#     v_c=0
#     for i in arr:
#         time = 0
#         c=i.split()
#         process=c[1][0]
#         if process == "p":
#             if c[1] in dict:
#                 v=int(dict[c[1]])
#                 v+=int(c[2])
#                 #print(c[1],v)
#                 dict[c[1]]=str(v)
#             else:
#                 dict[c[1]]=c[2]
#         else:
#                 v_c+=int(c[1])
#                 print(c[1], v_c)
#                 dict["Non"] = str(v_c)
#     res=0
#     for key in sorted(dict):
#         print(f"{key}: {dict[key]}")   #---------------------logic---------------------------#####################-
#         res+=call1(int(dict[key]),work)
#     print(res)
# def call1(dic,work):
#     c=0
#     while(dic>0):
#         dic=dic-work
#         c+=1
#     return c
#
# call(res,6)
#---------------------logic---------------------------
# res = ["compaign p1 4", "compaign 4", "compaign p1 4", "compaign p1 7", "compaign p0 7", "compaign 3"]
#
# def call(arr, work):
#     count_dict = {}
#     other_total = 0
#     for i in arr:
#         pat=i.split()
#         if len(pat)==3:
#             pt=pat[1]
#             time=int(pat[2])
#             count_dict[pt]=count_dict.get[pt,0]+time
#         elif len(pat)==2:
#             other_total+=int(pat[1])
#             count_dict["non"]=other_total
#
#     # Sort dictionary by key
#     for key in sorted(count_dict):
#         print(f"{key}: {count_dict[key]}")
#
# call(res, 6)



#------------------------------------Casa Retail AI-------------------------------------------------
# s="12233"
# dict={}
# seen=set()
# bool=True
# for i in range(len(s)-1):
#     if s[i] not in seen:
#         if s[i]==s[i+1]:
#             bool=False
#             dict[s[i]]=dict.get(s[i],1)+1
#         else:
#             if bool==True:
#                 dict[s[i]]=1
#             seen.add(s[i])
# print(dict)
#------------------------------------Casa Retail AI-------------------------------------------------
# nums=38
# print(str(nums))
# num = 38
# c=str(num)
# while num:
#     count = 0
#     for i in c:
#         print(i)
#         count += int(i)
#         print(count)
#     c = str(count)
#     if len(c)==1:
#         break
# print(count)
# res=[]
# image = [[1,1,0],[1,0,1],[0,0,0]]
# for i in image:
#     i.reverse()
#     res.append(i)
#     #res.append(i[::-1])
# print(*res)

#--------------------------------------------------*************logic++++++++++++---------------------------------------
# for i in combinations(nums,p):
#     print(i)
# for i in permutations(nums,p):
#     print(i)

# from itertools import permutations
# from itertools import combinations
# nums = [10,1,2,7,1,3]
# p = 2
# min1 = float('inf')
# min2 = float('inf')
# for i in combinations(nums, p):#--------*************logic++++++++++++---------
#     num = abs(i[0] - i[1])
#     print(num,i)
#     if num < min2:
#         if num < min1:
#             min2 = min1
#             min1 = num
#         else:
#             min2 = num
#     print(min1,min2)
# print(max(min1, min2))



#-----------------------------------------------------------------------------------------
# s = "abcde"
# goal = "cdeab"
# r = len(s)
# res=s
# ans=""
# for i in range(len(s)):
#     res= res[1:r + 1] + res[0]
#     ans+=res
#     print(res)
#     if ans == goal:
#         print("True")
#     ans=""
#-----------------------------------------------------------------------------------------
#a=1,aa=27,ab=28,az=52,
#stack = reverse (hello world)

# class stack:
#     def __init__(self):
#         self.stack=[]
# class st:
#     def __init__(self,val):
#         self.stack=val.stack
#     def call(self,val) :
#         self.stack.append(val)
#     def reverse1(self):
#         for i in range(len(self.stack)):
#             rev=self.stack.pop()
#             print(rev[::-1])
# s=stack()
# c=st(s)
# for i in range(3):
#     c.call(input())
# c.reverse1()
#-----------------------------------------------------------------------------------------
#
# s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# c=s.lower()
# dict={}
# for i in range(len(s)):
#     dict[c[i]]=i+1
# print(dict)
# count=0
# in1=input()
# for i in range(len(in1)):
#     if i<len(in1) and i+1<len(in1):
#         if in1[i]=="a":
#             val=i
#             count=26+dict[in1[i+1]]
#             break
#     if i<1:
#         count=26*dict[in1[i]]+dict[in1[i+1]]
# print(count)

#count=26*dict[in1[i]]+dict[in1[i+1]]
#print(count)
#-----------------------------------------------------------------------------------------
# n=5
# count = 0
# for i in range(1,n + 1):
#     for j in range(i + 1, n + 1):
#         for k in range(j + 1, n + 1):
#             print(i,j,k)
#             if i ** 2 + j ** 2 == k ** 2:
#                 count += 1

# s = "aba"
# print((s+s)[1:-1])
# if s in (s+s)[1:-1]:
#     print((s+s)[1:-1])
# nums=[1,7,3,6,5,6]
# l = 0
# r = 0
# for i in nums:
#     r += i
# print(r)
# for i in nums:
#     r -= i
#     print("r",r)
#     if l == r:
#         print( i)
#     l = l + i
#     print("l",l)

#-----------------------------------------------------------------------------------------
# from itertools import permutations
# s = "aacecaaa"
# a = set(s)
# output = ""
# for j in range(1,len(s)):
#     for i in permutations(a, j):
#         temp = ''.join(i) + s
#         #print(temp)
#         c = temp[::-1]
#         if temp == c:
#             output = temp
#         temp = ""
# print(output)
##-----------------------------------------------------------------------------------------
# import bisect#--isect.insort() sorts lexicographically, like dictionary order: "a" < "aa" < "ab" < "b"-
# -----------------------------------*************logic++++++++++++----
# arr = []
# bisect.insort(arr, 5)
# bisect.insort(arr, 2)
# bisect.insort(arr, 3)
# print(arr[0])  # Output: [2, 3, 5]
##-----------------------------------------------------------------------------------------
import bisect
# from itertools import product
#
# class Solution:
#     def shortestPalindrome(self, s: str) -> str:
#         if s == s[::-1]:
#             return s
#         output = []
#         for length in range(1, len(s) + 1):
#             for i in product(s, repeat=length):
#                 temp = ''.join(i) + s
#                 if temp == temp[::-1]:
#                     output.append(temp)
#         if output:
#             return min(output, key=len)#------------------------------------*************logic++++++++++++----
#         return None
##-----------------------------------------------------------------------------------------

