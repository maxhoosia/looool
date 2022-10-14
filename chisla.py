a = int(input())
c=[]
d=[]
q =2


while a != 1:
    b = a/q
    if (a % q ) == 0 :
        c.append(q)
        q= 2
        a = b
    else :
        q = q+1
for i in range (len(c)):
    if c[i] >=10:
        n = 0
    else :
        n = 1
d.append(c[0])
c.pop(0)
if n == 0 :
    print (-1)
else:
    for j in range (len(c)):
        g= len(c)
        for i in range (len(c)):
            if i == len(c)-1:
                d.append(c[i])
            else :
                v =c[i]*c[i+1]
                if v <= 9:
                    d.append(v)
                    c[i+1]=1
                else :
                    d.append(c[0])
            
print (c,d)