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
for i in range (int(a / 2)):#это меняет порядок цифр в списке
    b = c[i]
    c[i] = c[a-1-i]
    c[a-1-i] = b
for i in range (a-2):#это основная программа она не доделана ps надеюсь вспонмю что она делает
    if a < 3 :
        q = q + prosto(c[1],c[0])
    else :
        for i in range(a-2):
            if super1(c[i+2],c[i]) >= prosto(c[i+1],c[i]) + prosto(c[i+2], c[i+1]):
                q = q + prosto(c[i],c[i+1]) + prosto(c[i+2], c[i+1])
                
            else :
                q =  q + super1(c[i+2],c[i])
                i = i+1
                
print (q)