
#5 Count Vowels
def countVoule(strts):
    count=0
    Strings = strts.lower()
    for i in Strings:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            #if True 
            count+=1
     #check if any vowel found
    if count == 0:
        print('No vowels found')
    else:
        print('Total vowels are :' + str(count))
        

String = input('Enter the string :')
countVoule(String)
