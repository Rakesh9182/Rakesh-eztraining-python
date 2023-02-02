l=[]
a,b,c,d=input().split()
l.extend([a,b,c,d])
product,sum=1,0
for i in l:
    product=product*int(i)
    sum=sum+int(i)
if product<750:
        print( product )
else:
     print(sum)
                                          
