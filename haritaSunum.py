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
