# Nama : Fatah Muhammad Fikrudin
# NIM : 0110121162
# Kelas : SI08

def check_email(string):
    if ' ' in string:
        if "@" not in string:
            domain = string.split('@', 1)
            if '.' not in domain[1:]:
                return False
    return True
def validPass(password):
    chaeSept = ["!", "@", "#", "$"]
    if len(password) >= 8:
        if any(word.isnumeric() for word in password):
            if any(word.islower() for word in password):
                if any(word.isupper() for word in password):
                    if any(word in chaeSept for word in password):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
print("\n")
print("Fitur Belanja")
a = 0
i = 0
j = 0
while a != "X":
    print()
    a = str(input("Masukkan nama produk yang akan dibeli atau X untuk selesai: "))
    if a == "X" or a == "x" and i == 0:
        break
    if a == "X" or a == "x" and i != 0:
        print()
        print("Total produk yang dibeli: ", i)
        print("Harga produk yang dibeli: ", j)
        print("\n")
        break
    else:
        b = int(input("Masukkan harga produk: "))
        print("Berhasil menambahkan", a, "dengan harga", float(b))
        print()
        i += 1
        j += b
anggota = str(input("Apakah anda seorang anggota? (Y/T): "))
if anggota == "Y" or anggota == "y":
    email = input("Masukkan email: ")
    while True:
        if check_email(email):
            print("Email valid")
            break
        else:
            email = input("Email tidak valid, ulangi: ")
    password = input("Masukkan Password: ")
    while True:
        if validPass(password):
            print("Password Valid")
            break
        else:
            password = input("Password tidak valid, ulangi: ")
    level = input("Masukkan Level Kepesertaan Anda (Silver/Gold/Diamond): ")
    print("\n")
    while level != "Silver" and level != "Gold" and level != "Diamond":
        level = input ("Masukkan tidak valid, ulangi: ")
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
print()
print("Terimakasih sudah belanja di Toko Kami!")