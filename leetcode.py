
#!/usr/bin/python
# -*- coding: utf-8 -*-

# q.169
# Given an array of size n, find the majority element. The majority element is the element that appears more than [n/2] times.
# You may assume that the array is non-empty and the majority element always exist in the array
# @param num, a list of integers
# @return an integer

def majority_element(nums):
    if len(nums) == 1:
          return nums[0]
    for n in nums:
        if nums.count(n) > len(nums)/2:
            return n
def diff(a,b):
    b = set(b)
    return [aa for aa in a if aa not in b]
            
def majority_element_v2(nums):
    return max([(nums.count(n),n) for n in set(nums)])[1]
    #list(set(temp1) - set(temp2))            

def test_majority_element():
    assert majority_element([1]) == 1
    assert majority_element([1,2,2,2,2,4]) == 2
    assert majority_element([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) == 1
    
    assert majority_element_v2([1]) == 1
    assert majority_element_v2([1,2,2,2,2,4]) == 2
    assert majority_element_v2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) == 1
    print "test passed"

#q.165
# Compare two version numbers version1 and version1.
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
#
# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.
    
# @param version1, a string
# @param version2, a string
# @return an integer
def compare_version(version1, version2):
    #print version1,version2
    if version1 == version2:
        return 0
    v1_p1,v1_p2 =   version1.split('.',1)  if  '.' in version1  else [version1,'0']
    print v1_p1,v1_p2
    v2_p1,v2_p2 =   version2.split('.',1)  if  '.' in version2  else [version2,'0']
    print v2_p1,v2_p2
    if int(v1_p1) > int(v2_p1):
        return 1
    elif int(v1_p1) == int(v2_p1):
        return compare_version(v1_p2,v2_p2)    
    else:
        return -1 
    
    
    
def test_compare_version():
    #print compare_version('0.1','0.2')
    assert compare_version('1.0','1.0') == 0
    assert compare_version('0.1','0.2') == -1
    assert compare_version('0.1','1.1') == -1
    assert compare_version('13.37','1.2') == 1
    assert compare_version('1','0') == 1
    assert compare_version('0.1','0.0.1') == 1
    print 'test passed'

#q.160
#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class LinkedList:
    def __init__(self,head = None):
        self.head = head
        
    def insert(self,node):
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node    
            
            

# find the node at which the intersection of two singly linked lists begins.
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
# @param two ListNodes
# @return the intersected ListNode

def get_intersection_node(head_a,head_b):
    pass
    
def test_get_intersection_node():
    linkedlst_a = LinkedList()
    linkedlst_a.insert(ListNode('c3')),linkedlst_a.insert(ListNode('c2')),
    linkedlst_a.insert(ListNode('c1')),
    linkedlst_a.insert(ListNode('a1')),linkedlst_a.insert(ListNode('a2'))
    linkedlst_b = LinkedList()
    linkedlst_a.insert(ListNode('c3')),linkedlst_a.insert(ListNode('c2')),
    linkedlst_a.insert(ListNode('c1')),
    linkedlst_a.insert(ListNode('b3')),linkedlst_a.insert(ListNode('b2')),linkedlst_a.insert(ListNode('b2'))
    assert get_intersection_node(linkedlst_a, linkedlst_b) == ListNode('c1')
    

#q. 
#determine whether an integer is a palindrome
#@return a boolean  
def is_palindrome(x):
    return str(x) == str(x)[::-1]
    
    
def test_is_palindrome():
    pass



#q.
#Given a sorted array, remove the dublicates in place such that each element appear only once
#do not allocate extra space for another array, you must do this in place with constant memory
#and return the new lenght
#param a list of integers
#return a integer
def remove_duplicates(A):
    tail = 0 
    for i in range(1,len(A)):
        if A[i] != A[tail]:
            tail+=1
            A[tail] = A[i]
            
        print A
    return tail+1        
            
        
        
    
    #return len(set(A))
    # s = []
#     for a in A:
#         if a not in s:
#             s.append(i)


            
    

def test_remove_duplicates():
    assert  remove_duplicates([1,1,2]) == 2   
    assert  remove_duplicates([1,1,2,2,2,3,3]) == 3   
    print "test passes"



