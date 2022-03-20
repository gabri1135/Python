n=int(input("Inserire un numero: "))
maxd=int(input("Inserire il numero fino a cui vuoi sapere i divisori: "))

print("I divisori sono:")
for i in range(1,maxd+1):
    if n%i==0: print(i, end=' ')
