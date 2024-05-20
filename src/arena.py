import os
from rng import random_uniform_sample
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

def arena(data, user_id):
    monster = toInteger(data['monster'])
    monster_inventory = toInteger(data['monster_inventory'])
    item_inventory = toInteger(data['item_inventory'])

    popped_monster_idx = []
    user_monster = []
    for i in range (1, len(monster_inventory)):
        if monster_inventory[i][0] == user_id:
            popped_monster_idx.append(i)
            monster_id = monster_inventory[i][1]
            level = monster_inventory[i][2]
            type_monster = monster[monster_id][1]
            atk_power = monster[monster_id][2]
            def_power = monster[monster_id][3]
            hp = monster[monster_id][4]
            user_monster_i = {
                "monster_id" : monster_id,
                "level" : level,
                "type_monster" : type_monster,
                "atk_power" : atk_power * (100 + (level - 1) * 10) / 100,
                "def_power" : def_power * (100 + (level - 1) * 10) / 100,
                "hp" : hp * (100 + (level - 1) * 10) / 100,
                "hp_normal" : hp * (100 + (level - 1) * 10) / 100
            }
            user_monster.append(user_monster_i)

    popped_item_idx = []
    user_item = []
    for i in range (1, len(item_inventory)):
        if item_inventory[i][0] == user_id:
            popped_item_idx.append(i)
            user_item_i = {
                "type": item_inventory[i][1],
                "quantity": item_inventory[i][2]
            }
            if user_item_i["type"] == "Strength Potion":
                user_item_i["efect"] = "Increases ATK Power"
                user_item_i["message1"] = "Setelah meminum ramuan ini, aura kekuatan terlihat mengelilingi "
                user_item_i["message2"] = " dan gerakannya menjadi lebih cepat dan mematikan."
            elif user_item_i["type"] == "Resilience Potion":
                user_item_i["efect"] = "Increases DEF Power"
                user_item_i["message1"] = "Setelah meminum ramuan ini, muncul sebuah energi pelindung di sekitar "
                user_item_i["message2"] = " yang membuatnya terlihat semakin tangguh dan sulit dilukai."
            elif user_item_i["type"] == "Healing Potion":
                user_item_i["efect"] = "Restores Health"
                user_item_i["message1"] = "Setelah meminum ramuan ini, luka-luka yang ada di dalam tubuh "
                user_item_i["message2"] = " sembuh dengan cepat. Dalam sekejap, dia terlihat kembali prima dan siap melanjutkan pertempuran."
            user_item.append(user_item_i)

    os.system("cls")

    print("Selamat datang di Arena!!")
  
    print("============ MONSTER LIST ============")
    for i in range (len(user_monster)):
        print(f"{i+1}. {user_monster[i]['type_monster']}")

    choosen_monster_id = 0
    while True:
        choosen_monster_id = int(input("Pilih monster untuk bertarung: "))
        if (0 < choosen_monster_id <= len(user_monster)):
            break
        else:
            print("Pilihan nomor tidak tersedia!")
    using_monster = user_monster[choosen_monster_id - 1]

    print(f"""
RAWRRR, {data["user"][user_id+1][1]} mengeluarkan monster {using_monster['type_monster']} !!!

Name      : {using_monster['type_monster']}
ATK Power : {using_monster['atk_power']}
DEF Power : {using_monster['def_power']}
HP        : {using_monster['hp']}
Level     : {using_monster['level']}
""")
    
    lanjut = input("Klik apapun untuk lanjut: ")

    stage = 1
    num = 1
    jumlah_hadiah_array = [30,50,100,170,260]
    jumlah_hadiah = 0
    while True:
        print(f"============= STAGE {stage} =============")

        apakah_menang = False
        used_potion = {
            "Strength Potion" : 0 ,
            "Resilience Potion" : 0,
            'Healing Potion' : 0
        }

        n = random_uniform_sample(15) + 1
        level_lawan = stage
        monster_lawan = monster[n]
        data_lawan = {
            "monster_id" : monster_lawan[0],
            "level" : level_lawan,
            "type_monster" : monster_lawan[1],
            "atk_power" : monster_lawan[2] * (100 + (level_lawan - 1) * 10) / 100,
            "def_power" : monster_lawan[2] * (100 + (level_lawan - 1) * 10) / 100,
            "hp" : monster_lawan[4] * (100 + (level_lawan - 1) * 10) / 100,
            "hp_normal" : monster_lawan[4] * (100 + (level_lawan - 1) * 10) / 100  
        }
        

        print(f"""
RAWRRR, Monster {data_lawan["type_monster"]} telah muncul !!!

Name      : {data_lawan["type_monster"]}
ATK Power : {data_lawan["atk_power"]}
DEF Power : {data_lawan["def_power"]}
HP        : {data_lawan["hp"]}
Level     : {data_lawan["level"]}
    """) 

        
        print(f"""
============ TURN {num} ({using_monster['type_monster']}) ============
1. Attack
2. Use Potion
3. Quit
""")
        turn = 0
        while True:
            turn = int(input("Pilih perintah: "))
            if turn < 1 or turn > 3:
                print("Perintah tidak valid!")
                turn = int(input("Pilih perintah: "))
            else:
                break
        print("\n")
        if turn == 3:
            print("Anda berhasil kabur dari BATTLE!")
            break
        elif turn == 2:
            if len(user_item) == 0:
                print("Anda tidak memiliki potion dalam inventory!")
            else:
                potion = 0
                while True:
                    print("============ POTION LIST ============")
                    for i in range(len(user_item)):
                        print(f"{i+1}. {user_item[i]['type']} (Qty : {user_item[i]['quantity']}) - {user_item[i]['efect']}")
                    print(f"{len(user_item) + 1}. Cancel")
                    print("\n")
                    potion = int(input("Potion yang diinginkan: "))
                    if potion < 1 or potion > len(user_item) + 1:
                        print("Potion tidak valid!")
                    elif potion == len(user_item) + 1:
                        print("Batal menggunakan potion.")
                        break
                    elif used_potion[user_item[potion - 1]["type"]] == 1 and user_item[potion - 1]['type'] != "Healing Potion":
                        print(f"Kamu mencoba memberikan ramuan ini kepada {using_monster['type_monster']}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.")
                    elif user_item[potion - 1]["quantity"] == 0:
                        print("Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!")
                    else:
                        if user_item[potion - 1]["type"] == "Strength Potion":
                            user_item[potion - 1]["quantity"] -= 1
                            used_potion["Strength Potion"] = 1
                            print(f"{user_item[potion - 1]['message1']}{using_monster['type_monster']}{user_item[potion - 1]['message2']}\n")
                        elif user_item[potion - 1]["type"] == "Resilience Potion":
                            user_item[potion - 1]["quantity"] -= 1
                            used_potion["Resilience Potion"] = 1
                            print(f"{user_item[potion - 1]['message1']}{using_monster['type_monster']}{user_item[potion - 1]['message2']}\n")
                        elif user_item[potion - 1]["type"] == "Healing Potion":
                            user_item[potion - 1]["quantity"] -= 1
                            using_monster['hp'] = using_monster['hp_normal']
                            print(f"{user_item[potion - 1]['message1']}{using_monster['type_monster']}{user_item[potion - 1]['message2']}\n")
                        is_did_something = 1
                        break

        elif turn == 1:
            if used_potion["Strength Potion"] == 1:
                random_attack = random_uniform_sample(60) - 30
                attack = (using_monster['atk_power']) * (100 + random_attack) / 100
                print(f"attack yang kamu berikan {random_attack}% dari attack_power!")
                attack = (attack * 1.2)
                print(f"Attack bertambah 20% karena penggunaan Strength Potion: {attack}") 
                attack = attack * (100 - data_lawan['atk_power']) / 100
                print(f"Attack berkurang {100 - data_lawan['atk_power']}% karena DEF Power: {attack}")
                data_lawan["hp"] = (data_lawan["hp"] - attack) // 1
                print(f"Sisa HP {data_lawan['type_monster']} adalah {data_lawan['hp']}")
            else:
                attack = using_monster['atk_power'] * (100 - data_lawan['atk_power']) / 100
                print(f"Attack berkurang {100 - data_lawan['atk_power']}% karena DEF Power: {attack}")
                data_lawan["hp"] = ((data_lawan["hp"]) - attack) // 1
                if data_lawan['hp'] <= 0:
                    data_lawan['hp'] = 0
                print(f"Sisa HP {data_lawan['type_monster']} adalah {data_lawan['hp']}")
            
            if data_lawan["hp"] <= 0:
                print("\n==============================================")
                print(f"Selamat, Anda berhasil mengalahkan monster {data_lawan['type_monster']} !!!")
                print(f"STAGED CLEARED !!! Total OC yang diperoleh pada sesi ini: {data['user'][user_id + 1][4]}")
                if stage < 5:
                    print("Memulai stage berikutnya ...")
                if stage == 5:
                    print("Selamat, Anda berhasil menyelesaikan seluruh stage Arena !!!")
                jumlah_hadiah += jumlah_hadiah_array[stage-1]
                data_lawan['hp'] = data_lawan['hp_normal']
                apakah_menang = True
                break

            is_did_something = 1
        
        if is_did_something == 1:
            print(f"============ TURN {num} ({data_lawan['type_monster']}) ============")
            if used_potion["Resilience Potion"] == 1:
                random_damage = random_uniform_sample(60) - 30
                damage = int(data_lawan['atk_power']) * (100 - random_damage) / 100
                print(f"attack yang lawanmu berikan {random_damage}% dari attack_powernya!")
                damage = (damage * 0.8)
                print(f"Damage berkurang 20% karena penggunaan Resilience Potion: {damage}")
                damage = damage * (100 - using_monster['def_power']) / 100
                print(f"Damage berkurang {100 - using_monster['def_power']}% karena DEF Power: {damage}")
                using_monster['hp'] = (using_monster['hp'] - damage) // 1
                print(f"Sisa HP {using_monster['type_monster']} adalah {using_monster['hp']}")
            else:
                damage = int(data_lawan['atk_power']) * (100 - int(using_monster['def_power'])) / 100
                print(f"Damage berkurang {100 - using_monster['def_power']}% karena DEF Power: {damage}")
                using_monster['hp'] = (using_monster['hp'] - damage) // 1
                if using_monster['hp'] <= 0:
                    using_monster['hp'] = 0
                print(f"Sisa HP {using_monster['type_monster']} adalah {using_monster['hp']}")
            num += 1
            if using_monster['hp'] <= 0:
                print(f"Yahhh, Anda dikalahkan monster {data_lawan['type_monster']}. Jangan menyerah, coba lagi !!!")
                using_monster['hp'] = using_monster['hp_normal']
                print(f"GAME OVER! Sesi latihan berakhir pada stage {stage}!")
                break

            lanjut = input("Klik apapun untuk lanjut: ")
    
    print(f"""
============== STATS ==============
Total hadiah      : {jumlah_hadiah} OC
Jumlah stage      : {stage}
Damage diberikan  : {monster_lawan[2]}
Damage diterima   : {using_monster['atk_power']}
    """)
    data["user"][user_id + 1][4] = int(data["user"][user_id + 1][4])
    data["user"][user_id + 1][4] += jumlah_hadiah
    user_monster.pop(choosen_monster_id - 1)
    user_monster.append(using_monster)

    for i in (len(popped_item_idx)-1,-1,-1):
        item_inventory.pop(i)
    for i in (len(popped_monster_idx) - 1,-1,-1):
        monster_inventory.pop(i)

    user_item_matrixed = []
    for data in user_item:
        user_item_i_matrixed = []
        user_item_i_matrixed.append(user_id)
        user_item_i_matrixed.append(data["type"])
        user_item_i_matrixed.append(str(data["quantity"]))
        user_item_matrixed.append(user_item_i_matrixed)

    user_monster_matrixed = []
    for data in user_monster:
        user_monster_i_matrixed = []
        user_monster_i_matrixed.append(user_id)
        user_monster_i_matrixed.append(data["monster_id"])
        user_monster_i_matrixed.append(str(data["level"]))
        user_monster_matrixed.append(user_monster_i_matrixed)

    monster_inventory.extend(user_monster_matrixed)
    item_inventory.extend(user_item_matrixed)
    data["item_inventory"] = item_inventory
    data["monster_inventory"] = monster_inventory   
