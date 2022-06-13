from Admin import admin
from Pemilik_toko_buah import pemilik_toko_buah
import getpass

while True:
    print("\n------------------")
    print("ketik keluar di kedua pilihan untuk keluar dari sistem.")
    id = input("Masukkan ID anda: ")
    pw = getpass.getpass(prompt="Masukkan sandi anda: ")
    x = admin(id, pw)
    i = x.login()
    if i == "admin":
        while True:
            print("\n------------------")
            print("Selamat Datang Admin!")
            print("1. Memasukkan data\n2. Lihat data\n3. Update data\n4. Delete data\n5. keluar")
            print("------------------\n")
            pilihan = input("Masukkan pilihan: ")
            if pilihan == "1":
                data = input("Masukkan nama data: ")
                jumlah = input("Masukkan jumlah: ")
                x = admin(id, pw, data, jumlah)
                x._create()
            elif pilihan == "2":
                x = admin()
                x.read()
            elif pilihan == "3":
                data = input("Masukkan nama data: ")
                jumlah = input("Masukkan jumlah: ")
                x = admin(id, pw, data, jumlah)
                x._update()
            elif pilihan == "4":
                data = input("Masukkan nama data: ")
                x = admin(id, pw, data)
                x._delete()
            elif pilihan == "5":
                break
            else:
                print("Anda memasukkan pilihan yang salah!")

    elif i == "pemilik":
        while True:
            print("\n------------------")
            print("Selamat Datang Pemilik Toko!")
            print("1. Lihat data\n2. Keluar")
            print("------------------\n")
            pilihan = input("Masukkan pilihan: ")
            if pilihan == "1":
                x = pemilik_toko_buah()
                x.baca()
            elif pilihan == "2":
                break
            else:
                print("Anda memasukkan pilihan yang salah!")
    else:
        if id and pw == "keluar":
            break
        else:
            print(i)
            continue
