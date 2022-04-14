# Mana yang lebi besar

puts("\n\n== Lebih Besar Lebih Kecil ==\n\n")
print("Masukkan Nilai A : ")
a = gets.chomp.to_i
print("Masukkan Nilai B : ")
b = gets.chomp.to_i

if a > b
    puts("\n=> #{a} lebih besar dari #{b}\n")
elsif a < b
    puts("\n=> #{b} lebih besar dari #{a}\n")
else
    puts("\n=> #{a} sama dengan #{b}\n")
end