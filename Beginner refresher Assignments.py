#!/usr/bin/env python
# coding: utf-8

# # Loops

# In[1]:


n = 11
for i in range(0,n,2):
    print(i)


# In[ ]:





# In[2]:


n=10
i=0
while i<=n:
    print(i)
    i+=2


# In[6]:


n = 10
for i in range(n+1):
    if i % 2 ==0:
        print(i)


# In[8]:


n = 10
i =1
while i<=n:
    print(i,end=' ')
    i+=1


# In[16]:


n = 10
i = 10
while i >=1:
    print(i)
    i-=1


# In[17]:


n = 10
for i in range(1,n+1,1):
    print(i,end=' ')


# In[18]:


n = int(input())
for i in range(n,0,-1):
    print(i,end=' ')


# In[34]:


n = int(input())
sum = 0
i = 1
while i <=n:
    i+=1
    sum+=i
print(sum)



# In[32]:


summ(n)


# In[35]:


n = 10
sum =0

for i in range(n+1):
    sum+=i
print(sum)


# # Functions

# In[43]:


def Interest(p,c,t=2,r=1):
  return p*t*r


# In[44]:


Interest(10,2)


# In[58]:


def volume_of_sphere(r):
    a = (4*(22/7)*(r**3))/3
    return a



# In[59]:


volume_of_sphere(100)


# In[60]:


def area_of_circle(r):
    a = (22/7)*(r**2)
    return a


# In[61]:


area_of_circle(15)


# In[64]:


list1=[2,12,45,6,8,32,17]
for i in list1:
    if i == 6:
        print('element exist')


# In[68]:


e_count = list1.count(6)
if e_count > 0:
    print("Yes, 6 exists in list")
else:
    print("No, 6 does not exists in list")


# In[69]:


if 6 in list1:
    print('element exist')


# # Lists

# In[7]:


list1=[2,12,45,6,8,32,17]
for i in range (len(list1)):
    if list1[i] == 32:
        print(i)
        break


# In[10]:


def duplicate(a):
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            return True
    return False
    


# In[12]:


duplicate([1,2,3,3,4,5,7,7,7])


# In[20]:


a = [23, 34, 25, 35, 66, 70, 14]
for val in a:
    if (val % 5 == 0) and (val % 7 == 0):
        print(val)


# In[25]:


def multiple(a,x):
    for val in a:
        if val % x==0:
            return val
        
    return -1


# In[29]:


multiple([2,4,12,3,4,5],4)





# In[32]:


def searching(a,b):
    count=0
    for x in a:
        if x == b:
            count+=1
    return count


# In[35]:


searching([1,2,2,5,3,7,7,7,7,7,7],7)


# In[43]:


arr = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]

for i in range(0, 4):
    print(arr[i].pop(), end=" ")
print(arr)


# In[40]:


a = [1,2,3,4,5]
a.pop()


# In[41]:


print(a)


# In[51]:


a = [1,2,4,8,7]
largest = -1
for i in range(len(a)):
    if a[i] > largest:
        largest = a[i]
        idx = i
print(largest)
print(idx)

second_largest = -1
for i in range(len(a)):
    if a[i] != largest and a[i]>second_largest:
        second_largest = a[i]
print(second_largest)


# In[54]:


a = [2,9,6,8,10]
largest = -float('inf')
for val in a:
    if val > largest:
        largest = val
print(f'the first largest value is {largest}')

second_largest = -1
for value in a:
    if value != largest and value  > second_largest:
        second_largest = value
print(f'the second largest value is {second_largest}')
    


# In[65]:


def swap(n_list):
    temp = n_list[0]
    n_list[0] = n_list[-1]
    n_list[-1] = temp
    return n_list


# In[66]:


swap([1,2,3,4,5,6])


# In[62]:


n_list=[1,2,3,4,5,6]
def swap(n_list):
  temp = n_list[0]
  n_list[0] = n_list[-1]
  n_list[-1] = temp
  return n_list
  
swap(n_list)


# # Taking multiple inputs in a list

# In[76]:


n = 1
while n == 1:
    user = input().split()
    if user == ['end']:
        break
    print(user)


# In[78]:


print(user)


# In[91]:


shopping_list = []
item = input()
while item != 'end':
    item = input()
    shopping_list.append(item)
print(shopping_list)


# In[92]:


print(shopping_list)


# # 2D matrices

# In[3]:


A = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]]

B = [[9, 8, 7], 
     [6, 5, 4], 
     [3, 2, 1]] 

