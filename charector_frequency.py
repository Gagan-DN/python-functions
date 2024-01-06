
#charecter Frequency
def char_frequency(stri):
    stri=stri.lower()
    frequency={}
    for chart in stri:
        if chart in frequency:
            frequency[chart]+=1
        else:
            frequency[chart]=1
    return frequency
st=input("Enter a string: ")
fre=char_frequency(st)
print("String frequency of each charecter :")
print(fre)
        
