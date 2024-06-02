from save import save

def exit(data):
    # PROGRAM exit

    # SPESIFIKASI
    # program menerima input dictionary data (yang berisi data yang akan disimpan jika user ingin menyimpannya)
    # program menerima input user yesOrNo (yang berisi character)

    # KAMUS
    # KAMUS VARIABEL
    # yesOrNo : character (berisi nilai yang menentukan apakah data akna di-save (y), data tidak di-save (n), atau input tidak valid(selain y atau n))

    # ALGORITMA
    yesOrNo = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ") # inisiasi variabel yesOrNo
    if yesOrNo == "y": # pengecekan, jika yesOrNo == "y", fungsi save(data) akan dijalankan
        save(data)
    elif yesOrNo != "n": # pengecekan, jika yesOrNo tidak sama dengan "y" atau "n", fungsi exit(data) akan dijalankan kembali
        exit(data)
    # secara implisit, jika yesOrNo == "n", maka tidak ada hal yang dijalankan dan program berhenti