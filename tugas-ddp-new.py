# # # Nama : Fatah Muhammad Fikrudin
# # # NIM : 0110121162
# # # Kelas : SI08

def check_email(string):
    if ' ' in string:
        return False
    if "@" not in string:
        return False
    if "@" > 1:
        return False
    domain = string.split('@', 1)
    if '.' not in domain[1:]:
        return False
    return True

def check_pw(string):
    if "!" or "@" or "#" or "$" not in string:
        return False
    if len(string) <= 8:
        return False
    if 
    
# pw = input("Masukkan Password: ")
# while True:
#     if check_pw(pw):
#         print("Password Valid")
#         break
#     else:
#         pw = input("Password tidak valid, ulangi: ")
string = "geeks"
print(len(string))
# print("\n\n")
# print("Fitur Belanja")
# print()
# a = 0
# i = 0
# j = 0
# while a != "X":
#     a = str(input("Masukkan nama produk yang akan dibeli atau X untuk selesai: "))
#     if a == "X" or a == "x":
#         break
#     else:
#         b = int(input("Masukkan harga produk: "))
#     print("Berhasil menambahkan", a, "dengan harga", float(b))
#     print()
#     i += 1
#     j += b
#     setelah_diskon = j
#     print()
#     print("Total produk yang dibeli: ", i)
#     if i == 0:
#         print
#     print("Total harga produk: ", float(j))

#     print("\n")
#     anggota = str(input("Apakah anda seorang anggota? (Y/T): "))
#     if anggota == "Y" or anggota == "y":
#         email = input("Masukkan email: ")
#         while True:
#             if check_email(email):
#                 print("Email valid")
#                 break
#             else:
#                 email = input("Email tidak valid, ulangi: ")
#

#         level = input("Masukkan Level Kepesertaan Anda (Silver/Gold/Diamond): ")
#         while level != "Silver" and level != "Gold" and level != "Diamond":
#             level = input ("Masukkan tidak valid, ulangi: ")
#         else:
#             if level == "Silver":
#                 if i < 5:
#                     diskon = j * (5/100)
#                     print("Selamat! Anda mendapatkan potongan harga sebesar 5%")
#                 else:
#                     diskon = j * (10/100)
#                     print("Selamat! Anda mendapatkan potongan harga sebesar 10%")
#             elif level == "Gold":
#                 if i < 5:
#                     diskon = j * (10/100)
#                     print("Selamat! Anda mendapatkan potongan harga sebesar 10%")
#                 else:
#                     diskon = j * (15/100)
#                     print("Selamat! Anda mendapatkan potongan harga sebesar 15%")
#             elif level == "Diamond":
#                 if i < 5:
#                     diskon = j * (15/100)
#                     print("Selamat! Anda mendapatkan potongan harga sebesar 15%")
#                 else:
#                     diskon = j * (20/100)
#                     print("Selamat! Anda mendapatkan potongan harga sebesar 20%")
#             else:
#                 print("Total harga produk: ", j)
#             setelah_diskon = j - diskon 
#             print('diskonya yaitu : {}'.format(int(diskon)))
#             print("Harga setelah diskon : {}".format(int(setelah_diskon)))
# print("Terimakasih sudah belanja di Toko Kami!")


# # total = 50000
# # setelah_diskon = total
 
# # if total < 100000:
# #     diskon = total * (5/100)
# # else:
# #     diskon = total * (10/100)
 
# # setelah_diskon = total - diskon
# # print('diskonya yaitu : {}'.format(int(diskon)))
# # print('Harga setelah diskon : {}'.format(int(setelah_diskon)))


# # total_harga = j - (diskon/100 * j)

# import sys
# import msvcrt

# passwor = ''
# while True:
#     x = msvcrt.getch()
#     if x == '\r':
#         break
#     sys.stdout.write('*')
#     passwor +=x
# print('\n'+passwor)

# import msvcrt
# import getch

# def getPass():
#     passwor = ''
#     while True:
#         x = getch.getch()
#         x = msvcrt.getch().decode("utf-8")
#         if x == '\r' or x == '\n':
#             break
#         print('*', end='', flush=True)
#         passwor +=x
#     return passwor

# print("\nout=", getPass())

# import getpass
 

# p = getpass.getpass()
# if except Exception as error:
#     print('ERROR', error)
# else:
#     print('Password entered:', p)