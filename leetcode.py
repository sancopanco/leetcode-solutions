
#!/usr/bin/python
# -*- coding: utf-8 -*-

# q.169
# Given an array of size n, find the majority element. 
# The majority element is the element that appears more than [n/2] times.
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
# For instance, 2.5 is not "two and a half" or "half way to version three", 
# it is the fifth second-level revision of the second first-level revision.
    
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
    r = "1"
    for i in range(1,n):
        r = say(r)
    return r    
        
def say(s):
    "return a string"
    total = 0
    result = ""
    def adj_count_i(i,c):
        count = 0
        while i < len(s):
            if s[i] == c:
                count+=1
            else:
                break    
            i+=1
        return count
    for i in range(len(s)):
        c_i = adj_count_i(i,s[i])
        total += c_i
        print c_i,i,s[i]
        if total <= len(s):
            result += str(c_i) + s[i]
    return result
         
    
def test_count_and_say():
    # assert say("1") == "11"
#     assert say("11") == "21"
#     assert say("21") == "1211"
#     assert say("1211") == "111221"
#     assert count_and_say(1) == "1"
#     assert count_and_say(2) == "11"
#     assert count_and_say(3) == "21"
#     assert count_and_say(4) == "1211"
#     assert count_and_say(5) == "111221"
    assert count_and_say(6) == "312211"
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
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
# return the length of last word in the string.
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
    

# q.110
# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more than 1.
#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def is_balanced(root):
    """return a boolean
    param root, a tree node
    """
    return depth(root) != -1;
        

def depth(root):
    if root == None:
        return 0
    ldepth = depth(root.left)
    #if ldepth == -1: return -1
    rdepth = depth(root.right)
    #if rdepth == -1: return -1    
    if abs(ldepth-ldepth) > 1:
        return -1
    return max(ldepth,rdepth) + 1    
        

            
        
    
    
def test_is_balanced():
    print "not implemented"    


# q.67
# Given two binary strings, return their sum (also a binary string).
# For example,
# a = "11"
# b = "1"
# Return "100".   
def add_binary(a,b):
    """return a string
    param a, a string
    param b, a string
    """
    max_len = max(len(a),len(b))
    a = a + (max_len-len(a))*'0'
    b = b + (max_len-len(b))*'0'
    result = "" 
    elde = 0 
    for i in range(max_len):
       a_i,b_i = int(a[i]),int(b[i])
       if (a_i + b_i+elde) == 2:
           elde = 1
           t = 0
       else:
          t = (a_i + b_i+elde)%2
       result += str(t)
       if (i == max_len-1) and elde:
           result+="1"
    return result[::-1]
    
    
def test_add_binary():
    #print add_binary("11","1")
    assert add_binary("1","0") == "1"
    assert add_binary("1","1") == "10"
    assert add_binary("11","1") == "100"
    assert add_binary("11","11") == "110"
    assert add_binary("1010","1011") == "10101"  #"10110"
                                         #01101      




# Reverse digits of an integer.
# Example1: x = 123, return 321
# Example2: x = -123, return -321
# If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.
# Did you notice that the reversed integer might overflow?
# Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. 
#How should you handle such cases?
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows
def reverse(x):
    "return an integer"
    sign = 1 
    if(x < 0):
        sign = -1 
    y,result = abs(x),0
    while y > 0:
        d = y % 10
        print d,y,result
        y = y / 10
        result = result * 10
        print d,y,result
        result = result + d
        print result
    return sign*result    
    
def test_reverse():
    assert reverse(123) == 321
    assert reverse(1) == 1
    assert reverse(-1) == -1
    assert reverse(11) == 11
    assert reverse(-123) == -321
    assert reverse(1534236469) == 0 # overflow
    print "test passes"    
    

# 
# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.
def roman_to_int(s):
    "return an integer"
    {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    
    
    
def test_roman_to_int():
    pass

# q.125
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
def is_valid(s):
    "return a boolean"
    st = []
    for c in s:
        if c in "({[":
            st.append(c)
        else:
            if len(st) == 0: return False
            last = st.pop()
            if (c == ")") and ("(" != last): return False    
            if (c == "]") and ("[" != last): return False
            if (c == "}") and ("{" != last): return False
    return len(st) == 0        
    
    
def test_is_valid():
    assert is_valid("()") == True
    assert is_valid("()[]{}") == True
    assert is_valid("(]") == False
    assert is_valid("([)]") == False 
    print "test passes"   



# Implement atoi to convert a string to an integer.
# Hint: Carefully consider all possible input cases.
# If you want a challenge, please do not see below and ask yourself what are the possible input cases.
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
# You are responsible to gather all the input requirements up front#
# The function first discards as many whitespace characters as necessary 
# until the first non-whitespace character is found. Then,
# starting from this character, takes an optional initial plus or 
#  minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
# The string can contain additional characters after those that form the integral number,
#  which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number,
# or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
# If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned

def atoi(str):
    "return an integer"
    pass

def test_atoi():
    pass





#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.data = x
        self.next = None
        
    def get_data(self):
        return self.data
        
    def get_next(self):
        return self.next    
        
    def set_data(self,newdata):
        self.data = data 
        
    def set_next(self,newnext):    
        self.next = newnext
            
class UnorderedList:
    def __init__(self):
        self.head = None
    #O(1)    
    def is_empty(self):
        return self.head == None    
    #O(1)    
    def add(self,item):
        tmp =  ListNode(item)
        tmp.set_next(self.head)
        self.head = tmp
    #O(n)
    def size(self):
        current = self.head
        count = 0
        while current:
            current = current.get_next()
            count = count + 1
        return count
    #O(n)
    def search(self,item):
        current = self.head
        found = False
        while current and (not found):
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()            
        return found
    #O(n)
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if not previous:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())                 
            
    def insert(self,node):
        
        pass
    def index(self):
        pass
    def pop(self):
        pass
    def append(self):
        pass         
    def __str__(self):
        current = self.head
        r = []
        while current:
            r.append(str(current.get_data()))
            current = current.get_next()
        return "->".join(r)                

