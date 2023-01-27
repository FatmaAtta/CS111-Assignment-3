f=open("CommonWords.txt","rt")
dict={}
words=f.read()
f.seek(0)
word=words.split()
for i in word:
    dict[i]=len(i)

def getWord():
    size=int(input("Enter the number of letters\n"))
    word=[key for key,value in dict.items() if value==size]
    for i in word:
        print(i,end="          ")
    print("\n")
getWord()
