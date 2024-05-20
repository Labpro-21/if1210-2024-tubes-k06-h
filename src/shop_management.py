from login import login
from load import load 

not_monster_shop = {}
not_item_shop = {}
exit = False

# Fungsi menentukan monster yang belum ada di toko monster.
def not_monster():
    for id, data in load.monster.items():
        ada = False
        for idmonster, datamonster in load.monster_shop.items():
            if id == idmonster:
                ada = True
                break
        if not ada:
            type = data['type']
            atk_power = data['atk_power']
            def_power = data['def_power']
            hp = data['hp']
            tidak_ada = {(id):{'type':(type),'atk_power':(atk_power),'def_power':(def_power),'hp':(hp)}}
            not_monster_shop.update(tidak_ada)

# Fungsi menentukan item yang belum ada di toko item.            
def not_item():
    for id, data in load.item.items():
        ada = False
        for iditem, dataitem in load.item_shop.items():
            if id == iditem:
                ada = True
                break
        if not ada:
            type = data['type']
            tidak_ada = {(id):{'type': (type)}}
            not_item_shop = {}

# Fungsi menampilkan daftar barang yang tersedia di toko monster atau toko item.
def tampilkan_shop(barang):
    if barang == 'monster':
        print("\nID | TYPE | ATK POWER | DEF POWER | HP | STOK | HARGA")
        for id, data in load.monster_shop.items():
            stok = data['stock']
            harga = data['price']
            for idmonster, datamonster in load.monster.items():
                if idmonster == id:
                    type = datamonster['type']
                    atk_power = datamonster['atk_power']
                    def_power = datamonster['def_power']
                    hp = datamonster['hp']
            print(f"{id} | {type} | {atk_power} | {def_power} | {hp} | {stok} | {harga}")

    elif barang == 'item':
        print("\nID | TYPE | STOK | HARGA")
        for id, data in load.item_shop.items():
            type = data['type']
            stok = data['stock']
            harga = data['price']
            print(f'{id} | {type} | {stok} | {harga}')

# PROGRAM UTAMA
def shop_management():
    global exit
    if login.user['user_id'] == '0':
        aksi = input('\nPilih aksi (lihat/tambah/ubah/hapus/keluar): ')
        
        if aksi == 'lihat':
            sub_aksi = input('\nApa yang mau dilihat? (monster/item): ')

            if sub_aksi == 'monster':                   
                tampilkan_shop('monster')
            elif sub_aksi == 'item':
                tampilkan_shop('item')
        
        elif aksi == 'tambah':
            sub_aksi = input('\nApa yang mau ditambah? (monster/item): ')
            if sub_aksi == 'monster':
                print('ID | TYPE | ATK POWER | DEF POWER | HP')
                not_monster()
                for id, data in not_monster_shop.items():
                    type = data['type']
                    atk_power = data['atk_power']
                    def_power = data['def_power']
                    hp = data['hp']
                    print(f'{id} | {type} | {atk_power} | {atk_power} | {def_power} | {hp}')    

                id_monster = input("\nMasukkan ID Monster: ")
                stok = input("Masukkan Stok Awal: ")
                harga = input("Masukkan Harga: ")

                for id, data in not_monster_shop.items():
                    if id_monster == id:
                        tambah={(id):{'stock': (stok), 'price': (harga)}}
                        load.monster_shop.update(tambah)
                        print('\nITEM BERHASIL DITAMBAHKAN KE SHOP')
                        break
            
            elif sub_aksi == 'item':
                print('ID | TYPE')
                not_item()
                for id, data in not_item_shop.items():
                    type = data['type']
                    print(f'{id} | {type}')

                id_item = input('\nMasukkan ID Item: ')
                stok = input('Masukkan Stok Awal')
                harga = input('Masukkan Harga: ')

                for id, data in not_monster.items():
                    if id_item == id:
                        type = data['type']
                        tambah = {(id):{'type': (type), 'stock': (stok), 'price': (harga)}}
                        load.item_shop.update(tambah)
                        print('\nITEM BERHASIL DITAMBAHKAN KE SHOP')

        elif aksi == 'ubah':
            sub_aksi = input('\nApa yang mau diubah? (monster/item): ')
            if sub_aksi == 'monster':
                tampilkan_shop('monster')

                ubah_stok = False
                ubah_harga = False

                id = input("\nMasukkan ID Monster: ")
                stok = input("Masukkan Stok Baru: ")
                harga = input("Masukkan Harga Baru: ")

                if stok != '':
                    ubah_stok = True
                    load.monster_shop[(id)]['stock'] = (stok)
                if harga != '':
                    ubah_harga = True
                    load.monster_shop[(id)]['price'] = (harga)

                if ubah_stok:
                    if ubah_harga:
                        print(f"Monster telah berhasil diubah dengan stok baru sejumlah {stok} dan dengan harga baru {harga}")
                    else:
                        print(f"Monster telah berhasil diubah dengan stok baru sejumlah {stok}")
                else:
                    if ubah_harga:
                        print(f"Monster telah berhasil diubah dengan harga baru {harga}")
                    else:
                        print("Isi Stok/Harga yang ingin diubah")

            elif sub_aksi == 'item':
                tampilkan_shop('item')

                ubah_stok = False
                ubah_harga = False

                id = input("\nMasukkan ID Item: ")
                stok = input("Masukkan Stok Baru: ")
                harga = input("Masukkan Harga Baru: ")

                if stok != '':
                    ubah_stok = True
                    load.item_shop[(id)]['stock'] = (stok)
                if harga != '':
                    ubah_harga = True
                    load.item_shop[(id)]['price'] = (harga)

                if ubah_stok:
                    if ubah_harga:
                        print(f"Item telah berhasil diubah dengan stok baru sejumlah {stok} dan dengan harga baru {harga}")
                    else:
                        print(f"Item telah berhasil diubah dengan stok baru sejumlah {stok}")
                else:
                    if ubah_harga:
                        print(f"Item telah berhasil diubah dengan harga baru {harga}")
                    else:
                        print("Isi Stok/Harga yang ingin diubah")

        elif aksi == 'hapus':
            sub_aksi = input('\nApa yang mau dihapus? (monster/item): ')
            if sub_aksi == 'monster':          
                tampilkan_shop('monster')

                id = input("\nMasukkan ID Monster: ")
                confirm = input('Apakah anda yakin ingin menghapus Monster dari shop (y/n)? ')
                
                if confirm == 'y':
                    del load.monster_shop[(id)]
                else:
                    next
            elif sub_aksi == 'item':
                tampilkan_shop('item')

                id = input("\nMasukkan ID Item: ")
                confirm = input('Apakah anda yakin ingin menghapus Item dari shop (y/n)? ')
                
                if confirm == 'y':
                    del load.item_shop[(id)]
                else:
                    next
        
        elif aksi == 'keluar':
            exit = True
            print('Dadah Mr. Monogram!')

print('========== SELAMAT DATANG Mr. Monogram ==========')
while not exit:
    shop_management() 