# Nama : Fatah Muhammad Fikrudin
# NIM : 0110121162
# Kelas : SI08

print("\n\n")
print("Fitur Belanja")
print()
a = 0
i = 0
j = 0
while a != "X":
    a = str(input("Masukkan nama produk yang akan dibeli atau X untuk selesai: "))
    if a == "X" or a == "x":
        break
    else:
        b = int(input("Masukkan harga produk: "))
    print("Berhasil menambahkan", a, "dengan harga", float(b))
    print()
    i += 1
    j += b

print()
print("Total produk yang dibeli: ", i)
if i == 0:
    print
print("Total harga produk: ", float(j))

print("\n")
anggota = str(input("Apakah anda seorang anggota? (Y/T): "))
if anggota == "Y" or anggota == "y":
    email = input("Masukkan Email: ")
    while email != "Valid":
        email = input("Email tidak Valid, ulangi: ")
    pw = input("Masukkan Password!: ")
    while pw != "valid":
        pw = input("Password tidak valid, ulangi!: ")
    level = input("Masukkan Level Kepesertaan Anda (Silver/Gold/Diamond): ")
    while level != "Silver" and level != "Gold" and level != "Diamond":
        level = input ("Masukkan tidak valid, ulangi: ")
        if level == "Silver":
            print()
            if i < 5:
                print("Selamat! anda mendapatkan potongan harga sebesar 5%")
            else:
                print("Selamat! Anda mendapatkan potongan harga sebesar 10%")
        elif level == "Gold":
            if i < 5:
                print("Selamat! Anda mendapatkan potongan harga sebesar 10%")
            else:
                print("Selamat! Anda mendapatkan potongan harga sebesar 15%")
        elif level == "Diamond":
            if i < 5:
                print("Selamat! Anda mendapatkan potongan harga sebesar 15%")
            else:
                print("Selamat! Anda mendapatkan potongan harga sebesar 20%")
else:
    print("Total harga produk: ", j)
# diskon = 
# total_harga = j - (diskon/100 * j)


                


print("Terimakasih sudah belanja di Toko Kami!")