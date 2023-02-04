'''import random as r
x="i love friends"


print(r.sample(x,8))


#everytime it give different output

a=[1,2,3,4,5,6]
r.shuffle(a)
print(a)


b=[1,2,3,4,5,6,7]
print(r.choice(b))


a=r.random()
print(a)


#will return random numbers  between 0.0 to 1.0

#0.0 include 1.0 excludes

print(r.randint(20,30))

a=[10,20,30,40,50]
print(r.choices(a,k=8))


a="hello good day"
print(r.choices(a,k=3))


#================

#display whole year calendar

import calendar

print("full calendar")
print(calendar.calendar(2022))


print("particular ,month")
print(calendar.month(2021,3))

print("set first day of the week")
calendar.setfirstweekday(calendar.sunday)
print(calendar.month(2022,3))


#================
def sample():#def or des
    print("great day")
    print("happy time")
sample()

#==================
#without arguement,without return value
def multi():
   n1=int(input("number"))
   n2=int(input("number"))
   n3=int(input("number"))
   prod=n1*n2*n3
   print(prod)

multi()

#===============

#without arguement,with return value
def multi():
   n1=int(input("number"))
   n2=int(input("number"))
   n3=int(input("number"))
   prod=n1*n2*n3
   return(prod)

res=multi()
print(res)  


#==================

#with arguement,with return value
def multi(n1,n2,n3):
   prod=n1*n2*n3
   print(prod)
   
print(2,3,4)


#==================

def lemons():
    inhand=int(input("enter no.of lemons:"))
    if inhand>21:
        print("you have",inhand-21,"excess lemons")
    elif inhand<21:
        print("you have to buy",21-inhand,"lemons")
    else:print("you have enough lemons")
lemons() 

#================
 
#sum of digits of given numbers

def digits(n):
    sum=0
    while n!=0:
        rem=n%10
        sum=sum+rem
        n=n//10
    return sum
n=int(input("enter the number"))
res=digits(n)
print(res)


#==========================

# recursive function

def display():
     n=int(input("enter a number"))
     if n==1:
         display()
     else:
        print("over")

display() 


#==================

#RECURSIVE FUNCTION

def fact(n):
    if n==0:
        return 1
    return n* fact(n-1)

result=fact(8)
print(result)'''


#==================

n=int(input("enter number:"))
a=0
b=1
sum=0
count=1

while(count<=n):
    print(sum,end=" ")
    count+=1
    a=b
    b=sum
    sum=a+b
































