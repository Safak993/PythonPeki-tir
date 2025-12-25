import time
#----Harita Oyunu----#
#----Fonksiyon----#
isim = input("\n(Sistem): İsmini gir \n(Kullanıcı):->")
if not isim.isalpha():
    print("\n(Sistem): Böyle bir isim yok")
    print("\n(Sistem): Oyun kodları siliniyor...")
    time.sleep(1)
    print("\n(Sistem): Oyun kapatıldı")
    exit()
def harita_ciz(satir, sutun, konum):
    for i in range(satir):
        for j in range (sutun):
            if i == konum[0] and j == konum[1]: # konum 0 a satira eşitse konum çiz
                print(konum_texture, end=" ")
            else:
                print(harita_texture, end=" ")
        print()
#----Değişkenler----#
#----Textureler----#
harita_texture = "⚪"
konum_texture = "🤵"
#----Ana değişkenler----#
satir = 5
sutun = 8
konum = [satir // 2, sutun // 2]
#----Ana döngü----#
harita_ciz(satir, sutun, konum)
while True:
    hareket = input(f"\n(Sistem): W/A/S/D \n({isim}):->").upper()
    #----W/A/S/D kontrolleri----#
    if hareket == "W" and konum[0] > 0:
        konum[0] -=1
    elif hareket == "S" and konum[0] < satir - 1:
        konum[0] +=1
    elif hareket == "A" and konum[1] > 0:
        konum[1] -=1
    elif hareket == "D" and konum[1] < sutun - 1:
        konum[1] +=1
    harita_ciz(satir, sutun, konum)