res = []
for r in range(len(A)):
    row = []
    for c in range(len(A[0])):
        row.append(A[r][c]+B[r][c])
    res.append(row)
print(row)
print(res)


# In[6]:


word = "Scaler" "Data" "Science"
word_list = list(word)


# In[7]:


print(word_list)


# # Right shift a element

# In[8]:


A = list(map(int,input().split()))
def shift_elements(A):
    last_elements = A[-1]
    for i in range(len(A)-1,0,-1):
        A[i] = A[i-1]
    A[0] = last_elements
    return A


# In[9]:


shift_elements(A)


# In[3]:


def largest_element(arr,n):
    # Initialize maximum in each row 
	max_row = [0] * n 
	
	# Loop through the matrix and find the maximum element in each row 
	for i in range(n): 
		for j in range(n): 
			if arr[i][j] > max_row[i]: 
				max_row[i] = arr[i][j] 
	
	# Print the maximum elements of each row 
	print(max_row) 


# In[4]:


largest_element([
    [1,2,3],[4,5,6],[7,8,9]
],3)


# In[7]:


def largest_element(arr,n):
    max_row = [0]*n
    for r in range(n):
        for c in range(n):
            if arr[r][c] > max_row[r]:
                max_row[r] = arr[r][c]
    print(max_row)


# In[8]:


largest_element([
    [1,2,3],[4,5,6],[7,8,9]
],3)


# In[11]:


def main_diagnol_sum(A):
    sum = 0
    for r in range(len(A)):
        for c in range(len(A[0])):
            if r==c:
                sum+=A[r][c]
    return sum


# In[12]:


main_diagnol_sum([
    [1,2,3],[4,5,6],[7,8,9]
])


# In[13]:


A = [[1,2,3], 
     [4,5,6], 
     [7,8,9]]

#initializing integer B
B = 2

#initializing empty result matrix
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

#iterating over rows
for i in range(len(A)):
   #iterating over columns
   for j in range(len(A[0])):
       result[i][j] = A[i][j] * B

for r in result:
   print(r)


# In[20]:


def scalar_product(A,B):
    result = [
        [0,0,0],[0,0,0],[0,0,0]
    ]
    for r in range(len(A)):
        for c in range(len(A[0])):
            result[r][c]=A[r][c]*B

    for i in result:
        print(i)


# In[21]:


scalar_product([
    [1,2,3],
    [4,5,6],
    [7,8,9]
],2)


# In[24]:


def sum_of_row(A):
    result = []
    for row in A:
        result.append(sum(row))
    return result   


# In[25]:


sum_of_row([
    [1,2,3],
    [4,5,6],[7,8,9]
])


# In[7]:


def transpose(A):
    result = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    for r in range(len(A)):
        for c in range(len(A[0])):
            result[c][r]=A[r][c]
    for i in result:
        print(i)
    


# In[8]:


transpose([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])


# # Strings

# In[1]:


str1 = 'abc'
str2='xyz'
temp = str1
str1= str2
str2 = temp


# In[2]:


print(str2,str1)


# In[3]:


s = 'Python for datascience'
print(s[-3:])
print(s[::-1])
print(s[11:15])


# In[4]:


s1 = 'scaler'
s2 = 'interviewbit'
print(len(s1))
print(len(s2))


# In[8]:


s = 'John.Smith1990@gmail.com'
alphabet = 0
digit = 0
for x in s:
    if x.isalpha():
        alphabet+=1
    elif x.isdigit():
        digit+=1
print(f'the number of alphabets are{alphabet}')
print(f'the number of digits are{digit}')


# In[9]:


str1 = 'Welcome'
print (str1[:6] + ' to Hollywood')


# In[16]:


def modify(string):
    if len(string) < 3:
        return string
    elif string[-3:] == "ing":
        return string + "ly"
    else:
        return string + "ing"


# In[23]:


modify('pythoning')


# In[28]:


words= ['goOd','mORNing','HOW','are','yoU','todAy']

def upper_char(words):
    output=[]
    for i in range(len(words)):
        if words[i][2].isupper():
            output.append(words[i])
    return output

 


# In[29]:


upper_char(words)


# In[31]:


word = "Scaler Academy"
n = len(word)
word1 = word.upper()
word2 = word.lower()

converted_word = ""

for i in range(n):
    if i % 2 == 0:
        converted_word += word2[i]
    else:
        converted_word += word1[i]
print(converted_word)


# # Sets and Dictionary

# In[32]:


a ={101,102,103}
b=a.copy()
b.add(104)


# In[33]:


