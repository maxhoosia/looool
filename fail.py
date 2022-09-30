a = int(input())
c =[]
q = 0
def super1 (x,y):
    g = 3*(abs(x-y))#это для супер прыжка
    return g;
    
def prosto (x,y):
    g = abs(x - y)#это для простого прыжка
    return g;
    
for i in range(a):#это определяет кол во платформ и расстояние между ними 
    b = int(input())
    c.append(b)
    
i = 0
while i != len(c):
    if i + 2 < len(c):
        if super1(c[i+2],c[i]) >= prosto(c[i+1],c[i]) + prosto(c[i+2], c[i+1]):
            q += prosto(c[i],c[i+1])
            i += 1
        else:
            q += super1(c[i+2],c[i])
            i += 2
        
    elif len(c) - i == 2:
        q += prosto(c[i], c[i+1])
        i += 1
    else:
        i+=1 
        
    
print(q)