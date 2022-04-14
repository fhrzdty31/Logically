# Ganjil atau genap

puts("\n\n== Ganjil Genap ==\n\n")
print("Masukkan Nilai : ")
a = gets.chomp.to_i

if a % 2 == 0
    puts("\n=> #{a} bernilai Genap\n")
else
    puts("\n=> #{a} bernilai Ganjil\n")
end