#function to convert the string into lower case
def lower_case(string):
    lowerCase=[]
    ascii=[ord(i) for i in string]
    counter=0
    for i in string:
        if (((ascii[counter])>=97 and (ascii[counter])<=122) or ((ascii[counter])>=32 and (ascii[counter])<=64)):
            x=chr(ascii[counter])
            lowerCase.append(x)
        else:
            x=chr((ascii[counter]+32))
            lowerCase.append(x)
        counter+=1
    return lowerCase

#function to encrypt the message
def encrypt(x):
    x=lower_case(string)
    encrypted=[]
    counter=0
    print("Encrypted: ",end="")
    for i in x:
        ascii=ord(i)
        if ascii==32:
            continue
        else:
            y=chr(ascii+1)
            encrypted.append(y)
        print(encrypted[counter],end='')
        counter+=1
    return encrypted

#function to turn list into string
def ListToString(x):
    string=''.join(x)
    return string

#function to be decrypted
def decrypt(x):
    x=ListToString(y)
    counter=0
    decrypted=[]
    print("Decrypted: ",end="")
    for i in x:
        ascii=ord(i)
        l=chr(ascii-1)
        decrypted.append(l)
        print(decrypted[counter],end='')
        counter+=1
    print(' ')
    return decrypted

string=input("Enter a sentence to be encrypted \n")
x=lower_case(string)
y=encrypt(x)
print(" ")
z=ListToString(y)
w=decrypt(z)




        
