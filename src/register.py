def register(user, item_inventory, monster_inventory):
    # PROGRAM register

    # SPESIFIKASI:
    # program menerima array user (yang berisi data user.csv dalam bentuk matrix)
    # Program menerima input user berupa username dan password. 
    # Username dikatakan valid jika berisi sekumpulan character alfabet, angka, underscore dan strip. 
    # Selanjutnya akan dilakukan proses validasi username. 
    # Jika username tidak valid akan ditampilkan pesan "Username hanya boleh berisi alfabet, angka, underscore, dan strip!". 
    # Jika username sudah digunakan sebelumnya, akan ditmapilkan pesan f"Username {uname} sudah terpakai, silakan gunakan username lain!"
    # Jika benar, user dipersilahkan untuk memilih monster awal.
    # Lalu, data id, username, password, role, oc akan tersimpan dalam bentuk array ke matrix user.
    # nilai default:
        # id : jumlah user + 1
        # role : agent
        # oc : 0

    # KAMUS
    # KAMUS FUNGSI DAN PROSEDUR
    def validasiUName (uname):
        # SPESIFIKASI
        # fungsi menerima input uname (username). Fungsi mengecek apakah uname merupakan username yang valid. Jika iya, fungsi memberikan boolean True. Jika tidak, fungsi memberikan boolean False.

        # KAMUS LOKAL
        # res: bool (menunjukkan apakah uname valid atau tidak)
        # x : integer (menunjukkan nilai ascii code dari _)

        # ALGORITMA
        res = True # Inisiasi bool res
        for _ in uname: # looping pada setiap character pada string uname
            x = ord(_) # inisiasi integer x
            if not(x == 45 or x == 95 or 48 <= x <= 57 or 97 <= x <= 122 or 65 <= x <= 90): # pengecekan, jika char _ tidak memenuhi syarat character username yang valid, maka res akan bernilai "false" dan looping dihentikan
                res = False
                break
        return res # Fungsi memberi output boolean res

    def isIn (x, A):
        # SPESIFIKASI
        # fungsi menerima input x (tipe data bebas) dan array A (tipe data bebas), lalu funsgi akan mengecek apakah x ada di dalam array A. Jika iya, fungsi akan memberi output boolean True. Jika tidak, fungsi akan memberi output boolean False

        # KAMUS LOKAL 
        # res : bool (menyimpan boolean yg menyatakan apakah x ada di dalam array A)

        res = False # inisiasi variabel res
        for _ in A: # looping pada setiap anggota array A
            if _ == x: # pengecekan, jika _ == x, maka variabel res menjadi True, dan looping dihentikan
                res = True
                break
        return res # fungsi memberi output res
    
    # KAMUS VARIABEL
    # uname : string (berisi username yang diinputkan user)
    # pwd : string (berisi password yang diinputkan user)
    # validUname : bool (berisi boolean yg menyatakan apakan username valid atau tidak)
    # dataUname : Array of string (berisi nama username yang telah tersimpan)
    # numMos : integer (menyimpan input user yang merepresentasikan monster awal yang dipilih)
    # Mos : string (menyimpan nama monster yang sesuai dengan id (numMos) yang diinputkan sebelumnya)
    # id : integer (menyimpan nilai id dari username yang didaftarkan)


    # ALGORITMA
    uname = input("Masukkan username: ") # input username
    pwd = input("Masukkan password: ") # input password

    monster_id = -1

    validUname = validasiUName(uname) # memvalidasi username

    if validUname: # pengecekan pertama: jika username tidak valid, user diminta registerasi ulang
        # menghimpun nama username yang telah dibuat
        dataUname = [user[i][1] for i in range (1, len(user))] # inisiasi array dataUname
        if isIn(uname, dataUname): # pengecekan, menggunakan fungsi isIn(). Jika username yg akan didaftarkan sudah terdaftar sebelumnya (uname ada dalam array dataUname), maka user akan diminta registerasi ulang.
            print(f"Username {uname} sudah terpakai, silakan gunakan username lain!")
            register(user, item_inventory, monster_inventory)
        else: # jika username yang akan didaftarkan belum terdaftar sebelumnya, maka user dipersilakan memilih monster awal
            # Memilih monster awal
            print("Silakan pilih salah satu monster sebagai monster awalmu.")
            print("1. Charizard")
            print("2. Bulbasaur")
            print("3. Aspal")
            numMos = int(input("Monster pilihanmu : ")) # Inisiasi dan input variabel numMos 
            Mos = "" # inisiasi string Mos. Selanjutnya akan diisi dengan nama yang sesuai dengan numMos
            if numMos == 1:
                Mos = "Charizard"
                monster_id = 3
            elif numMos == 2:
                Mos = "Bulbasaur"
                monster_id = 5
            elif numMos == 3:
                Mos = "Aspal"
                monster_id = 17
            while numMos != 1 and numMos != 2 and numMos != 3 :
                print ("Monster tidak tersedia dalam pilihan.")
                print("Silakan pilih salah satu monster sebagai monster awalmu.")
                print("1. Charizard")
                print("2. Bulbasaur")
                print("3. Aspal")
                numMos = int(input("Monster pilihanmu : ")) # Inisiasi dan input variabel numMos 
                if numMos == 1:
                    Mos = "Charizard"
                    monster_id = 3
                elif numMos == 2:
                    Mos = "Bulbasaur"
                    monster_id = 5
                elif numMos == 3:
                    Mos = "Aspal"
                    monster_id = 17
            # ditampilkan pesan selamat datang
            print(f"Selamat datang Agent {uname}. Mari kita mengalahkan Dr. Asep Spakbor dengan {Mos}!")
            # proses menyimpan data yang sudah diinputkan ke matrix user
            user.append([str(len(dataUname) + 1), uname, pwd, "agent", "0"])
            item_inventory.append([str(len(dataUname) + 1), 'Strength Potion', '0'])
            item_inventory.append([str(len(dataUname) + 1), 'Resilience Potion', '0'])
            item_inventory.append([str(len(dataUname) + 1), 'Healing Potion', '0'])
            monster_inventory.append([str(len(dataUname) + 1), str(monster_id), '1'])
    else: # jika username tidak valid, user diminta registerasi ulang
        print("Username hanya boleh berisi alfabet, angka, underscore, dan strip!")
        register(user, item_inventory, monster_inventory)
