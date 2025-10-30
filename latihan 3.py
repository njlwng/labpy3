#latihan 3.py
print("=== Program Simulasi ATM Sederhana ===")

saldo = 1000000

while True:
    print("\nMenu:")
    print("1. Cek Saldo")
    print("2. Tarik Uang")
    print("3. Keluar")
    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        print(f"Saldo Anda sekarang: Rp {saldo}")
    elif pilihan == "2":
        tarik = int(input("Masukkan jumlah uang yang ingin ditarik: "))
        if tarik <= saldo:
            saldo -= tarik
            print(f"Anda menarik Rp {tarik}. Sisa saldo: Rp {saldo}")
        else:
            print("Saldo tidak cukup!")
    elif pilihan == "3":
        print("Terima kasih telah menggunakan ATM.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
