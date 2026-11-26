
print("1. member")
print("2. non member")
 
pilihan = input("masukan jenis pelanggan :")

match pilihan:
    case "1":
        print("1. member mendapatkan diskon 10%")
    case "2":
        print("2. non member mendapatkan diskon 5%")

    case _:
        print("tidak mendapat diskon") 

nominal = int(input("masukan nominal belanja : "))
if nominal >= 1000000:
    print("anda dpat diskon")
else:
    print("maaf anda tidak dapat diskon")            
   