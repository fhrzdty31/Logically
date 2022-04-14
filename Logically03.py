# Berapa jumlahnya

print("\n\n== Penjumlahan Bilangan ==\n\n")
jumlah = 0
n = int(input('Masukkan nilai N : '))

for i in range(1, (n+1)) :
    jumlah += i
    print(i, end=", ")
print("\nJumalah = ", jumlah, "\n")