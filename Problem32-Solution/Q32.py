import sys
size=int(input("Enter the size of the array\n"))
list1=[int(input("Enter a number in the first list ")) for i in range(size)]
list2=[int(input("Enter a number in the second list ")) for i in range(size)]
list1.sort()
list2.sort()
equal=True 
for i in range(size):
    if list1[i] != list2[i]:
            print("The two lists are not equal\n ")
            sys.exit()
print("The two lists are equal!\n")
