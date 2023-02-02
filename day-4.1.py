'''d={n:n*n for n in range(1,5)}
print(d)



#calculating product price for 5 units
old={'rice':60,'dhaal':120,'oil':150}
new={product :price*5 for (product,price)in old.items()}
print(new)


#WITH CHECKS
real={'sam':24,'angel':18,'kumar':35}

now={name:age for (name,age) in real.items() if age>20}
print(now)



#dictionary


import random

cust={"virat","abd","gayle"}
cust_dict={names:random.randint(1,100) for names in cust}
print(cust_dict)


#keys and values from two iterables-zip function

l1=['a','b','c']
l2=[2,3,5]
d={a:b for (a,b) in zip (l1,l2)}
print(d)


#=======================
import random
student_names=list(map(str,input("enter names:").split()))
marks= []
for i in range(len(student_names)):
    a=(random.randint(300,500)/500)*100
    marks.append(a)
dict={x:y for (x,y) in zip(student_names,marks)}
print(dict)'''


'''#======================


s=input("enter the string value")
ch=input("enter the character")
if ch in s:
    print("character is present:",character)
else:
    print("character is not present")'''


#==============


'''s="racecar"
if s[::-1]==s:
    print("it is a palindrome")
else:
    print("it is not a palindrome")'''
    

'''#============

s=input("enter a string")
space=0
if " " in s:
    for i in s:
        if i==" ":
            space=space+1
    print(space,"spaces")
else:
         print("string doesnot contain spaces")'''



#==============


