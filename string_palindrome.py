#1 palindrome of string
def is_palindrome(strg):
    temp=strg
    rev=strg[::-1]
    if rev==temp:
        print("The given string is palindrome.")
    else:
        print("The given string is not a palindrome.")
strg=input("Enter a string ; ")
is_palindrome(strg)
