f=open("file1.txt","r")
f2=open("file2.txt","w")
#
#print(f.read())
for line in f:
    f2.write(line)
f2.close()
f2=open("file2.txt","r")
print(f2.read())
f2.close()