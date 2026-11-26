nilai = int(input("masukan nilai ujian siswa : "))
if nilai >= 75:
    print("selamat anda lulus")
else:
    print("maaf anda belum lulus") 

print("1. teori")
print("2. praktik")
 
pilihan = input("masukan nilai ujian :")

match pilihan:
    case "1":
        print("1. teori")
    case "2":
        print("2. praktik")

    case _:
        print("kategori ujian tidak valid")    
   
