print("==========")
print("Program Kasir Sederhana")
print("Selamat Datang Di Warung Endulita")
keranjangBelanja = []
while True:
    menu_pilihan = input(' 1.Menu Makanan\n 2.Menu Minuman\n 3.Menu Snack\n Masukkan menu utama 1-3: \n')
    if menu_pilihan == "1":
        print("==========")
        print("Anda memilih nomor 1 : Menu Makanan")
        print("Pilih menu makanan anda :")
        makanan = ["Nasi Geprek", "Rujak Soto", "Nasi Tempong","Mie Goreng"]
        while True:
            for a in range(0, len(makanan)):
                print(f'{a + 1}.{makanan[a]}')
            list_makanan = int(input(f"Masukkan menu yang diinginkan? [1-{len(makanan)}] : \n"))
            if list_makanan <= len(makanan):
                keranjangBelanja.append(makanan[list_makanan-1])
                for b in range(0,len(keranjangBelanja)):
                    print(f'{b+1}.{keranjangBelanja[b]}  1x')
                break
            else:
                print("Silakan Masukkan Menu yang benar")
                continue
    elif menu_pilihan == "2":
        print("==========")
        print("Anda memilih nomor 2 : Menu Minuman")
        print("Pilih menu minuman anda :")
        minuman = ["Es Teh","Es Mojitos","Jus Buah","Kopi"]
        while True:
            for c in range(0, len(minuman)):
                print(f'{c + 1}.{minuman[c]}')
            list_minuman = int(input(f"Masukkan menu yang diinginkan? [1-{len(minuman)}] : \n"))
            if list_minuman <= len(minuman):
                keranjangBelanja.append(minuman[list_minuman-1])
                for d in range(0,len(keranjangBelanja)):
                    print(f'{d+1}.{keranjangBelanja[d]}  1x')
                break
            else:
                print("Silakan Masukkan Menu yang benar")
                continue
    elif menu_pilihan == "3":
        print("==========")
        print("Anda memilih nomor 3 : Menu Snack")
        print("Pilih menu snack anda :")
        snack = ["Kucur","Piscok","Samosa","Klepon"]
        while True:
            for e in range(0, len(snack)):
                print(f'{e + 1}.{snack[e]}')
            list_snack = int(input(f"Masukkan menu yang diinginkan? [1-{len(snack)}] : \n"))
            if list_snack <= len(snack):
                keranjangBelanja.append(snack[list_snack-1])
                for f in range(0,len(keranjangBelanja)):
                    print(f'{f+1}.{keranjangBelanja[f]}  1x')
                break
            else:
                print("Silakan Masukkan Menu yang benar")
                continue
    else:
        print("Menu tidak tersedia")
        continue

    validasi_menu = input('Ada yang ingin ditambahkan ? Y/n\n')
    if validasi_menu == "Y" or validasi_menu == "y":
        print("==========")
        continue
    else:
        print("Pesanan anda akan di antar")
        break