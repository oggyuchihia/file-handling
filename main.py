file=open('Codingal.txt')

print(file.read())

file.close()

file1=open("Codingal.txt","w")

file1.write("Hello")

file1.close()

file2=open("Codingal.txt","a")

file2.write("\nI am penguin")

file2.close()

#Counting lines of files

file3=open("Codingal1.txt","r")

Counter=0

Content=file3.read()

Colist=Content.split("\n")

for i in Colist:
    if i:
        Counter+=1

print("The toatl number of lines are")
print(Counter)

#Appending content

firstfile=input("Enter the name of first file:")
secondfile=input("Enter the name of second file:")

f1=open(firstfile,"a")
f2=open(secondfile,"r")

f1.write(f2.read())

f1.seek(0)
f2.seek(0)


