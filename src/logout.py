def logout(log_status):
    if not log_status:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        return True
    else:
        print("Logout berhasil!")
        print("\nSilahkan login lagi jika ingin mengakses kembali program")
        return False