# Nama : Fatah Muhammad Fikrudin
# NIM : 0110121162
# Kelas : SI08

def check():
	import re
	regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
	email = input("Enter email: ")
	if(re.fullmatch(regex, email)):
		return True
	else:
         print("Email tidak valid")
         return check()

def validPass():
    password = input("Masukkan password: ")
    chaeSept = ["!", "@", "#", "$"]
    if len(password) >= 8:
        if any(word.isnumeric() for word in password):
            if any(word.islower() for word in password):
                if any(word.isupper() for word in password):
                    if any(word in chaeSept for word in password):
                        return True
                    else:
                        print("Password tidak valid")
                        return validPass()
                else:
                    print("Password tidak valid")
                    return validPass()
            else:
                print("Password tidak valid")
                return validPass()
        else:
            print("Password tidak valid")
            return validPass()
    else:
        print("Password tidak valid")
        return validPass()

print()
print("Fitur Belanja")
print()
print("Selamat datang di Toko NF Electrics!! Selamat berbelanja")
i = 0
j = 0
while True:
    print()
    product = str(input("Masukkan nama produk yang akan dibeli atau X untuk menyelesaikan: "))
    while product == "":
        product = input("Tidak Valid, ulangi: ")
    if product == "X" or product == "x" and i == 0:
        print("Terimakasih sudah belanja di Toko Kami!")
        quit()
    if product == "X" or product == "x" and i != 0:
        print()
        print("Jumlah produk yang dibeli: ", i)
        print("Harga produk yang dibeli: ", j)
        print()
        break
    else:
        price = int(input("Masukkan harga produk: "))
        print("Berhasil menambahkan", product, "dengan harga", float(price))
        i += 1
        j += price
anggota = str(input("Apakah kamu anggota? (Y/T): "))
if anggota == "Y" or anggota == "y":
    check()
    while True:
        if validPass():
            level = input("Masukkan Level Keanggotaan Anda(Silver/Gold/Diamond): ")
            print()
            while level != "Silver" and level != "Gold" and level != "Diamond":
                level = input ("Enter invalid, repeat: ")
            else:
                if level == "Silver":
                    if i < 5:
                        diskon = j * (5/100)
                        print("Selamat! Anda mendapatkan potongan harga sebesar 5%")
                    else:
                        diskon = j * (10/100)
                        print("Selamat! Anda mendapatkan potongan harga sebesar 10%")
                elif level == "Gold":
                    if i < 5:
                        diskon = j * (10/100)
                        print("Selamat! Anda mendapatkan potongan harga sebesar 10%")
                    else:
                        diskon = j * (15/100)
                        print("Selamat! Anda mendapatkan potongan harga sebesar 15%")
                elif level == "Diamond":
                    if i < 5:
                        diskon = j * (15/100)
                        print("Selamat! Anda mendapatkan potongan harga sebesar 15%")
                    else:
                        diskon = j * (20/100)
                        print("Selamat! Anda mendapatkan potongan harga sebesar 20%")
                setelah_diskon = j - diskon
                print("Total Harga yang harus dibayar: ", float(setelah_diskon))
                quit()
        else:
            validPass()
    
print()
print("Terimakasih sudah belanja di Toko Kami!")
print("Sampai Jumpa!!!!")

