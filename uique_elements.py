
#9 Unique Elements
def unique_elements(sc_list):
    newli=[]
    for i in sc_list:
        if i in newli:
            continue
        else:
            newli+=i
    return newli
#a=["a","a","f","G","g"]
lists=[]
lists=input("Enter some elements : ")
print("The original list: ",lists)
uniq=unique_elements(lists)
print("List with unique elements:")
print(uniq)
