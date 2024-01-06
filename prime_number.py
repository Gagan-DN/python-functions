
#10 cheak prime number function
def is_primeNumber(num):
    flag=True
    if num>0:
        for i in range(1,int(num/2)):
            if num%i==0:
                flag=False
            else:
                flag=True
    else:
        flag=False
    if flag==True:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
    
num=int(input("Enter a number: "))
is_primeNumber(num)
