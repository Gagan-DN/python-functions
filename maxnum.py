#2 maximum_number_finder
def find_max(num_list):
    lg_num=0
    for i in num_list:
        if i<=lg_num:
            continue
        else:
            lg_num=i
    return lg_num

u=[12,32,44,44,66,98,76,34,65]
t=find_max(u)
print("The maximum number is ",t)
