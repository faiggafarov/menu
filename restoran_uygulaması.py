menyu = ["CORBALAR", "BALIKLAR", "SALATALAR", "IZGARALAR", "MAKARNALAR", "ICECEKLER"]
menu = ["CORBA", "BALIK", "SALATA", "IZGARA", "MAKARNA", "ICECEK"]
masa1 = list()
m1siparis = list()
masa2 = list()
m2siparis = list()
masa3 = list()
m3siparis = list()
yenim1s = list()
yenim2s = list()
yenim3s = list()
i=0

print("----------Hoşgeldiniz----------")
while True:
    intro = int(input("1-Menü al\n2-Sipariş al\n3-Menü güncelle\n4-Çıkış Yap\n\tSeçiniz:"))
    if intro == 1:
        print(menyu)
    elif intro == 2:
        while True:
            kisi = int(input("Kaç kişiyiz?:"))
            masa1.append(kisi)
            print("Kişi sayısı:", masa1)
            for i in range(kisi):
                    istek = input("Ne istersiniz?:").upper()
                    if istek in menu:
                        m1siparis.append(istek)
                        add = input("Başka bir isteyiniz varmı?:(E/H)").upper()
                        if add == "E":
                            while True:
                                istek2 = input("Başka ne istersiniz?:").upper()
                                if istek2 in menu:
                                    m1siparis.append(istek2)
                                    break
                                else:
                                    print("Maalesef,böyle yemek restoranımızda yok")
                        else:
                            pass
                    else:
                        print("Maalesef,böyle yemek restoranımızda yok")
            print(m1siparis)
            break
        while True:
            kisi = int(input("Kaç kişiyiz?:"))
            masa2.append(kisi)
            print("Kişi sayısı:", masa2)
            for i in range(kisi):
                    istek = input("Ne istersiniz?:").upper()
                    if istek in menu:
                        m2siparis.append(istek)
                        add = input("Başka bir isteyiniz varmı?:(E/H)").upper()
                        if add == "E":
                            while True:
                                iistek2 = input("Başka ne istersiniz?:").upper()
                                if iistek2 in menu:
                                    m2siparis.append(iistek2)
                                    break
                                else:
                                    print("Maalesef,böyle yemek restoranımızda yok")
                        else:
                            pass
                    else:
                        print("Maalesef,böyle yemek restoranımızda yok")
            print(m2siparis)
            break
        while True:
            kisi = int(input("Kaç kişiyiz?:"))
            masa3.append(kisi)
            print("Kişi sayısı:", masa3)
            for i in range(kisi):
                    istek = input("Ne istersiniz?:").upper()
                    if istek in menu:
                        m3siparis.append(istek)
                        add = input("Başka bir isteyiniz varmı?:(E/H)").upper()
                        if add == "E":
                            while True:
                                iistekk = input("Başka ne istersiniz?:").upper()
                                if iistekk in menu:
                                    m3siparis.append(iistekk)
                                    break
                                else:
                                    print("Maalesef,böyle yemek restoranımızda yok")
                        else:
                            pass
                    else:
                        print("Maalesef,böyle yemek restoranımızda yok")
            print(m3siparis)
            break
    elif intro == 3:
        while True:
            update = input("Menu güncellemek istermisiniz?:(E/H)").upper()
            if update == "E":
                secim = int(input("Hangi Masa?:\n1-Masa\n2-Masa\n3-Masa\n\tSeçiniz:"))
                if secim == 1:
                        wish1 = input("Başka ne istersiniz?:").upper()
                        if wish1 in menu:
                            yenim1s.append(wish1)
                            yenim1s.update(m1siparis)
                            break
                        else:
                            print("Maalesef, böyle yemek restoranımızda yok")

                        print(yenim1s)
                if secim == 2:
                        wish2 = input("Başka ne istersiniz?:").upper()
                        if wish2 in menu:
                            yenim2s.append(wish2)
                            yenim2s.update(m2siparis)
                            break
                        else:
                            print("Maalesef, böyle yemek restoranımızda yok")
                        print(yenim2s)
                if secim == 3:
                        wish3 = input("Başka ne istersiniz?:").upper()
                        if wish3 in menu:
                            yenim3s.append(wish3)
                            yenim1s.update(m1siparis)
                            break
                        else:
                            print("Maalesef, böyle yemek restoranımızda yok")
                        print(yenim3s)

    elif intro == 4:
        print("Çıkış Yaptınız")
        break

print("\n----------Hesap Bolumu----------")
while True:
    hesap = int(input("Hangi Masa?:\n1-Masa\n2-Masa\n3-Masa\n\tSeçiniz:"))
    if hesap == 1:
        print(m1siparis)
        break
    if hesap == 2:
        print(m2siparis)
        break
    if hesap == 3:
        print(masa3)
        break




