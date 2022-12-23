# bu sayfa c2 kategorisi içindir

def c2(talep, c2):
    controller = 0

    for doluSatir in range(0,10):
        if controller == 1:
            break
        for doluSutun in range(0,10):
            if controller == 1:
                break
            if c2[doluSatir][doluSutun] == 0:
                controller=1
                break

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
            c2[doluSatir][doluSutun+i]=1
    else: 
        kalanKoltuk = talep-(10-doluSutun)

        for i in range(0,10-doluSutun):
            c2[doluSatir][doluSutun+i]=1
    
        for i in range(0,kalanKoltuk):
            c2[doluSatir+1][i] = 1

    
    return c2