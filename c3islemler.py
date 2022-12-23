# bu sayfa c3 kategorisi içindir

def c3(talep, c3):
    controller = 0

    for doluSatir in range(0,10):
        if controller == 1:
            break
        for doluSutun in range(0,10):
            if controller == 1:
                break
            if c3[doluSatir][doluSutun] == 0:
                controller=1
                break
    print(doluSatir)
    print(doluSutun)
    for doluSatir in range(0,10):
        if controller == 1:
            break
        for doluSutun in range(0,10):
            if controller == 1:
                break
            if c3[doluSatir][doluSutun] == 0:
                controller=1
                break

    print(doluSatir)
    print(doluSutun)   

    if talep <= 10-doluSutun: #satırdaki boş yer sayısı talepten fazla mı kontrol edip ona işlemi yapar
        for i in range(0,talep):
            c3[doluSatir][doluSutun+i]=1
    else: 
        kalanKoltuk = talep-(10-doluSutun)

        for i in range(0,10-doluSutun):
            c3[doluSatir][doluSutun+i]=1
    
        for i in range(0,kalanKoltuk):
            c3[doluSatir+1][i] = 1

    
    return c3