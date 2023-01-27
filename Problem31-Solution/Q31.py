import sys
#function that orders a list ascendingly
def ascending(list):
    for i in range(0,len(list)):
        for j in range(0,len(list)-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list

#function to check if two sorted lists are equal
def isequal(list1,list2):
    for i in range(size1):
        if list1[i] != list2[i]:
            print("Lists are equal = False\n ")
            sys.exit()
    print("Lists are equal = True\n")

size1=int(input("Enter the size of first array\n"))
size2=int(input("Enter the size of second array\n"))

#if the sizes of the arrays are not equal then the arrays are automatically not equal
if size1!=size2:
    print("Lists are equal = False\n")
    sys.exit()

list1=[int(input("Enter a number in the first list ")) for i in range(size1)]
list2=[int(input("Enter a number in the second list ")) for i in range(size2)]
list1=ascending(list1)
list2=ascending(list2)
isequal(list1,list2)

                

