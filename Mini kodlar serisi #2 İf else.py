degisken = input("buraya sa yaz yoksa kabul etmez").upper()
if degisken == "SA":
    print("tebrikler basardin")
else:
    print("SA YAZICAKTIN!")
isim = input("isminizi giriniz (Sadece harf)")
if not isim.isalpha():#burada bir yazı varmı
    print("harfte yazı yok")
    print("Uyarıldın")
else:
     print("harfte yazı var.")
yas = input("yaşınızı giriniz (sadece sayı)")
if not yas.isdigit(): # isdigit sayı kontrolü sayı varmı yokmu
    print("Burda sayı yok")
    print("Uyarıldın")
else:
    print("sayı var tebrikler")