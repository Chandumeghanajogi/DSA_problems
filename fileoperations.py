f=open("chandu.txt","r")
print(f.read())
f.close()

with open("chandu.txt","a+") as f:
    print(f.write("welcome to italy"))

with open("chandu.txt","w") as f:
    print(f.write("chandumehsdshhfbhsehv"))