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

#_________________________________________________________________________________________________________
#__
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

