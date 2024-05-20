# asumsi monster di dict
monster = [
    {"ID": 1, "TYPE": "Snorlax", "ATK": 60, "DEF": 66, "HP": 43},
    {"ID": 2, "TYPE": "Pikachu", "ATK": 52, "DEF": 53, "HP": 40},
    {"ID": 3, "TYPE": "Goku", "ATK": 54, "DEF": 63, "HP": 45},
    {"ID": 4, "TYPE": "Bejita", "ATK": 46, "DEF": 47, "HP": 40},
    {"ID": 5, "TYPE": "Naruto", "ATK": 62, "DEF": 50, "HP": 29},
]


# Fungsi strip()
def mstrip(str):
    nstring = ""
    for char in str:
        if char != " ":
            nstring += char
    return nstring

# Fungsi split()
def split(str, pisah):
    hasil = []
    kata = ''
    for char in str:
        if char == pisah: 
            hasil.append(kata)
            kata = '' 
        else:
            kata += char
    hasil.append(kata)
    return hasil

# Fungsi cek Input int atau tidak
def is_integer(s):
    digits = "0123456789"
    for char in s:
        if char not in digits:
            return False
        
    return True

def id_baru(monster):
    max_id = -1
    for creature in monster:
        if creature["ID"] > max_id:
            max_id = creature["ID"]
    return max_id + 1

def cek_sama(nama, dict):
    for row in dict:
        if row["TYPE"].lower() == nama.lower():
            return False
    return True


def monster_management(): 
    print ()
    print("SELAMAT DATANG DI DATABASE PARA MONSTER !!!")
    print ()

    running = True 
    while running == True:
        print ()
        print("1. Tampilkan semua monster")
        print("2. Tambah monster baru")
        print("3. Keluar")
        print ()
        input_1 = int(input("Pilih Aksi : "))
        print ()
        if input_1 == 3:
            print("Selamat tinggal!")
            break
        elif input_1 == 1:
            categories = ["ID", "TYPE", "ATK", "DEF", "HP"]
            header = ""
            for category in categories:
                header += category + " " * (10 - len(category))
            print(header)

            print("-" * (len(header) + 5))

            for creature in monster:
                data_row = ""
                for category in categories:
                    data_row += str(creature[category]) + " " * (10 - len(str(creature[category])))
                print(data_row)
        elif input_1 == 2:
            print("Memulai pembuatan monster baru...")
            valid = False
            while valid == False:
                new_monster = input("Masukkan Type/Nama : ")
                if cek_sama(new_monster, monster) == False:
                        print("Monster sudah terdaftar di database!")
                elif new_monster == "":
                    print("Masukkan input yang valid")
                else: valid = True
            valid_2 = False
            while valid_2 == False:
                atk_power = str(input("Masukkan ATK Power : "))
                if atk_power == "":
                    print("input tidak valid, coba lagi!")
                elif is_integer(atk_power) == False:
                    print("Masukkan input bertipe Integer, coba lagi!")
                elif is_integer(atk_power) == True:
                    valid_2 = True
            valid_3 = False
            while valid_3 == False:
                def_power = str(input("Masukkan DEF Power: "))
                if def_power == "":
                    print("input tidak valid, coba lagi!")
                elif is_integer(def_power) == False:
                    print("Masukkan input bertipe Integer, coba lagi!")
                elif is_integer(def_power) == True:
                        if int(def_power) < 0 or int(def_power) > 50:
                            print("DEF Power harus bernilai 0-50, coba lagi!")
                        else:
                            valid_3 = True
            valid_4 = False
            while valid_4 == False:
                hp = str(input("Masukkan HP: "))
                if hp == "":
                    print("input tidak valid, coba lagi!")
                elif is_integer(hp) == False:
                    print("Masukkan input bertipe intger, coba lagi!")
                elif is_integer(hp) == True:
                    valid_4 = True
            print("Name/Type   | ATK Power | DEF Power | HP")
            print(new_monster + " " * (12 - len(new_monster)) + " | " + atk_power + " " * (10 - len(atk_power)) + " | " + def_power + " " * (10 - len(def_power)) + " | " + hp)
            inp2 = input("Tambahkan Monster ke Database (Y/N) : ")
            if inp2.lower() == 'y':
                new_id = id_baru(monster)
                monster.append({"ID": new_id, "TYPE": new_monster, "ATK": int(atk_power), "DEF": int(def_power), "HP": int(hp)})
                print("Monster baru telah ditambahkan!")
            elif inp2.lower() == 'n':
                print("Monster gagal ditambahkan!")