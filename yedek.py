c2 = []
controller = 0
talep = 11

#matrisin tanımlaması
for zeroToTen in range(0,10):
    c2.append([0,0,0,0,0,0,0,0,0,0])

c2[0] = [1,1,1,1,1,1,1,0,0,0] #silinecek

def koltukGoster(): #koltukları çıktı verir.
    for zeroToTen in range(0,10):
        print(c2[zeroToTen])

talep = int(input("\nRezerve istediğiniz koltuk sayısını 10'dan büyük olmayacak şekilde giriniz.\n")) #istenilen koltuk sayısı


for doluSatir in range(0,10):
    if controller == 1:
        break
    for doluSutun in range(0,10):
        if controller == 1:
            break
        if c2[doluSatir][doluSutun] == 0:
            controller=1
            break

print(doluSatir)
print(doluSutun)

if talep <= 10-doluSutun: #satırdaki boş yer sayısı talepten fazla mı kontrol edip ona işlemi yapar
    for i in range(0,talep):
        c2[doluSatir-1][doluSutun+i]=1
else: 
    kalanKoltuk = talep-(10-doluSutun)

    for i in range(0,10-doluSutun):
        c2[doluSatir-1][doluSutun+i]=1
    
    for i in range(0,kalanKoltuk):
        c2[doluSatir][i] = 1

 













#en son çıktı
for zeroToTen in range(0,10):
    print(c2[zeroToTen])
