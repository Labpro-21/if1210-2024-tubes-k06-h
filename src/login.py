def login(user):
    user_input = input("Username: ")
    pass_input = input("Password: ")

    user_idx = 0
    user_valid = False

    for i in range(len(user)):
        if user[i][1] == user_input:
            user_valid = True
            user_idx = i
            break

    if not user_valid:
        print("Username tidak terdaftar!")
        return False
    elif user[user_idx][2] != pass_input:
        print("Password salah!")
        return False
    else:
        print(f"Selamat datang, Agent {user_input}!")
        print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
        return True