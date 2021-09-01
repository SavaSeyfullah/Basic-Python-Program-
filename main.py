
bakiye = 2000

secim = input("Kartı Takmak için S tuşuna, Çıkarmak için K tuşuna basınız: ")


if secim == 'S':
    while True:
        islem = int(input("""
                  Hoşgeldiniz
                  Bakiyeniz:{}
                  Yapmak İstediğiniz İşlemi Seçiniz:
                  1 - Para Çekmek
                  2 - Para Yatırma
                  3 - Kart Bilgileri
                  4 - Kart İade

                  Lütfen Yapmak İstediğiniz İşlemi Belirtiniz: """.format(bakiye)))
        if islem == 1:
            cekme = int(input("Çekmek istediğiniz miktarı giriniz: "))
            if cekme > bakiye:
                print("Bakiyenizde yeterli miktar bulunmamaktadır")
            else:
                bakiye -= cekme
                print("Güncel Bakiyeniz {}TL'dir.".format(bakiye))

        if islem == 2:
            cekme = int(input("Yatırmak istediğiniz miktarı giriniz: "))
            bakiye += cekme
            print("Güncel Bakiyeniz {}TL'dir.".format(bakiye))

        if islem == 3:
            print("""
                 Kart Bilgileri
                 --------------------
                 Ad Soyad: Monkey D. Luffy
                 Kart Numarası: 45589659869545
                 Güncel Bakiye: {}""".format(bakiye))

        if islem == 4:
            print("Güle Güle")
            break

elif secim == 'K':
     print("Güle Güle")


print()
