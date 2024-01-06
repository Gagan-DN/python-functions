
#8 greatest commen diviser of two numbers(gcd)
def hcf_gcd(num1,num2):
    if num1==0:
        return num2
    if num2==0:
        return num1
    if num1==num2:
        return num1
    if num1>num2:
        return hcf_gcd(num1-num2,num2)
    return hcf_gcd(num1,num2-num1)

num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
if hcf_gcd(num1,num2):
    print("GCD of ",num1," and ",num2," is ",hcf_gcd(num1,num2))
else:
    print("not found")
    
