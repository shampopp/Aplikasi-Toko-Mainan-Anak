

print("\n=== Silahkan Isi Data Anda ===")
print("Nama lengkap = SHARMA YASHA PRAYUDI")
print("Nomor Absen = 28")
print("kelas = X TEL 8")
print("Hari = SENIN")
print("Guru Mata Pelajaran = APDANIEL ALAMSYAH, S.KOM")

username = "sharmayashaprayudi"
password = "smktelkomjakarta"

boneka = ['BONEKA BERUANG', 'BONEKA ANNABELLE', 'BONEKA CHARLIE']
robot = ['ROBOT GUNDAM', 'ROBOT POWER RANGER', 'ROBOT OPTIMUS PRIME']
lego = ['LEGO BATMAN', 'LEGO BARBIE', 'LEGO MARVEL']
actionfigure = ['Naruto', 'Ultraman', 'Batman']
hotwheels = ['Porsche', 'Ferrari ', 'Lamborghini']

def login():
    attemps = 0
    while attemps < 3:
        username1 = input("masukan username: ")
        password2 = input("masukan password: ")
        if username1 == username and password2 == password:
            print('login berhasil selamat datang di program ini')
            return True
        else:
            attemps += 1
            print(f"percobaan anda {attemps} dari 3\n")
if login():
    while True:
        print('\n=== Selamat Datang, Berikut adalah list TOKO MAINAN ANAK : ===')
        print('1. Mainan BONEKA')
        print("2. Mainan ROBOT")
        print("3. MAINAN LEGO")
        print("4. ACTION FIGURE")
        print("5. HOTWHEELS")
        pilihan = input('Silahkan masukan angka(1/2/3/4/5) atau ketik beli: ') .lower()

        
        if pilihan == 'beli':
            harga1 = 100000
            harga2 = 150000
            harga3 = 200000
            harga4 = 120000
            harga5 = 280000
            nama=input("Masukan Nama Pembeli :")
            kode=input("Kode Mainan :")
            if kode == '1':
                print('anda memilih boneka, harga 1 paket yaitu Rp 100000')
                jumlah_beli=(int(input("Jumlah Beli :")))
                print("================================")

                print("Nama Pembeli :", nama)
                print("Kode Mainan :", kode)

                print("Jumlah Beli :", jumlah_beli)
                print("Harga Satuan :", harga1)
                total_harga=(jumlah_beli*harga1)
                print("Total Harga :", total_harga)
                total_bayar=(int(input("Total Bayar :")))

                uang_kembali=(total_bayar-total_harga)
                print("Uang Kembalian : ", uang_kembali)
                print("================================")   
                break
            if kode == '2':
                print('anda memilih Robot, harga 1 paket yaitu Rp 150000')
                jumlah_beli=(int(input("Jumlah Beli :")))
                print("================================")

                print("Nama Pembeli :", nama)
                print("Kode Mainan :", kode)
                print("Jumlah Beli :", jumlah_beli)
                print("Harga Satuan :", harga2)
                total_harga=(jumlah_beli*harga2)
                print("Total Harga :", total_harga)
                total_bayar=(int(input("Total Bayar :")))

                uang_kembali=(total_bayar-total_harga)
                print("Uang Kembalian : ", uang_kembali)
                print("================================")   
                break
            if kode == '3':
                print('anda memilih Lego, harga 1 paket yaitu Rp 200000')
                jumlah_beli=(int(input("Jumlah Beli :")))
                print("================================")

                print("Nama Pembeli :", nama)
                print("Kode Mainan :", kode)
                print("Jumlah Beli :", jumlah_beli)
                print("Harga Satuan :", harga3)
                total_harga=(jumlah_beli*harga3)
                print("Total Harga :", total_harga)
                total_bayar=(int(input("Total Bayar :")))

                uang_kembali=(total_bayar-total_harga)
                print("Uang Kembalian : ", uang_kembali)
                print("================================")   
                break
            if kode == '4':
                print('anda memilih ACTION FIGURE, harga 1 paket yaitu Rp 120000')
                jumlah_beli=(int(input("Jumlah Beli :")))
                print("================================")

                print("Nama Pembeli :", nama)
                print("Kode Mainan :", kode)
                print("Jumlah Beli :", jumlah_beli)
                print("Harga Satuan :", harga4)
                total_harga=(jumlah_beli*harga4)
                print("Total Harga :", total_harga)
                total_bayar=(int(input("Total Bayar :")))

                uang_kembali=(total_bayar-total_harga)
                print("Uang Kembalian : ", uang_kembali)
                print("================================")   
                break
            if kode == '5':
                print('anda memilih HOTWHEELS, harga 1 paket yaitu Rp 280000')
                jumlah_beli=(int(input("Jumlah Beli :")))
                print("================================")

                print("Nama Pembeli :", nama)
                print("Kode Mainan :", kode)
                print("Jumlah Beli :", jumlah_beli)
                print("Harga Satuan :", harga5)
                total_harga=(jumlah_beli*harga5)
                print("Total Hargaa :", total_harga)
                total_bayar=(int(input("Total Bayar :")))

                uang_kembali=(total_bayar-total_harga)
                print("Uang Kembalian : ", uang_kembali)
                print("================================")   
                break

    

        elif pilihan == '1':
            print('MAINAN BONEKA')
            for i in range(len(boneka)):
                print(f"{i+1}. {boneka[i]}")
        elif pilihan == '2':
            print('MAINAN ROBOT')
            for i in range(len(robot)):
                print(f"{i+1}. {robot[i]}")
        elif pilihan == '3':
            print('MAINAN LEGO')
            for i in range(len(lego)):
                print(f"{i+1}. {lego[i]}")
        elif pilihan == '4':
            print('ACTION FIGURE')
            for i in range(len(actionfigure)):
                print(f"{i+1}. {actionfigure[i]}")
        elif pilihan == '5':
            print('HOTWHEELS')
            for i in range(len(hotwheels)):
                print(f"{i+1}. {hotwheels[i]}")
        else:
            print('pilihan anda tidak valid')
    
   


