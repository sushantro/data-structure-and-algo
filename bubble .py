list1=[5,4,15,3,1,0]
print(list1)
for i in range(len(list1)):
    min_val=min(list1)
    min_ind=list1.index(min_val)
    list1[i],list1[min_ind]=list1[min_ind],list1[i]

print(list1)




