# Apakah Semua Berbeda

print("\n\n== Mencari Nilai yang Sama ==\n\n")
a = []
for i in range(5) :
    a.append(int(input('Masukkan Angka : ')))
for i in range(5):
        for j in range(i+1, 5):
            if a[i] == a[j] :
                print("\n=> Ada\n")
                exit()
print("\n=> Tidak Ada\n")