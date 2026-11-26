print("===Selamat datang di Bioskop galaxy===")

umur = int(input("Masukkan umur anda: "))
if umur >= 17:
        print("Silahkan pilih genre film anda: ")
        print("1. Horror")
        print("2. Action")
        print("3. Comedy")
        print("4. Family")
        print("5. Romance")
        genre = int(input("Masukkan pilihan genre film anda (1-5): "))
        match genre:
            case 1:
                print("Anda memilih genre Horror")
                print("Anda ingin horor lokal atau luar negeri?")
                print("1. Horror lokal")
                print("2. Horror luar negeri")
                horror = int(input("Masukkan pilihan anda (1-2): "))
                match horror:
                    case 1:
                        print("Anda memilih horror lokal")
                        print("1. Pengabdi Setan")
                        print("2. Bayi Ireng")
                        
                        lokal = int(input("Film apa yang akan anda tonton (1/2) : "))
                        match lokal:
                            case 1:
                                print("Anda memilih Pengabdi Setan")
                                print("Selamat menonton")
                            case 2:
                                print("anda memilih Bayi Ireng")
                                print("selamat menyaksikan")
                    case 2:
                        print("Anda memilih horror luar negeri")
                        print("1. Smile")
                        print("2. IT")
                        
                        lokal = int(input("Film apa yang akan anda tonton (1/2) : "))
                        match lokal:
                            case 1:
                                print("Anda memilih Smile")
                                print("Selamat menonton")
                            case 2:
                                print("anda memilih IT")
                                print("selamat menyaksikan")               
            case 2:
                print("Anda memilih genre Action")
                print("Anda ingin Lokal atau Luar Negri?")
                print("1. lokal")
                print("2. luar")
                lokal = int(input("Masukkan pilihan anda (1-2): "))
                match lokal:
                    case 1:
                        print("Anda memilih Action Lokal")
                        print("1. kemenraider")
                        print("2. Satria Batang Hitam")
                        
                        
                    case 2:
                        print("Anda memilih Action Luar Negri")
                        print("1. Avengers : Doomsday")
                        print("2. The Dark Knight")
                        
                        luar = int(input("Film apa yang akan anda tonton (1/2) : "))
                        match luar:
                            case 1:
                                print("Anda memilih film Avengers : Doomsday")
                                print("Selamat menonton")
                            case 2:
                                print("anda memilih The Dark Knight")
                                print("selamat menyaksikan")
            case 3:
                print("Anda memilih genre Comedy")
                print("Anda ingin menonton film komedi lokal atau luar negeri?")
                print("1. Komedi lokal")
                print("2. Komedi luar negeri")
                komedi = int(input("Masukkan pilihan anda (1-2): "))
                match komedi:
                    case 1:
                        print("Anda memilih komedi lokal")
                        print("1. Agak Laen")
                        print("2. Rusdi Dan Kawan Kawan")
                        lokal = int(input("Film apa yang akan anda tonton (1/2) : "))
                        match lokal:
                            case 1:
                                print("Anda memilih film Agak Laen")
                                print("Selamat menonton")
                            case 2:
                                print("anda memilih Rusi Dan Kawan Kawan")
                                print("selamat menyaksikan")
                    case 2:
                        print("Anda memilih komedi luar negeri")
                        print("1. arisan")
                        print("2. Dead Poets Society")
                        lokal = int(input("Film apa yang akan anda tonton (1/2) : "))
                        match lokal:
                            case 1:
                                print("Anda memilih film arisan")
                                print("Selamat menonton")
                            case 2:
                                print("anda memilih Dead Poets Society")
                                print("selamat menyaksikan")
            case 4:
                print("Anda memilih genre Family")
                print("Anda ingin menonton film keluarga lokal atau luar negeri?")
                print("1. Film keluarga lokal")
                print("2. Film keluarga luar negeri")
                keluarga = int(input("Masukkan pilihan anda (1-2): "))
                match keluarga:
                    case 1:
                        print("Anda memilih film keluarga lokal")
                        print("1. Keluarga gila")
                        print("2. upin ipin")
                        lokal = int(input("Film apa yang akan anda tonton (1/2) : "))
                        match lokal:
                            case 1:
                                print("Anda memilih film Keluarga gila")
                                print("Selamat menonton")
                            case 2:
                                print("anda memilih upin ipin")
                                print("selamat menyaksikan")
                    case 2:
                        print("Anda memilih film keluarga luar negeri")
                        print("1. si entong")
                        print("2. Home Alone")
                        lokal = int(input("Film apa yang akan anda tonton (1/2) : "))
                        match lokal:
                            case 1:
                                print("Anda memilih film si entong")
                                print("Selamat menonton")
                            case 2:
                                print("anda memilih Home Alone")
                                print("selamat menyaksikan")
            case 5:
                print("Anda memilih genre Family")
                print("Anda ingin menonton film keluarga lokal atau luar negeri?")
                print("1. Film keluarga lokal")
                print("2. Film keluarga luar negeri")
                keluarga = int(input("Masukkan pilihan anda (1-2): "))
                match keluarga:
                    case 1:
                        print("Anda memilih film keluarga lokal")
                        print("1. Keluarga Cemara")
                        print("2. Laskar Pelangi")
                        lokal = int(input("Film apa yang akan anda tonton (1/2) : "))
                        match lokal:
                          case 1:
                            print("Anda memilih film Keluarga Cemara")
                            print("Selamat menonton")
                          case 2:
                              print("Anda memilih film Jatuh Cinta Seperti Di Film-Film")
                              print("Selamat menyaksikan")
                    case 2:
                        print("Anda memilih Romance Luar Negri")
                        print("1. Drawing Closer")
                        print("2. The Notebook")
                        luar = int(input("Film apa yang akan anda tonton (1/2) : "))
                        match luar:
                            case 1:
                                print("Anda memilih film Drawing Closer")
                                print("Selamat mnyaksikan")
                            case 2:
                                print("Anda memilih film The Notebook")
                                print("Selamat menyaksikan")
else:
    print("Pilih genre film anda")
    print("1. Film Animasi 2D")
    print("2. Film Animasi 3D")
    genre = int(input("Masukan genre film anda(1/2) : "))
    match genre:
        case 1:
            print("Anda memilih film 2D")
            print("1. Naruto")
            print("2. One Piece")
            animasi = int(input("Film apa yang akan anda tonton (1/2) : "))
            match animasi:
                case 1:
                    print("Anda memilih animasi Naruto")
                    print("Selamat menonton")
                case 2:
                    print("Anda memilih animasi One Piece")
                    print("Selamat menyaksikan")
        case 2:
            print("Anda memili film 3D")
            print("1. Nemo")
            print("2. Kunfu Panda")
            animasi = int(input("Film apa yang akan anda tonton (1/2) : "))
            match animasi:
                case 1:
                    print("Anda memilih animasi Nemo")
                    print("Selamat menonton")
                case 2:
                    print("Anda memilih animasi Kungfu panda")
                    print("Selamat menyaksikan")
