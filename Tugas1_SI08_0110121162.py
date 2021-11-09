# Nama : Fatah Muhammad Fikrudin
# NIM : 0110121162
# Kelas : SI08

def check():
	import re
	regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
	email = input("Enter email: ")
	if(re.fullmatch(regex, email)):
		print("Valid Email")
	else:
		print("Invalid Email, Try it again.")
		return check()
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
print("Shopping Features")

i = 0
j = 0
while True:
    print()
    product = str(input("Enter the name of the product to be purchased or X to finish: "))
    if product == "X" or product == "x" and i == 0:
        quit()
    if product == "X" or product == "x" and i != 0:
        print()
        print("Total products purchased: ", i)
        print("The price of the product purchased: ", j)
        print("\n")
        break
    else:
        price = int(input("Enter product price: "))
        print("Added successfully", product, "with price", float(price))
        print()
        i += 1
        j += price
anggota = str(input("Are you a member? (Y/T): "))
if anggota == "Y" or anggota == "y":
    check()
    password = input("Enter Password: ")
    while True:
        if validPass(password):
            print("Valid Password")
            break
        else:
            password = input("Invalid Email, Try it again.")
    level = input("Enter your Membership Level (Silver/Gold/Diamond): ")
    print("\n")
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
print()
print("Terimakasih sudah belanja di Toko Kami!")