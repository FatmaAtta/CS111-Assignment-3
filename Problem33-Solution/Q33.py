#function that sorts lists ascendingly
def ascending(list):
    for i in range(0,len(list)):
        for j in range(0,len(list)-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list

 #function that sorts lists descendingly   
def descending(list):
    for i in range(0,len(list)):
        for j in range(0,len(list)-1):
            if list[j]<list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list

#function that checks if list is ascending
def isascending(list1,list2):
    #ascending=True
    for i in range(len(list1)):
        if list1[i]==list2[i]:
            ascending=True
            continue
        else:
            ascending=False
        if not ascending:
            break
    return ascending
#function that checks if list is descending
def isdescending(list1,list2):
   #descending=True
   for i in range(len(list1)):
      if list1[i]==list2[i]:
            descending=True
            continue
      else:
            descending=False
      if not descending:
            break
   return descending
size=int(input("Enter the size of the array\n"))
print("Enter numbers\n")
list=[int(input()) for i in range(size)]
originalList=list.copy()


if isascending(originalList,ascending(list)):
    print("\n1\n")
elif isdescending(originalList,descending(list)):
    print("\n-1\n")
else:
    print("\n0\n")



