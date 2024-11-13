print("~~SELAMAT DATA DI KALKULATOR BY ANGGI RODESA~~")

username = input("enter username: ")
while True:
    angkamasuk1 = int(input("enter angka1: "))
    angkamasuk2 = int(input("enter angka2: "))

    print("1. Pertambahan")
    print("2. Pengurangan")
    print("3. Pembagian")
    print("4. Perkalian")

    role = (input("Piih Role [1/2/3/4]: "))

    if role == '1':
        hasil = angkamasuk1 + angkamasuk2
        print("hasil pertambahan: ", hasil)
    elif role == '2':
        hasil = angkamasuk1 - angkamasuk2
        print("hasil pengurangan: ", hasil)
    elif role == '3':
        if angkamasuk2 == 0:
            print("maaf tidak bisa membagi dengan 0")
        else:
            hasil = angkamasuk1 / angkamasuk2
            print("hasil pembagian: ", hasil)
    elif role == '4':
        hasil = angkamasuk1 * angkamasuk2
        print("hasil perkalian: ", hasil)
    else:
        print("maaf angka tidak valid!, masukan angka yang valid")

    lanjut = input("Apakah ingin kalkulasi kembali? (y/n): ")
    if lanjut.lower() != 'y':
        print("Terima kasih telah menggunakan kalkulator!")
        break