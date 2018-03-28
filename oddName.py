name=input("Enter the name ")
if name=="":
    print ("The name cannot be left blank")
c=0
for char in name:
    c=c+1
    if c%2==0:
        print (char)



