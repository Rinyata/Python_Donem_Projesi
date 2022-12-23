import c1islemler,c2islemler,c3islemler,c4islemler
import matrisTanimlamalari, haritaSunum


#genel tanımlamalar:

c1,c2,c3,c4,koltukHaritasi = [],[],[],[],[] #c'ler kategorilerin kendi matrisleri, koltuk haritası ise 4ünün birleşiminden oluşan asıl matrisimiz.

(c1,c2,c3,c4,koltukHaritasi) = matrisTanimlamalari.matrisTanimla(c1,c2,c3,c4,koltukHaritasi)# boş matrislerimizi tanımlıyoruz


#kategori seçimi ve işlem yaptırma
def kategoriSecIslemYaptir(kategoriSecimi,c1,c2,c3,c4,talep):

    if kategoriSecimi == 1:
        c1 = c1islemler.c1(talep,c1)
    elif kategoriSecimi == 2:
        c2 = c2islemler.c2(talep,c2)
    elif kategoriSecimi == 3:
        c3 = c3islemler.c3(talep,c3)
    elif kategoriSecimi == 4:
        c4 = c4islemler.c4(talep,c4)

def reservation():

    talep = int(input("\nRezerve istediğiniz koltuk sayısını 10'dan büyük olmayacak şekilde giriniz.\n")) #istenilen koltuk sayısını input alma

    kategorisecimi = int(input("Lütfen 4 kategoriden birini seçiniz.\n"))#kategori seçimi ve işlem yaptırma
    kategoriSecIslemYaptir(kategorisecimi,c1,c2,c3,c4,talep)



    for temp1 in range(0,10): #c1in ana haritaya yerleştirilmesi
        for temp2 in range(0,10):
            koltukHaritasi[temp1][temp2+5] = c1[temp1][temp2]

    for temp1 in range(0,10): #c3ün ana haritaya yerleştirilmesi
        for temp2 in range(0,10):
            koltukHaritasi[temp1+10][temp2+5] = c3[temp1][temp2]

    for temp1 in range(0,10): #c2nin sağ kısmının ana haritaya yerleştirilmesi
        for temp2 in range(0,5):
            koltukHaritasi[temp1][temp2+15] = c2[temp1][temp2+5]

    for temp1 in range(0,10): #c2nin sol kısmının ana haritaya yerleştirilmesi
        for temp2 in range(4,-1,-1):
            koltukHaritasi[temp1][temp2] = c2[temp1][4-temp2]

    for temp1 in range(0,10): #c4nin sağ kısmının ana haritaya yerleştirilmesi
        for temp2 in range(0,5):
            koltukHaritasi[temp1+10][temp2+15] = c4[temp1][temp2+5]

    for temp1 in range(0,10): #c4nin sol kısmının ana haritaya yerleştirilmesi
        for temp2 in range(4,-1,-1):
            koltukHaritasi[temp1+10][temp2] = c4[temp1][4-temp2]


#Koltukların tamamını bozmadan çıktı vermemiz için oluşturduğumuz fonksiyonumuz:
def KoltukHaritasiSunumu(koltukharitasi):  

    gosterimlikHarita = koltukharitasi #orijinali değiştirmemek adına...

    #Koltukların tamamını çıktı vereceğimizde kategorilerimiz ayrı gözüksün diye bu eklentileri yapıyoruz.
    for zeroToTen in range(0,20):
        for zeroToTen2 in range(0,20):
            if zeroToTen2 == 5:
                gosterimlikHarita[zeroToTen].insert(zeroToTen2,"|")
            elif zeroToTen2 == 16:
                gosterimlikHarita[zeroToTen].insert(zeroToTen2,"|")

    for zeroToTen in range(0,20):
        if zeroToTen == 10:
            print("----------------------------------------------------------------------")
        print(gosterimlikHarita[zeroToTen])

#Yukarıdaki çıktı verme fonksiyonumuzu çalıştıralım:
def printSaloon():
    haritaSunum.KoltukHaritasiSunumu(koltukHaritasi)





status = 4

while(status != 0):
    print("\n")
    print("****************")
    print("**  ANA MENÜ  **")
    print("****************")
    print("1. Rezervasyon")
    print("2. Salonu Yazdır")
    print("3. Yeni Etkinlik")
    print("0. Çıkış")
    print("****************")
    print("\n")

    choice = int(input("Seçiminiz? "))
    print("\n")


    if choice == 0:
        status = 0
    elif choice ==1:
        reservation()
    elif choice ==2:
        printSaloon()
    elif choice ==3:
        c1,c2,c3,c4,koltukHaritasi = [],[],[],[],[]
        (c1,c2,c3,c4,koltukHaritasi) = matrisTanimlamalari.matrisTanimla(c1,c2,c3,c4,koltukHaritasi)#matrisleri sıfırlarız