print(b)


# In[34]:


def frequency(A):
    freq={}
    for char in A:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
    return freq


# In[35]:


frequency('Radha')


# In[40]:


s = {1,2,3,3}
r = {4,5,6}
print(len(s)+len(r))


# In[41]:


dict1 = {'age': 35, 'name': 'abc', 'salary': 45000}

val = dict1['age']

if val in dict1:
    print('This is a member of the dictionary')
else:
    print('This is not a member of the dictionary')


# In[46]:


s = {'x':50,'y':40,'z':30}
sum = 0
for val in s:
    sum+=s[val]
print(sum)
    
    


# In[47]:


bbt = {'Sheldon': 1, 'Leonard': 2}
bbt.update({'Penny': 2})
print(bbt)


# # PROBLEM SOLVING

# In[48]:


def sum_odd_even(A):
    even = 0
    odd = 0
    for x in A:
        if x % 2 == 0:
            even+=x
        else:
            odd+=x
    return[even,odd]


# In[50]:


sum_odd_even([1,2,3,4,5,5,7,7])


# In[57]:


def sum_even(A):
    rows = len(A)
    cols = len(A[0])
    even_no = 0
    for i in range(rows):
        for j in range(cols):
            if A[i][j] % 2 == 0:
                even_no+=A[i][j]
    return even_no


# In[58]:


sum_even([[1,2,3],[4,5,6],[7,8,9]])


# In[61]:


def find_max_row(A):
    rows = len(A)
    cols = len(A[0])
    result = []
    for i in range(rows):
        max_ele=0
        for j in range(cols):
            if A[i][j]>max_ele:
                max_ele=A[i][j]
        result.append(max_ele)
    return result


# In[62]:


find_max_row([[1,2,3],[4,5,6],[7,8,9]])


# In[75]:


def bin_to_dec(A):
    power = 1
    decimal = 0
    while A>0:
        rem = A%10
        d = rem*power
        decimal+=d
        power*=2
        A//=10
    return decimal


# In[77]:


bin_to_dec(1111)


# In[85]:


def count_of_ones(n):
    count=0
    while n>0:
        rem = n %10
        if rem == 1:
            count+=1
        n//=10
    return count
        


# In[86]:


count_of_ones(1101)


# In[87]:


print('Radha')


# In[89]:


def hamming_distance(str1,str2):
    count = 0
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            count+=1
    return count


# In[90]:


hamming_distance('abcde','xycde')


# In[107]:


# Program to find the sum of digits of a number until the sum is reduced to 1 digit.
# Example -> 538769->38 ->11 ->2

def sum_digits(num):
    sum_dig=0
    while num > 0:
        rem = num % 10
        sum_dig+=rem
        num//=10
    return sum_dig
num = int(input())
result = num
while result > 10:
    result = sum_digits(result)
print(result)


# In[102]:


sum_digits(12345671)


# In[104]:


# Program to find the sum of digits of a number until the sum is reduced to 1 digit.
# Example -> 538769->38 ->11 ->2


# Function to find the sum of digits
def sum_digits(num):
    # Initializing the sum to 0
    sum_dig = 0
    # Iterating through the digits of the number
    while num > 0:
        # Extracting the last digit of the number
        rem = num % 10
        # Adding the digits to the sum
        sum_dig += rem
        # Removing the last digit from the number
        num //= 10
    # Returning the sum of digits
    return sum_dig

# Taking the input from the user
num = int(input("Enter a number: "))

# Initializing the result to the number itself
result = num

# Iterating until the result is reduced to a single digit
while result > 10:
    # Calling the function to find the sum of digits
    result = sum_digits(result)

# Printing the result
print(result)


# In[119]:


# Given two sentences, write a program to return the sum of the total number of unique words from each sentence
def count_unique_words(sentence1, sentence2):
    words1 = sentence1.split()
    words2 = sentence2.split()
    unique_words = set(words1 + words2)
    return len(unique_words)

sentence1 = "This is a sentence"
sentence2 = "This is another sentence"

total_unique_words = count_unique_words(sentence1, sentence2)
print(total_unique_words) # prints 8


# In[120]:


def count_unique_word(sentence1,sentence2):
    word1 = sentence1.split()
    word2 = sentence2.split()
    unique_word = set(word1+word2)
    return len(unique_word)


# In[121]:


sentence1 ='Radha is my everything'
sentence2 = 'Krsna is my saviour'
total_unique_word = count_unique_word(sentence1,sentence2)
print(total_unique_word)


# In[114]:





# In[ ]:




