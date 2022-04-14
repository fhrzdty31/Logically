# Ganjil atau genap chapter 2

print("\n\n== Ganjil Genap 5 Angka ==\n\n")
a = []
b = []
for i in range(5) :
    a.append(int(input('Masukkan Angka : ')))
for i in range(5):
    if (a[i] % 2) == 0 :
        b.append("Genap")
    else :
        b.append("Ganjil")

print(f"\n=> {a}\n=> {b}\n")