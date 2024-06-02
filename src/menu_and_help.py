def menu_help(user, user_idx, uname, log_status):
    print("=========== HELP ===========")
    if not log_status:
        print("Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.")
        print()
        print("   1. Login: Masuk ke dalam akun yang sudah terdaftar")
        print("   2. Register: Membuat akun baru")
        return
    
    
    if user[user_idx][3] == "agent":
        print(f"Halo Agent {uname}. Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang:")
        print(f"   1. Logout: Keluar dari akun yang sedang digunakan")
        print(f"   2. Inventory: Lihat OWCA-dex dan peralatanmu, Agent {uname}")
        print(f"   3. Laboratory: Upgrade monster yang kamu miliki, Agent {uname}!")
        print(f"   4. Battle : Ayo bertarung di Arena, Agent {uname} dan menangkan hadiahnya!")
        print(f"   5. Arena : Ayo masuk ke Arena, Agent {uname} dan latih monstermu!")
        print(f"   6. Shop and Currency : Ayo belanjakan OWCA-mu dengan potion dan monster di sini, Agent {uname}!")
    else:
        print("Selamat datang, Admin. Berikut adalah hal-hal yang dapat kamu lakukan:")
        print("   1. Logout: Keluar dari akun yang sedang digunakan")
        print("   2. Shop Management: Lakukan manajemen pada SHOP sebagai tempat jual beli peralatan Agent")
        print("   3. Monster Management: Lakukan manajemen pada SHOP untuk menambah monster")

    print()
    print("Footnote:")
    print("   1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar")
    print("   2. Jangan lupa untuk memasukkan input yang valid")
