import os

def toInteger(matrix):
    for i in range (len(matrix)):
        for j in range (len(matrix[i])):
            if is_digit(str(matrix[i][j])):
                matrix[i][j] = int(matrix[i][j])
    return matrix

def is_digit(word):
    result = True
    for letter in word:
        if not(47 < ord(letter) < 58):
            result = False
            break
    return result

def isIn (x, A):
    res = False # inisiasi variabel res
    for _ in A: # looping pada setiap anggota array A
        if _ == x: # pengecekan, jika _ == x, maka variabel res menjadi True, dan looping dihentikan
            res = True
            break
    return res # fungsi memberi output res

def itsIndex (x, A):
    for i in range (len(A)):
        if A[i] == x:
            return i

def shop_currency(data, user_id):
    user = toInteger(data['user'])
    monster = toInteger(data['monster'])
    monster_inventory = toInteger(data['monster_inventory'])
    monster_shop = toInteger(data['monster_shop'])
    item_inventory = toInteger(data['item_inventory'])
    item_shop = toInteger(data['item_shop'])

    # {USER INVENTORY THINGS}
    popped_monster_inventory = []
    user_monster = []
    for i in range (1, len(monster_inventory)):
        if monster_inventory[i][0] == user_id:
            popped_monster_inventory.append(i)
            id = monster_inventory[i][1]
            type_ = monster[id][1]
            level = monster_inventory[i][2]
            user_monster_i = {
                "type" : type_,
                "level" : level
            }
            user_monster.append(user_monster_i)

    popped_user_item = []
    user_item = []
    for i in range (1, len(item_inventory)):
        if item_inventory[i][0] == user_id:
            popped_user_item.append(i)
            type_ = item_inventory[i][1]
            quantity = item_inventory[i][2]
            user_item_i = {
                "type" : type_,
                "quantity" : quantity
            }
            user_item.append(user_item_i)
    
    username = user[user_id][1]
    oc = user[user_id][4] 

    user_inventory = {
        "id" : user_id,
        "username" : username,
        "oc" : oc,
        "user_monster" : user_monster,
        "user_item" : user_item
    }
    # {AKHIR USER INVENTORY THINGS}

    # {DISPLAY MONSTER THINGS}
    popped_monster_shop = []
    display_monster = []
    for i in range (1, len(monster_shop)):
        popped_monster_shop.append(i)
        id = monster_shop[i][0]
        stock = monster_shop[i][1]
        price = monster_shop[i][2]
        type_ = monster[id][1]
        atk_power = monster[id][2]
        def_power = monster[id][3]
        hp = monster[id][4]
        display_monster_i = {
            "id" : id,
            "stock" : stock,
            "price" : price,
            "type" : type_,
            "atk_power" : atk_power,
            "def_power" : def_power,
            "hp" : hp
        }
        display_monster.append(display_monster_i)
    # {AKHIR DISPLAY MONSTER THINGS}

    # {DISPLAY ITEM THINGS}
    popped_item_shop = []
    display_item = []
    for i in range (1, len(item_shop)):
        popped_item_shop.append(i)
        id = i
        type_ = item_shop[i][0]
        stock = item_shop[i][1]
        price = item_shop[i][2]
        display_item_i = {
            "id" : id,
            "type" : type_,
            "stock" : stock,
            "price" : price
        }
        display_item.append(display_item_i)
    # {AKHIR DISPLAY ITEM THINGS}

    # {MULAI PROGRAM}
    os.system("cls")
    print("Irasshaimase! Selamat datang di SHOP!!")
    while True:
        aksi = input("Mau apa (lihat/beli/keluar) :")
        if aksi == "lihat":
            lihat_apa = ""
            while True:
                lihat_apa = input("Lihat apa (monster/item): ")
                if lihat_apa == "monster" or lihat_apa == "item":
                    break
                else:
                    print("Inputan salah!")

            if lihat_apa == "monster":
                print("ID | Type           | ATK Power | DEF Power | HP   | Stok | Harga")
                for item in display_monster:
                    print(f"{item['id']}  | {item['type']:<14} | {item['atk_power']:<9} | {item['def_power']:<9} | {item['hp']:<4} | {item['stock']:<4} | {item['price']:<5}")
            elif lihat_apa == "item":
                print("ID | Type                 | Stok  | Harga")
                for item in display_item:
                    print(f"{item['id']}  | {item['type']:<20} | {item['stock']:<5} | {item['price']:<5}")
        elif aksi == "beli":
            print(f"Jumlah OWCA coinmu sekarang adalah: {user_inventory['oc']}")
            beli_apa = ""
            while True:
                beli_apa = input("Mau beli apa? (monster/item): ")
                if beli_apa == "monster" or beli_apa == "item":
                    break
                else:
                    print("Inputan salah!")
            if beli_apa == "monster":
                id_monster_dibeli = int (input("Masukkan id monster: "))
                monster_dibeli = display_monster[id_monster_dibeli - 1]
                user_monster_type = []
                for i in range (len(user_inventory["user_monster"])):
                    user_monster_type.append(user_inventory["user_monster"][i]["type"])
                if monster_dibeli['price'] > user_inventory['oc']:
                    print("OC-mu tidak cukup.")
                elif isIn(monster_dibeli['type'], user_monster_type):
                    print(f"Monster {monster_dibeli['type']} sudah ada dalam inventory-mu! Pembelian dibatalkan.")
                else:
                    print(f"Berhasil membeli monster: {monster_dibeli['type']}. Item sudah masuk ke inventory-mu!")
                    display_monster[id_monster_dibeli - 1]["stock"] -= 1
                    type_monster_dibeli = {
                        "type" : monster_dibeli['type'],
                        "level" : 1
                    }
                    user_inventory['user_monster'].append(type_monster_dibeli)
                    user_inventory['oc'] -= monster_dibeli['price']
                    
            elif beli_apa == "item":
                id_item_dibeli = int(input("Masukkan id potion: "))
                jumlah_potion = int(input("Masukkan jumlah: "))
                item_dibeli = display_item[id_item_dibeli - 1]
                if item_dibeli['price'] * jumlah_potion > user_inventory['oc']:
                    print("OC-mu tidak cukup.")
                else:
                    print(f"Berhasil membeli item: {jumlah_potion} {item_dibeli['type']}. Item sudah masuk ke inventory-mu!")
                    display_item[id_item_dibeli - 1]["stock"] -= 1
                    belum_tersimpan = True
                    for i in range (len(user_inventory['user_item'])):
                        if user_inventory['user_item'][i]['type'] == item_dibeli['type']:
                            user_inventory['user_item'][i]['quantity'] += 1
                            print(user_inventory['user_item'])
                            belum_tersimpan = False
                    if belum_tersimpan:
                        type_item_dibeli = {
                            'type' : item_dibeli['type'],
                            'quantity' : 1
                        }
                        user_inventory['user_item'].append(type_item_dibeli)
                    user_inventory['oc'] -= item_dibeli['price']

        elif aksi == "keluar":
            print("Mr. Yanto bilang makasih, belanja lagi ya nanti :)")
            break
        else:
            print("Inputan salah!")


    for i in (len(popped_user_item) - 1,-1,-1):
        item_inventory.pop(i)

    for i in (len(popped_monster_inventory) - 1,-1,-1):
        monster_inventory.pop(i)

    for i in (len(popped_monster_shop) - 1,-1,-1):
        monster_shop.pop(i)

    for i in (len(popped_item_shop) - 1,-1,-1):
        item_shop.pop(i)

    # {ITEM INVENTORY}
    print(user_inventory['user_item'])
    for i in range (len(user_inventory['user_item'])):
        display_item_i = []
        display_item_i.append(user_id)
        display_item_i.append(user_inventory['user_item'][i]['type'])
        display_item_i.append(user_inventory['user_item'][i]['quantity'])
        item_inventory.append(display_item_i)

    # {MONSTER INVENTORY}
    monster_array = []
    for i in range (len(monster)):
        monster_array.append(monster[i][1])
    for i in range (len(user_inventory['user_monster'])):
        display_monster_i = []
        display_monster_i.append(user_id)
        index = itsIndex(user_inventory['user_monster'][i]['type'], monster_array)
        display_monster_i.append(index)
        display_monster_i.append(user_inventory['user_monster'][i]['level'])
        monster_inventory.append(display_monster_i)

    # {MONSTER SHOP}
    for i in range (len(display_monster)):
        display_monster_i = []
        display_monster_i.append(display_monster[i]['id'])
        display_monster_i.append(display_monster[i]['stock'])
        display_monster_i.append(display_monster[i]['price'])
        monster_shop.append(display_monster_i)
    # {ITEM SHOP}
    for i in range (len(display_item)):
        display_item_i = []
        display_item_i.append(display_item[i]['type'])
        display_item_i.append(display_item[i]['stock'])
        display_item_i.append(display_item[i]['price'])
        item_shop.append(display_item_i)
    user[user_id][4] = user_inventory['oc']
    data['item_inventory'] = item_inventory
    data['item_shop'] = item_shop
    data['monster_inventory'] = monster_inventory
    data['monster_shop'] = monster_shop
    data['user'] = user
    return data
