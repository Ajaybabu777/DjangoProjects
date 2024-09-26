s=input("enter the string :")
subs=input("enter the sub string :")
f=False
pos=-1
n=len(s)
while True:
    pos=s.find(subs,pos+1,n) #17
    if pos==-1:
        break
    print("found at index : ",pos)
    f=True
if f==False:
    print("not found")