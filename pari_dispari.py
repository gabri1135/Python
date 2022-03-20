dispari = 0
for i in range(10):
    dispari += int(input(f"inserisci il {i+1} numero: ")) % 2

print("Hai inserito", 10-dispari, "numeri pari e", dispari, "dispari")
