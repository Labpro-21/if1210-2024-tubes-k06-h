def monster_upgrade(monsters, idx, owca_coin):
    pilihan_monster = monsters[idx]
    sudah_upgrade= False
    while not sudah_upgrade: 
        if pilihan_monster['level'] >= 5:
            print ()
            print("Maaf, monster yang Anda pilih sudah memiliki level maksimum.")
            print ()
            break
        else:
            upgrade_harga_arr = [300, 500, 800, 1000] 
            level_now = pilihan_monster['level']
            if level_now <= 4:
                upgrade_harga = upgrade_harga_arr[level_now - 1]
                print(f"\n{pilihan_monster['name']} akan di-upgrade ke level {pilihan_monster['level'] + 1}.")
                print(f"Harga untuk melakukan upgrade {pilihan_monster['name']} adalah {upgrade_harga} OC.")
                if owca_coin >= upgrade_harga:
                    confirm = input(">>> Lanjutkan upgrade (Y/N): ")
                    if confirm in ['Y', 'y']:
                        pilihan_monster['level'] += 1
                        owca_coin -= upgrade_harga
                        print(f"Selamat, {pilihan_monster['name']} berhasil di-upgrade ke level {pilihan_monster['level']}!")
                        sudah_upgrade = True
                    elif confirm in ['N', 'n']:
                        print("Upgrade dibatalkan.")
                        break
                    else:
                        print("Pilihan tidak valid. Silakan masukkan Y atau N.")
                else:
                    print("Maaf, OC Anda tidak mencukupi untuk melakukan upgrade.")
                    break
            else:
                print("Maaf, monster sudah mencapai level maksimum.")
                break
    return owca_coin

def laboratory(monsters, owca_coins):
    while True:  
        print ()
        print("\nSelamat datang di Lab Dokter Asep !!!\n")
        print ()
        print("============ MONSTER LIST ============")
        for ix, monster in enumerate(monsters, 1):
            print(f"{ix}. {monster['name']} (Level: {monster['level']})")

        print("\n============ UPGRADE PRICE ============")
        print("1. Level 1 -> Level 2: 300 OC")
        print("2. Level 2 -> Level 3: 500 OC")
        print("3. Level 3 -> Level 4: 800 OC")
        print("4. Level 4 -> Level 5: 1000 OC")

        pilih = input(">>> Pilih monster (atau keluar): ")
        if pilih == 'keluar':
            print ()
            print ("Terima kasih sudah datang ke Lab Dokter Asep.")
            print ()
            break  
        elif pilih.isdigit():
            pilih = int(pilih)
            if 1 <= pilih <= len(monsters):
                owca_coins = monster_upgrade(monsters, pilih - 1, owca_coins)
            else:
                print("Pilihan tidak valid, silakan pilih nomor monster yang valid.")
        else:
            print("Pilihan tidak valid, silakan pilih nomor monster yang valid.")

# CONTOH
if __name__ == "__main__":
    agent_inventory = [{'name': 'Chaca', 'level': 1}, {'name': 'Pikachow', 'level': 2}, {'name': 'Zeze', 'level': 5}]
    owca_coins = 1000

    laboratory(agent_inventory, owca_coins)


