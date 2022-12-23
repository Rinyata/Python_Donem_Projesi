def matrisTanimla(c1,c2,c3,c4,koltukHaritasi):
    #matrisin tanımlaması
    for zeroToTen in range(0,10):
        c1.append([0,0,0,0,0,0,0,0,0,0])

    for zeroToTen in range(0,10):
        c2.append([0,0,0,0,0,0,0,0,0,0])

    for zeroToTen in range(0,10):
        c3.append([0,0,0,0,0,0,0,0,0,0])

    for zeroToTen in range(0,10):
        c4.append([0,0,0,0,0,0,0,0,0,0])
    
    for zeroToTen in range(0,20):
        koltukHaritasi.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        
    return(c1,c2,c3,c4,koltukHaritasi)