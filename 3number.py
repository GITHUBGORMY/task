a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
sum=0
if(a==b) and (b==c) and(c==a):
    sum=(a+b+c)*3
    print("valuesare equal three times their sum = ",sum)
else:
    sum=a+b+c
    print("sum=",sum)