class OrderedList:
    def __init__(self):
        self.head = None
    
    #O(n)    
    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current and (not found and not stop):
            if current.get_data() == item:
                found = True
            else:
                if current.get_data > item:
                    stop = True
                else:
                    current = current.get_next()
        return found
    #O(n)
    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()
                
        tmp = ListNode(item)
        if not previous:
            tmp.set_next(self.head)
            self.head = tmp
        else:
            tmp.set_next(current)
            previous.set_next(tmp)
            
    def __str__(self):
        current = self.head
        r = []
        while current:
            r.append(str(current.get_data()))
            current = current.get_next()
        return "->".join(r)    
            
                              
        
                    
                    
                
                    
            
            
# q.160
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
    mylist = UnorderedList()
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)
    assert get_intersection_node(linkedlst_a, linkedlst_b) == ListNode('c1')
        
        

# q.2
# You are given two linked lists representing two non-negative numbers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

def add_two_numbers(l1,l2):
    "return a ListNode"
    head = ListNode()
    current_1,current_2 = l1,l2
    c = 0
    while current_1:
        d_1 = current_1.data
        d_2 = current_2.data
        add = (d_1+d_2+c);
        c = add/10;
        digit = ListNode(add%10)
        digit.next = head
        head = digit
        current_1 = current_1.next
    return head    
    
    

def test_add_two_numbers():
    l1 = UnorderedList()
    l1.add(3)
    l1.add(4)
    l1.add(2)
    print l1
    
    l2 = OrderedList()
    l2.add(4)
    l2.add(6)
    l2.add(5)
    print l2
    
    r = OrderedList()
    l2.add(8)
    l2.add(0)
    l2.add(7)
    
    assert add_two_numbers(l1,l2) == r    

# Find the contiguous subarray within an array (containing at least one number) which has the largest sum
# If you have figured out the O(n) solution,
# try coding another solution using the divide and conquer approach, which is more subtle.
def max_sub_array(A):
    pass
    
#O(n)    
def max_sub_array_v2(A):
    max_so_far = 0
    max_ending_here = 0 
    for a in A:
        max_ending_here = max_ending_here + a
        if max_ending_here < 0:
             max_ending_here = 0
        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return  max_so_far   
    
#O(n)Kadane's algorithm 
def max_sub_array_v3(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far    
        
    
def test_max_sub_array():
    print max_sub_array_v3([-2, -3, 4, -1, -2, 1, 5, -3])
    #assert max_sub_array_v2([-2, -3, 4, -1, -2, 1, 5, -3]) == 4
    assert max_sub_array_v3([4, -2, 7, 4, -8, -6, 2, 9, 1, 0, -4]) == 13
    assert max_sub_array_v3([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert max_sub_array_v3([-2,1,-3,4,-1,2,1,-5,4]) == 6 #[4,-1,2,1]
    print "test passes"

# q.69
# Compute and return the square root of x.    
def sqrt(x):
    """return an integer
    param x, an integer
    """
    def good_enough(guess):
        precision = 0.001
        f = abs(guess ** 2 - x)
        return (f < precision)
        
    def improve(guess):
        return (guess + x/guess) / 2.0
            
    counter = 1
    guess = 1
    while not good_enough(guess) and counter <= 100:
        guess = improve(guess)
        counter += 1
    assert counter <= 100,'100 iterations done and no good answer'        
    return int(guess)
                
def test_sqrt():
    assert sqrt(0) == 0
    assert sqrt(4) == 2
    assert sqrt(5) == 2
    assert sqrt(11) == 3
    print "test passes"    
    
# q.3
# Given a string, find the length of the longest substring without repeating characters. For example,
# the longest substring without repeating letters for "abcabcbb" is "abc",
# which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
def length_of_longest_substring(s):
    "return an integer"
    if len(s) == 0: return 0 
    curr_len = 1
    max_len = 1
    prev_index =  None
    visited = {}
    visited[s[0]] = 0
    for i in range(1,len(s)):
        prev_index = visited.get(s[i],-1)
        if prev_index == -1 or i - curr_len > prev_index:
            curr_len = curr_len + 1
        else:
            if curr_len > max_len:
                max_len = curr_len
            curr_len = i - prev_index    
        visited[s[i]] = i   
    if curr_len > max_len:
        max_len = curr_len    
        
    return max_len;        
        
def test_length_of_longest_substring():
    assert length_of_longest_substring("abcabcbb") == 3#"abc"
    assert  length_of_longest_substring("ABDEFGABEF") == 6#"BDEFGA"
    assert length_of_longest_substring("bbbbb") == 1#"b"
    assert length_of_longest_substring("") == 0
    print "test passes"
        

        

    
def test():
    #test_majority_element()
    #test_compare_version()     
    #test_get_intersection_node
    #test_remove_duplicates
    #test_plus_one()
    #test_min_stack()
    #test_lengthof_lastword() 
    #test_count_and_say() 
    #test_is_balanced()
    #test_add_binary()
    #test_reverse() 
    #test_roman_to_int()
    #test_is_valid()
    #test_add_two_numbers()
    #test_max_sub_array()
    #test_sqrt()
    test_length_of_longest_substring()

test()
    















    
    













    
            



                