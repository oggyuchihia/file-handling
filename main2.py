with open("Codingal.txt","r") as file:
    data=file.readlines()
    for line in data:
        word=line.split()   
        print(word)     

#Os functions
File1=open("New file.txt","x")
File1.close()

import os
if os.path.exists("My file.txt"):
    os.remove("My file.txt")
else:
    print("The file does not exist")

File2=open("My file.txt","w")
File2.write("hello how are you")
File2.close()