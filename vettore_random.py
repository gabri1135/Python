from random import randint

#mod1
v=list()
while len(v)<5:
    while True:
        r=randint(0,9)
        if not r in v:
            break
    v.append(r)
print(v)

#mod 2
s=set()
while len(s)<5:
    s.add(randint(0,9))
print(s)
    
    
    

