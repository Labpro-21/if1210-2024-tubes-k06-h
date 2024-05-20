import os
import argparse

def load():
    # PROGRAM load

    # SPESIFIKASI
    # Program menerima input nama folder yang akan di load menggunakan argparse
    # path folder yang diinputkan disimpan dalam variabel folder_name
    # Jika folder_name tidak memiliki nilai, akan diprint pesan:
        # "Tidak ada nama folder yang diberikan!"
        # "Usage: python main.py <nama_folder>"
        # lalu program berhenti
    # Jika folder_name ada nilainya, namun tidak dapat ditemukan, akan diprint pesan: 
        # "Folder '{folder_name}' tidak ditemukan."
        # Lalu program berhenti
    # Jika folder_name ada nilainya dan dapat ditemukan folder dengan path tersebut, maka:
        # akan diprint "Loading..."
        # dibuat dictionary "dict" yang akan menyimpan seluruh data yang diload
        # seluruh data .csv akan diconvert ke matrix dan disimpan dalan dictionary "dict"
        # akan diprint "Selamat datang di program OWCA!"
        # return dict

    # KAMUS
    # KAMUS FUNGSI DAN PROSEDUR
    def parse(file):
        # SPESIFIKASI
        # fungsi menerima input string "file" yang akan diubah menjadi matrix dengan ketentuan:
            # submatrix dipisahkan dengan enter ("\n")
            # anggota submatrix dipisahkan dengan titik koma (";")

        # KAMUS LOKAL
        # matrix : matrix of string (menyimpan matrix hasil parse(file))
        # array : matrix of string (submatrix sementara yang menyimpan elemen pada satu baris)
        # data : string (anggota submatrix)

        # ALGORITMA
        matrix = [] # inisiasi variabel matrix
        for line in file: # looping untuk setiap baris (line) pada file
            if line == "99999":
                pass
            else:
                array = [] # inisiasi variabel array
                data = "" # inisiasi variabel data
                for _ in line: # looping untuk setiap character pada baris (line)
                    if _ != ";": # pengecekan, jika _ != ";" maka _ akan ditambahkan pada string data
                        data += _
                    else: # pengecekan, jika _== ";", string data akan ditambahkan pada array, dan nilai string data direset
                        array.append(data)
                        data = ""
                data = data[:-1]
                array.append(data) # data paling akhir belum di-append ke array karena di akhir baris tidak ada ";", maka ditambahkan manual setelah looping berakhir
                matrix.append(array) # array ditambahkan pada matrix
        return matrix # fungsi menghasilkan matrix
    
    # KAMUS VARIABEL
    # dict : dictionary (menyimpan seluruh data yang diload dan informasi tambahan)

    dict = {} # inisiasi dict

    # serangkaian kode untuk mengambil input nama folder yang dituliskan di terminal. nama folder disimpan dalam variabel folder_name
    parser = argparse.ArgumentParser(description="Load data from external files.")
    parser.add_argument("folder_name", type=str, nargs="?", help="Nama folder yang berisi file penyimpanan.")
    args = parser.parse_args()
    folder_name = args.folder_name
    
    if folder_name is None: # pengecekan, jika folder_name tidak memiliki nilai, maka akan diprint pesan peringatan, lalu program berhenti. Fungsi tidak memberi output (output None)
        print("Tidak ada nama folder yang diberikan!")
        print("Usage: python main.py <nama_folder>")
        return None
    elif not os.path.exists(folder_name): # pengecekan, jika folder_name ada nilainya, namun tidak ada di penyimpanan, maka akan diprint pesan peringatan, lalu program berhenti. Fungsi tidak memberi output (output None)
        print(f"Folder '{folder_name}' tidak ditemukan.")
        return None
    else: # pengecekan, jika folder_name memiliki nilai dan terdapat di penyimpanan, maka:
        print("Loading...") # diprint "Loading..."
        dict['folder_name'] = folder_name # variabel folder_name dicopy ke dict['folder_name'] sebagai informasi tambahan
        # file user.csv diubah ke matrix dan disimpan dalam dict['user']
        with open(os.path.join(folder_name, "user.csv"), "r") as file:
            dict['user'] = parse(file)
        # file monster.csv diubah ke matrix dan disimpan dalam dict['monster']
        with open(os.path.join(folder_name, "monster.csv"), "r") as file:
            dict['monster'] = parse(file)
        # file item_inventory.csv diubah ke matrix dan disimpan dalam dict['item_inventory']
        with open(os.path.join(folder_name, "item_inventory.csv"), "r") as file:
            dict['item_inventory'] = parse(file)
        # file monster_inventory.csv diubah ke matrix dan disimpan dalam dict['monster_inventory']
        with open(os.path.join(folder_name, "monster_inventory.csv"), "r") as file:
            dict['monster_inventory'] = parse(file)
        # file monster_shop.csv diubah ke matrix dan disimpan dalam dict['monster_shop']
        with open(os.path.join(folder_name, "monster_shop.csv"), "r") as file:
            dict['monster_shop'] = parse(file)
        # file item_shop.csv diubah ke matrix dan disimpan dalam dict['item_shop']
        with open(os.path.join(folder_name, "item_shop.csv"), "r") as file:
            dict['item_shop'] = parse(file)
                
        print("Selamat datang di program OWCA!")
        return dict # fungsi menghasilkan dict