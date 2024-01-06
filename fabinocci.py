
#6 Fibonacci Sequence
def fabi(num):
    if num<=1:
        return num
    else:
        return (fabi(num-1)+fabi(num-2))
    
nterms=int(input("Enter the rang :"))
fabi(nterms)
