import os

def save(data):
    # PROGRAM save

    # SPESIFIKASI
    # menerima input data (berupa dictionary yang menyimpan seluruh data yang digunakan)
    # menerima input user berupa nama folder yang akan digunakan untuk menyimpan data
    # fungsi melakukan pengecekan keberadaan folder data dan folder yang diinputkan. Jika belu ada, akan dibuat terlebih dahulu 
    # lalu, seluruh data akan disimpan dalam file.csv masing-masing
    # ditampilkan pesan: f"Berhasil menyimpan data di folder {folder_path}!"

    # KAMUS
    # KAMUS FUNGSI DAN PROSEDUR
    def save_csv(folder_path, type_csv, data):
        # SPESIFIKASI
        # prosedur menerima input:
            # folder_path (menyatakan path folder yang dituju)
            # type_csv (menyatakan nama file csv yang akan disimpan)
            # data (matrix yang berisi data yang akan diubah ke csv format)
        # I.S. file type_csv dalam  folder folder_path belum menyimpan data terkini
        # I.S. file type_csv dalam  folder folder_path sudah menyimpan data terkini

        # KAMUS LOKAL
        # file_path : string (menyimpan path untuk file yang akan disimpan)
        # line : string (menyimpan satu baris yang akan dituliskan ke file.csv)
        # len_data : integer (menyimpan panjang matrix data)
        # len_row : integer (menyimpan panjang array data[j])

        # ALGORITMA
        file_path = os.path.join(folder_path, type_csv) # inisiasi variabel file_path
        with open(file_path, "w") as file: # membuka/membuat file dengan path yang ditentukan sbelumnya (dalam mode "w" atau tulis)
            len_data = len(data) # inisiasi variabel len_data
            for j in range(len_data): # looping pada setiap anggota matrix data (submatrix)
                line = "" # inisiasi variabel line
                len_row = len(data[j]) # inisiasi variabel len_row
                for i in range(len_row): # looping untuk setiap i dalam range(len_row)
                    line += str(data[j][i]) # string line dikonkatenasi dengan string data[row][i]
                    if i != len_row - 1: # pengecekan, jika i += len_row - 1, maka line akan dikonkatenasi dengan ";"
                        line += ";"
                if j == len_data - 1: # pengecekan, jika j == len_data - 1, maka string line akan dikonkatenasi dengan "\n", agar pada baris terakhir dibuat baris baru yang kosong
                    line += "\n"
                file.write(line) # line akan ditulis ke file.csv
        
    # KAMUS VARIABEL
    # folder_name : string (menyimpan input user, menyimpan folder yang dituju untuk melakukan save)
    # folder_path : string (menyimpan path: data/folder_name)

    folder_name = input("Masukkan nama folder: ") # inisiasi variabel folder_name
    # mengecek apakah folder data sudah ada atau belum. Jika belum ada, akan dibuat
    if not os.path.exists("data"):
        print("Membuat folder data...")
        os.makedirs("data")
    folder_path = os.path.join("data", folder_name) # inisiasi variabel folder_path
    # mengecek apakah folder_path sudah ada atau belum. Jika belum ada, akan dibuat
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Membuat folder {folder_path}...")
    # menyimpan seluruh data ke file csv masing-masing
    save_csv(folder_path, "user.csv", data["user"])
    save_csv(folder_path, "monster.csv", data["monster"])
    save_csv(folder_path, "item_inventory.csv", data["item_inventory"])
    save_csv(folder_path, "monster_inventory.csv", data["monster_inventory"])
    save_csv(folder_path, "monster_shop.csv", data["monster_shop"])
    save_csv(folder_path, "item_shop.csv", data["item_shop"])
    # ditampilkan pesan bahwa proses menyimpan data berhasil
    print(f"Berhasil menyimpan data di folder {folder_path}!")
