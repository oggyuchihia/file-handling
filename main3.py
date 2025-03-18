f1=open("repeated.txt","r")
f2=open("updated.txt","w")

linesseen=set()

for line in f1.readlines():
    if line not in linesseen:
        f2.write(line)
        linesseen.add(line)

f1.close()
f2.close()