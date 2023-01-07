n =int(input("enter a no"))
num=n
sum=0
while(n>0):
    rem=n%10
    sum=sum+(rem**3)
    n=n//10
    if(sum==num):
        print("armstrong no")
    else:
        print("not a armstrong no")
