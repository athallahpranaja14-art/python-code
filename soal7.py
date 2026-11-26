print("=====MENU MAKANAN===== : ")
print("1.  ES TEH      5.000")
print("2.  ES JERUK    7.000")
print("3.  KOPI NESCAFE  10.000")
print("4.  SUSU KUCING   10.000")
print("5.  KOPI LUAK TAI MUSANG   15.000")
print("==========================")

pilihan = input("masukan bulan yang dipilih :")

match pilihan:
    case "1":
        print("1.  ES TEH    5.000")
    case "2":
        print("2.  ESJERUK   7.000")
    case "3":
        print("3.  KOPI NESCAFE    10.000")
    case "4":
        print("4.  SUSU KUCING     10.000")
    case "5":
        print("5.  KOPI LUAK TAI MUSANG   15.000")
    
    case _:
        print("MENU TIDAK ADA")    




