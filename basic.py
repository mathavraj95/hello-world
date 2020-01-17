# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 19:39:07 2019

@author: cosmotron
"""

print("hello",5,end = "\n");print("k")
#a,b,c = input("enter three different datatypes").split()
#d,e,f = [x for x in input("enter three different datatypes").split()]
#g,h,i = map(int,input("enter 3 int").split())

for i in range(1,12):
    print(10*i,end=' ')

n = 2
fact = 1   
for i in range(n,1,-1):
    print("hi")
    fact = fact*i
#hi is not printed for n=0 and 1
n = 5
fact = 1
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        print("hi")
        fact = fact*i
    return fact
print(factorial(n))


#multpiles of 5
for i in range(5,101,5):
    print(i,end=" ")

#decimal to octal
#adding succesive strings to null
n = 9
ans = ""
while n > 0:
    remainder = n%8
    ans = str(remainder) + ans
    n = int(n/8)
print("\n",ans)

#split and map
#a = map(int,input("enter numbers").split())
a = [4,5,6]
b = list(map(factorial,a))
print(b)

#splitting and joining strings
c = ["hello","world"]
d = list(c[0])
print(d)
d = '_'.join(d)
print(d)

#n is positive and non zero
n=6
def fib(n):
    if n>=3:
        return fib(n-1) + fib(n-2) 
    else:
        return 1
print(fib(n))
def recursivesum(a,pos):
    if pos < len (a):
        return a[pos] + recursivesum(a,pos+1)
    else:
        return 0
print(recursivesum(a,0))

def mult_recur(a,b):
    if b>=1:
        return a + mult_recur(a,b-1)
    else:
        print("first")       #basecase return executed first
        return 0
print(mult_recur(3,100))
def print_move(n,fr,to):
    print("move disk "+str(n)+" from "+fr+" to "+to)
def tower(n,fr,to,spare):
    if n==1:
        print(n,"i")
        print_move(n,fr,to)

    else:
        tower(n-1,fr,spare,to)
        print_move(n,fr,to)
        tower(n-1,spare,to,fr)
tower(3,'A','C','B')

#binary search
arr = [2,4,6,8,10,11]
item = 11
def search(item, arr):
    m = int(len(arr)/2)
    mid = arr[m]
    print(arr,m,"hi")
    if item == mid:
        print("re",m)
        return m
    elif item < arr[m]:
      print(m)
      return  search(item,arr[0:m])
    elif item > arr[m]:
        return m + search(item,arr[m:len(arr)])
print(search(item,arr))

pal = "Mr. Owl ate my metal worm"
n = 1
m = 1
def path(m,n):
    if(m==0 and n==0):
        return 0
    if(m==0 or n ==0):
        return 1
    else:
        return path(m-1, n) + path(m, n-1)  
mem = {}
def fibm(n):
    if(n<=1):
        return n
    if n in mem:
        return mem[n]
    else:
        mem[n] = fibm(n-1) + fibm(n-2) 
        return mem[n]
print(fibm(2))

#list comprehension  
#slicing start , end , skip
li = [1,2,3,4,5]
print(li[1:-1]) #start index inclusive end index exclusive
print(li[1:-1:2]) #alternate skip by 2
print(li[:3]) #from start upto index 2
print(li[2:]) #from index 2 upto end
print(li[::-1]) #reverse entire
print(li[1::-1]) # start from index 1 and count backwards
print(li[-2:0:-1]) #reverse inner 

eli = [val for val in li if val%2 == 0]

mat = [ [ 3, -5, -7, 9 ],      
      [ 13, 0, -2, 1 ],
      [ -9, 8, 3, -1 ] ]
r = len(mat) #3 rows
c = len(mat[0])  #4 columns
ans = [[x+y for (x,y) in zip(mat[i], mat[i])] for i in range(r)]

#set
#SET cannot be accessed by index
rolls1 = {2,4,7,6,5,8}
rolls2 = {1,6,8,3,9,7}

rolls_uni = rolls1 | rolls2
rolls_int = rolls1 & rolls2
rolls_xor = rolls1 ^ rolls2
rolls_1d2 = rolls1 - rolls2
rolls_2d1 = rolls2 - rolls1

if rolls2 <= rolls1 :
    print("rolls2 is subset of rolls1")

if rolls1.isdisjoint(rolls2) :
    print("disjoint sets")

#dictionary
#list with non numeric indexes also possible
student = {}
student["name"] = "ABC"
student["courses"] = [ "CS101" , "MA102" , "CS110" ]
glossary = {
    "word1" : "meaning1",
    "word2" : "meaning2"}
keys = [k for k in student]  #gives the INDICES not the values
vals = [student[k] for k in student]  #gives values
student.pop("courses", None) #deletes and updates

rep = [1,2,1,3,4,2,3,2,4,3]
freq = {}
for i in rep:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
