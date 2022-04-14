# Mungkinkah

print("\n\n== Mungkin atau Tidak ==\n")
print("x + y = 10\n")
a = []
for i in range(5) :
    a.append(int(input('Masukkan Angka : ')))
for i in range(5):
        for j in range(5):
            if a[i] + a[j] == 10:
                print("\n=> Bisa\n")
                exit()
print("\n=> Tidak Bisa\n")