print("=====NAMA NAMA BULAN===== : ")
print("1.  JANUARI")
print("2.  FEBRUAR")
print("3.  MARET")
print("4.  APRIL")
print("5.  JUNI")
print("6.  MEI")
print("==========================")

pilihan = input("masukan bulan yang dipilih :")

match pilihan:
    case "1":
        print("1.  JANUARI")
    case "2":
        print("2.  FEBRUARI")
    case "3":
        print("3.  MARET")
    case "4":
        print("4.  APRIL")
    case "5":
        print("5.  JUNI")
    case "6":
        print("6.  MEI")
    
    case _:
        print("bulan tidak ada")    