#Given an array an a value, remove all instances of that value in place an return  the new length
#the order of elements can be changed
#param A list of integers
#param elem an integer,value need to be removed
#return an integer
def remove_element(A,elem):
    A[:] = [x for x in A if x != elem]
    return len(A)


def test_remove_element():
    assert  remove_element([1,2,1,1,2,3,4,],1) == 5
    assert  remove_elemtn([1,1],1) == 0
    assert  remove_elemtn([1],1) == 0  


# q.38
# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence
def count_and_say(n):
    "return a string"
    def say(i):
        str_n = str(n)
        result = ""
        total = 0
        for i in str_n:
            count_i = str_n.count(i)
            total += count_i
            if total <= len(str_n):
                result += str(count_i) + str(i)
        yield result
        
    for x in range(1,n):
        say(x)
    
    
        
    
    
    

def test_count_and_say():
    print count_and_say(1)
    # assert count_and_say(1) == "1"
#     print count_and_say(2)
#     assert count_and_say(2) == "11"
#     assert count_and_say(3) == "21"
#     assert count_and_say(4) == "1211"
#     assert count_and_say(5) == "111221"
    print "test passes"
    

# q.66
# Given a non-negative number represented as an array of digits, plus one to the number.
#
# The digits are stored such that the most significant digit is at the head of the list.
# @param digits, a list of integer digits
def plus_one(digits):
    "return a list of integer digits"
    i = 0
    elde = False
    result = []
    for d in reversed(digits):
        print d
        if d == 9:
            result.append(0)
            if i == len(digits)-1 and all(i==9 for i in digits):
                result.append(1)    
            elde = True
        else:
            if (i == 0) or elde:
                d+=1
            result.append(d)    
        i+=1    
    return result[::-1]
            
        
    
    
    
def test_plus_one():
    #print plus_one([0])
    assert plus_one([0]) ==  [1]
    assert plus_one([9]) ==  [1,0]
    assert plus_one([1,0]) ==  [1,1]
    #print plus_one([9,8,7,6,5,4,3,2,1,0])
    assert plus_one([9,8,7,6,5,4,3,2,1,0]) == [9,8,7,6,5,4,3,2,1,1]
   #print plus_one([1,2]) 
    #print plus_one([1,9])
    assert plus_one([1,2]) == [1,3]
    #print plus_one([1,9])
    assert plus_one([1,9]) == [2,0]
    print "test passes"





# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# get_min() -- Retrieve the minimum element in the stack.

class MinStack:
    
    def  __init__(self):
        self.items = []
        self.min_stack = []
        
    def push(self, x):
        "return an integer"
        self.items.append(x)
        print len(self.min_stack)
        if len(self.min_stack) == 0:
            self.min_stack.append(x)
        else:    
            m = self.top()
            if x <= m:
                self.min_stack.append(x)
        
    def pop(self):
        "return nothing"
        e = self.items.pop()
        if self.min_stack:
            if e == self.top():
                self.min_stack.pop()
    def top(self):
       "return an integer"
       return self.min_stack[len(self.min_stack)-1] 

    
    def get_min(self):
        "return an integer"
        return self.top()
        
    def __str__(self):
            return str(self.min_stack)  + ";" + str(self.items)
        
def test_min_stack():
    min_stack = MinStack()
    min_stack.push(1)
    min_stack.push(3)
    min_stack.push(4)
    min_stack.push(2)
    min_stack.push(7)
    min_stack.push(5)
    assert min_stack.get_min() == 1
    print min_stack
    print "test passes"




# q.58
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.

def lengthof_lastword(s):
    """return an integer
    param s, a string
    """
    a = s.split()
    if a:
        return len(a[len(a)-1])
    return 0

def test_lengthof_lastword():
    assert lengthof_lastword("") == 0
    assert lengthof_lastword("H") == 1                
    assert lengthof_lastword("Hello World") == 5
    assert lengthof_lastword("Hello test testtest") == 8                
    print "test passes"
    

#q.28
#Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
def str_str(haystack, needle):
    return haystack.find(needle)
    
    
    
    
def test():
    #test_majority_element()
    #test_compare_version()     
    #test_get_intersection_node
    #test_remove_duplicates
    #test_plus_one()
    #test_min_stack()
    #test_lengthof_lastword() 
    test_count_and_say()   
    

test()
    















    
    













    
            



                