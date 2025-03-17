file=open("Codingal.txt","r")
print(file.read(8))
file.close()

#Reading 1st line

file=open("Codingal.txt","r")
print("reading the first line")
print(file.readline())
file.close()

#Reading multiple lines
file=open("Codingal.txt","r")
print("reading the multiple line")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()


#Looping through lines
file=open("Codingal.txt","r")
print("looping through lines")
for line in file:
    print(line)
file.close()

#Printing lines noth starting with particular prefixes
file1=open("Codingal.txt","r")
file2=open("Codingal updated.txt","w")


for line in file1.readlines():
    if not (line.startswith("Coding")):
        print(line)
        file2.write(line)
                 
file1.close()
file2.close()

#reading odd lines
f1=open("Codingal.txt","r")
f2=open("odd lines.txt","w")

cont=f1.readlines()
type(cont)
for i in range(1,len(cont)+1):
    if i % 2!=0:
        f2.write(cont[i-1])

    else:
        pass

f1.close()
f2.close()