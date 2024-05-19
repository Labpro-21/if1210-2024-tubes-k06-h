def pot_Inventory (userinventory):
    for i in userinventory:
        if i[1]=='strengthpotion':
            jumlahstr=i[2]
            break
    else : jumlahstr = 0
    for i in userinventory:
       if i[1]=='respotion' :
            jumlahres=i[2]
            break
    else : jumlahres = 0
    for i in userinventory:
        if i[1]=='healingpotion' :
           jumlahheal=i[2]
           break
    else : jumlahheal = 0
    return [jumlahstr,jumlahres,jumlahheal]

def pot_List (qty): 
    pot_Type = ['ATK', 'DEF', 'HEAL']
    pot_Type_2 = []
    pot_Qty =[]
    for i in range (3): 
        if qty[i] != 0 :
            pot_Type_2.append(pot_Type[i])
            pot_Qty.append(qty[i])
    return (pot_Type_2, pot_Qty)

def monster_Id (yourmonsterdata):
    mons_Id_Array = []
    for i in yourmonsterdata :
       mons_Id_Array.append(i[1])
    return mons_Id_Array

def monster_Lv (yourmonsterdata):
    mons_Lv_Array = []
    for i in yourmonsterdata :
       mons_Lv_Array.append(i[2])
    return mons_Lv_Array

def inventory(userinventory, yourmonsterdata, monsterdata, coin) :
    print(f'jumlah OWCA coin anda saat ini : {coin}')
    while True :
        check = input('Silakan pilih jenis item yang ingin diketahui Anda (Monster/Item/Back): ')
        if check.lower() == 'item' :
            x=1
            types=[]
            for i in userinventory:
                if i[1] == 'Strength Potion' :
                    type = 'ATK potion'
                elif i[1] == 'Resilience Potion' :
                    type = 'DEF potion'
                elif i[1] == 'Healing Potion' :
                    type = 'HEAL potion'

                types.append(type)
                print(f'{x}. Type: {type}')
                x+=1
            while True :
                pot_Number = input('Masukkan nomor potion untuk menampilkan detail item (1/2/3/Back): ')
                if pot_Number.lower() != 'back':
                    pot_Number = int(pot_Number)
                    print(f'Type: {types[pot_Number-1]}')
                    print(f'Quantity: {userinventory[pot_Number-1][2]}')
                else :
                    break
        elif check.lower() == 'monster' :
            y = 0
            for i in yourmonsterdata :
                print(f"{y+1}. {i[1]}")
                y+=1
            while True :
                mons_Number = input('Masukkan nomor monster untuk menampilkan detail monster (1/2/dst/Back): ')
                if mons_Number.lower() != 'back' :
                    mons_Number = int(mons_Number)
                    monsterlvl = int(yourmonsterdata[mons_Number-1][2])
                    for i in monsterdata :
                        if i[1]==yourmonsterdata[mons_Number-1][1] :
                            print(f'Nama      : {i[1]}')
                            print(f'ATK Power : {int(i[2])+(monsterlvl-1)*(5/100)*(int(i[2]))}')
                            print(f'DEF Power : {int(i[3])+(monsterlvl-1)*(5/100)*(int(i[3]))}')
                            print(f'HP        : {int(i[4])+(monsterlvl-1)*(5/100)*(int(i[4]))}')
                            print(f'Level     : {monsterlvl}')
                else :
                    break
        elif check.lower() == 'back' :
            break 