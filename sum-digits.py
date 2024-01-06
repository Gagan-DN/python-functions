
#4 sum of digits
num = input("Enter Number: ")
def nu(num):
    sum = 0
    count=0
    for i in num:
        sum = sum + int(i)
    for i in num:
        count= count + 1
    print("total number of digits is ",count)
    print("total sum of digits is ",sum)
    
nu(num)
