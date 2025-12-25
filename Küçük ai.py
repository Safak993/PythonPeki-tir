#----Konusma roboti mini----#
import time
#----Listeler ----#
isim = input("\n(Sistem): İsminizi giriniz\n(Kullanıcı):->")
print("\n(Sistem): Ai başlıyor")
time.sleep(1)
if not isim.isalpha():
    print("\n(Sistem): Böyle bir isim yok")
    exit()
konusma = ["OYUN OYNUYORUM", "OYUN OYNUYOM", "OYUNDAYIM", "OYUNDAIM"]#Konuşma robotuna giden bilgilerin listeleri
konusma_2 = ["MERHABA", "MERABA", "SELAM", "SELAMIN ALEYKÜM"]
konusma_3 = ["NABER", "NASILSIN", "İYİMİSİN"]
#----Ana döngü----#
while True:
    konus = input(f"\n(Sistem): Konuş\n{isim}: ->").upper()#yazılan şeyi küçük bile olsa büyüğe çevirme
    if konus in (tuple(konusma)):
        time.sleep(1)
        print("\n(Sistem): Bende oyun severim ")
    elif konus in (tuple(konusma_2)):
        time.sleep(1)
        print("\n(Sistem): Selam🖐")
    elif konus in (tuple(konusma_3)):
        print("\n(Sistem): Ai Düşünüyor...")
        time.sleep(1)
        print("\n(Sistem): İyiyim sen nasılsın")
    else:
        print("\n(Sistem): Ai Düşünüyor...")
        time.sleep(1)
        print("\n(Sistem): Böyle bir cevabı bilmiyorum")