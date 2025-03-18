f1=open("Codingal.txt","r")
f2=open("repeated.txt","r")

data1=f1.read()
data2=f2.read()

data1 += "\n"
data1+=data2

f3=open("updated.txt","w")

f3.write(data1)

f1.close()
f2.close()
f3.close()

