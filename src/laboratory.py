def cek(a, user_idx):
    if a[0] == user_idx:
            return True
    return False

def monster_upgrade(listmonster, monster,  idx, owca_coin):
    pilihan_monster = listmonster[idx]
    print(pilihan_monster)
    sudah_upgrade= False
    while not sudah_upgrade: 
        if int(pilihan_monster[2]) >= 5:
            print ()
            print("Maaf, monster yang Anda pilih sudah memiliki level maksimum.")
            print ()
            break
        else:
            upgrade_harga_arr = [300, 500, 800, 1000] 
            level_now = int(pilihan_monster[2])
            temp_owca = int(owca_coin)
            if level_now <= 4:
                upgrade_harga = upgrade_harga_arr[level_now - 1]
                print(f"\n {monster[int(pilihan_monster[1])][1]} akan di-upgrade ke level {int(pilihan_monster[2]) + 1}.")
                print(f"Harga untuk melakukan upgrade {monster[int(pilihan_monster[1])][1]} adalah {upgrade_harga} OC.")
                if temp_owca >= upgrade_harga:
                    confirm = input(">>> Lanjutkan upgrade (Y/N): ")
                    if confirm in ['Y', 'y']:
                        pilihan_monster[2] = str(int(pilihan_monster[2]) + 1)
                        # monster_inv[monster_idx][2] = pilihan_monster[2]
                        temp_owca -= upgrade_harga
                        print(f"Selamat, {monster[int(pilihan_monster[1])][1]} berhasil di-upgrade ke level {pilihan_monster[2]}!")
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
    return str(temp_owca)

def laboratory(yourmonster , monster, owca_coins, user_idx, user):
    while True:  
        print ()
        print("\nSelamat datang di Lab Dokter Asep !!!\n")
        print ()
        print("============ MONSTER LIST ============")
        y = 0
        mons_list = []
        for i in yourmonster :
            if cek(i, user_idx):
                if i[1] != "monster_id" :
                    mons_list.append(i)
                    print(f"{y+1}. {monster[int(i[1])][1]} " ": level ", f"{i[2]}")
                    y+=1
                

        print("\n============ UPGRADE PRICE =back===========")
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
            if 1 <= pilih <= len(mons_list):
                owca_coins = monster_upgrade(mons_list, monster, pilih-1, owca_coins)
                user[int(user_idx)+1][4] = owca_coins
            else:
                print("Pilihan tidak valid, silakan pilih nomor monster yang valid.")
        else:
            print("Pilihan tidak valid, silakan pilih nomor monster yang valid.")

#das CONTOH
if __name__ == "__main__":
    agent_inventory = [{'name': 'Chaca', 'level': 1}, 
                       {'name': 'Pikachow', 'level': 2}, 
                       {'name': 'Zeze', 'level': 5}]
    owca_coins = 1000

    laboratory(agent_inventory, owca_coins)
