import time
import math

class LCG:
    def __init__(self, seed, a=1664525, c=1013904223, m=2**32):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m

    def random(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

class Monster:
    def __init__(self, name, atk_power, def_power, max_hp, level):
        self.name = name
        self.atk_power = atk_power
        self.def_power = def_power
        self.max_hp = max_hp
        self.hp = max_hp
        self.level = level

class Potion:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect
        self.used = False

def attack(attacker, target):
    damage = attacker.atk_power
    damage_reduction = target.def_power / 100 * damage
    damage -= damage_reduction
    target.hp -= damage
    target.hp = max(0, target.hp)  # HP tidak kurang dari 0
    return math.floor(damage)  # Bulatkan ke bawah

def use_potion(monster, potion):
    if potion.used:
        print("Potion ini sudah digunakan sebelumnya dalam pertempuran ini!")
        return
    if potion.effect == 'strength':
        monster.atk_power = math.floor(monster.atk_power * 1.05)  # Bulatkan ke bawah
        print(f"{monster.name} menggunakan Strength Potion! ATK Power-nya meningkat menjadi {monster.atk_power}")
    elif potion.effect == 'resilience':
        monster.def_power = math.floor(monster.def_power * 1.05)  # Bulatkan ke bawah
        print(f"{monster.name} menggunakan Resilience Potion! DEF Power-nya meningkat menjadi {monster.def_power}")
    elif potion.effect == 'healing':
        healing_amount = min(monster.max_hp * 0.25, monster.max_hp - monster.hp)
        monster.hp += healing_amount
        monster.hp = min(monster.hp, monster.max_hp)  # HP tidak melebihi maksimal
        print(f"{monster.name} menggunakan Healing Potion! HP-nya meningkat menjadi {math.floor(monster.hp)}")
    potion.used = True

def main():
    # Menggunakan waktu saat ini sebagai seed untuk LCG
    seed = int(time.time())
    lcg = LCG(seed=seed)

    # Inisialisasi Monster Zuko dengan atribut yang dihasilkan secara acak
    zuko_name = "Zuko"
    zuko_atk_power = math.floor(lcg.random() % 31 + 20)  # Random ATK Power antara 20 dan 50
    zuko_def_power = math.floor(lcg.random() % 51)  # Random DEF Power antara 0 dan 50
    zuko_max_hp = math.floor(lcg.random() % 101 + 100)  # Random HP antara 100 dan 200
    zuko_level = 1
    zuko = Monster(zuko_name, zuko_atk_power, zuko_def_power, zuko_max_hp, zuko_level)

    # Menampilkan atribut Zuko
    print(f"Name      : {zuko.name}")
    print(f"ATK Power : {zuko.atk_power}")
    print(f"DEF Power : {zuko.def_power}")
    print(f"HP        : {math.floor(zuko.max_hp)}")  # Bulatkan ke bawah
    print(f"Level     : {zuko.level}")

    print("\n============ MONSTER LIST ============")
    print("1. Chacha")
    print("2. Pikachow")
    print("3. Zeze")

    monster_choice = 0
    while monster_choice < 1 or monster_choice > 3:
        monster_choice = int(input("\nPilih monster untuk bertarung: "))

        if monster_choice < 1 or monster_choice > 3:
            print("Pilihan nomor tidak tersedia!")

    # Menetapkan atribut Monster berdasarkan pilihan
    if monster_choice == 1:
        agent_name = "Chacha"
        agent_atk_power = 30
        agent_def_power = 15
        agent_max_hp = 150
    elif monster_choice == 2:
        agent_name = "Pikachow"
        agent_atk_power = 25
        agent_def_power = 5
        agent_max_hp = 120
    elif monster_choice == 3:
        agent_name = "Zeze"
        agent_atk_power = 35
        agent_def_power = 20
        agent_max_hp = 180

    # Membuat objek Monster untuk agent dengan atribut yang ditetapkan
    agent_level = 1
    agent = Monster(agent_name, agent_atk_power, agent_def_power, agent_max_hp, agent_level)

    # Menampilkan atribut Agent
    print(f"\nRAWRRR, Agent X mengeluarkan monster {agent.name} !!!\n")
    print(f"Name      : {agent.name}")
    print(f"ATK Power : {agent.atk_power}")
    print(f"DEF Power : {agent.def_power}")
    print(f"HP        : {math.floor(agent.max_hp)}")  # Bulatkan ke bawah
    print(f"Level     : {agent.level}")

    # Inisialisasi potion
    strength_potion = Potion("Strength Potion", "strength")
    resilience_potion = Potion("Resilience Potion", "resilience")
    healing_potion = Potion("Healing Potion", "healing")

    # Pertempuran dimulai
    turn = 1
    while True:
        print(f"\n============ TURN {turn} ({agent.name}) ============")
        print("1. Attack")
        print("2. Use Potion")
        print("3. Quit")

        choice = input("\nPilih perintah: ")

        if choice == '1':  # Attack
            damage_dealt = attack(agent, zuko)
            print(f"\nSCHWINKKK, {agent.name} menyerang {zuko.name} !!!\n")
            print(f"Name      : {zuko.name}")
            print(f"ATK Power : {zuko.atk_power}")
            print(f"DEF Power : {zuko.def_power}")
            print(f"HP        : {math.floor(zuko.hp)}")  # Bulatkan ke bawah
            print(f"Level     : {zuko.level}")
            print(f"\n{agent.name} dealt {damage_dealt} damage to {zuko.name}!\n")

            if zuko.hp <= 0:
                print("\nSelamat, Anda berhasil mengalahkan monster Zuko !!!\n")
                break

            # Zuko menyerang balik
            print(f"\n============ TURN {turn} ({zuko.name}) ============")
            damage_taken = attack(zuko, agent)
            print(f"\nSCHWINKKK, {zuko.name} menyerang {agent.name} !!!\n")
            print(f"Name      : {agent.name}")
            print(f"ATK Power : {agent.atk_power}")
            print(f"DEF Power : {agent.def_power}")
            print(f"HP        : {math.floor(agent.hp)}")  # Bulatkan ke bawah
            print(f"Level     : {agent.level}")
            print(f"\n{zuko.name} dealt {damage_taken} damage to {agent.name}!\n")

            if agent.hp <= 0:
                print("\nYahhh, Anda dikalahkan monster Zuko. Jangan menyerah, coba lagi !!!\n")
                break

            turn += 1

        elif choice == '2':  # Use Potion
            print("\nPilih potion yang ingin digunakan:")
            print("1. Strength Potion")
            print("2. Resilience Potion")
            print("3. Healing Potion")
            potion_choice = input("\nPilih potion: ")

            if potion_choice == '1':
                use_potion(agent, strength_potion)
            elif potion_choice == '2':
                use_potion(agent, resilience_potion)
            elif potion_choice == '3':
                use_potion(agent, healing_potion)
            else:
                print("\nPilihan tidak valid! Silakan pilih 1, 2, atau 3.\n")

        elif choice == '3':  # Quit
            print("\nAnda berhasil kabur dari BATTLE!\n")
            break

        else:
            print("\nPilihan tidak valid! Silakan pilih 1, 2, atau 3.\n")

if __name__ == "__main__":
    main()
