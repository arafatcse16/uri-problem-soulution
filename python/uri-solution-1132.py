x=int(input())
y=int(input())
t=x
s=0
if(x>y):
    x=y
    y=t
while(x<=y):
    if(x%13!=0):
        s+=x
    x+=1
print(s) 