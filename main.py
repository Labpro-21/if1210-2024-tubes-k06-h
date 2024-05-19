import sys
sys.path.append('src')  

# Melakukan import fungsi fungsi yang tidak dibuat dalam file main
from load import load
from login import login
from logout import logout
from register import register
from save import save
from exit import exit
from menu_and_help import menu_help
from laboratory import laboratory
from laboratory import monster_upgrade
from inventory import inventory

# Inisialisasi seluruh variabel
is_Logged_in = False
is_Playing = True
dict = load()
user_idx = 1

while is_Playing :
    if dict is not None :
        if not is_Logged_in  : 
            print("1. Login")
            print("2. Register")
            print("3. Help")
            command = int(input((">>> Pilih command yang akan kamu pilih : "))) 
            # Meminta pengguna untuk memberikan input berupa nilai 1/2/3 sesuai keterangan
            if command == 1 :
                is_Logged_in, user_idx = login(dict['user']) 
            # Akan menjalankan fungsi login apabila pengguna memberikan input nilai 1
            
            elif command == 2 :
                register(dict['user'])
                save(dict)
            # Akan menjalankan fungsi register apabila pengguna memberikan input nilai 2
            # Selanjutnya akan menjalankan fungsi save untuk menyimpan informasi hasil register
              
            elif command == 3 :
                menu_help(dict['user'], user_idx, dict['user'][user_idx][1], is_Logged_in)
                cmd_help = (int(input("\n>>> Pilih fungsi : ")))
                # Akan menjalankan fungsi menu_help apabila pengguna memberikan input nilai 3
                if not is_Logged_in :
                # Akan dieksekusi ketika belum login
                    if cmd_help == 1 :
                        is_Logged_in, user_idx = login(dict['user'])
                    # Akan menjalankan fungsi login apabila pengguna memberikan input nilai 1

                    elif cmd_help == 2 :
                        register(dict['user'])
                        save(dict)
                    # Akan menjalankan fungsi register apabila pengguna memberikan input nilai 2
                    # Selanjutnya akan menjalankan fungsi save untuk menyimpan informasi hasil register
                
                elif dict['user'][user_idx][3] == "agent" and is_Logged_in :
                # Akan dieksekusi ketika sudah login dan memiliki role agent    
                    if cmd_help == 1 :
                        logout(dict['user'])
                        is_Logged_in = False
                        user_idx = 1
                        
                    elif cmd_help == 2 :
                        inventory(dict['item_inventory'], dict['monster'], dict['monster_inventory'], dict['user'][4])

                    elif cmd_help == 3 :
                        laboratory(dict['monster'], dict['user'][4])
  #==================================================================================================
                else :
                # Akan dieksekusi ketika role adalah admin
                    if cmd_help == 1 :
                        logout(dict['user'])
                        is_Logged_in = False
                        user_idx = 1
                        
                    elif cmd_help == 2 :
                        print("\nLoading...")
#==================================================================================================
            while command != 1 and command != 2 and command != 3 :
            # Akan melakukan pengulangan ketika command tidak tersedia dalam pilihan
                print ("Command tidak tersedia.")
                command = int(input(">>> Pilih command yang akan kamu pilih : "))
                print("1. Login")
                print("2. Register")
                print("3. Help")
                if command == 1 :
                    is_Logged_in, user_idx = login(dict['user']) 

                elif command == 2 :
                    register(dict['user'])
                    save(dict)

                elif command == 3 :
                    menu_help(dict['user'], user_idx, dict['user'][user_idx][1], is_Logged_in)
                    cmd_help = (int(input("\n>>> Pilih fungsi : ")))

                    if not is_Logged_in :
                        if cmd_help == 1 :
                            is_Logged_in, user_idx = login(dict['user'])

                        elif cmd_help == 2 :
                            register(dict['user'])
                            save(dict)

                    elif dict['user'][user_idx][3] == "agent" and is_Logged_in:
                        if cmd_help == 1 :
                            logout(dict['user'])
                            is_Logged_in = False
                            user_idx = 1

                        # elif cmd_help == 2 :
                        #     inventory()
                        
                        elif cmd_help == 3 :
                            laboratory(dict['monster'], dict['user'][4])

                    else : 
                    # Kalau role adalah admin
                        if cmd_help == 1 :
                            logout(dict['user'], user_idx)
                            is_Logged_in = False
                            
                        elif cmd_help == 2 :
                            print("\nLoading...")
            
            print("\nLoading...")
        
        print("\nMasukkan command \"Help\" untuk daftar command yang dapat kamu panggil.")
        print("Masukkan command \"Exit\" untuk keluar dari program.")
        
        cmd_main = input("\n >>> Masukkan command : ").lower()
        if cmd_main == "help" :
            menu_help(dict['user'], user_idx, dict['user'][user_idx][1], is_Logged_in)
            cmd_help = (int(input("\n>>> Pilih fungsi : ")))

            if not is_Logged_in :
                if cmd_help == 1 :
                    is_Logged_in, user_idx = login(dict['user'])

                elif cmd_help == 2 :
                    register(dict['user'])
                    save(dict)

            elif dict['user'][user_idx][3] == "agent" and is_Logged_in:
                if cmd_help == 1 :
                    logout(dict['user'])
                    is_Logged_in = False
                    user_idx = 1

                elif cmd_help == 2 :
                    inventory(dict['item_inventory'], dict['monster'], dict['monster_inventory'], dict['user'][user_idx][4])

                elif cmd_help == 3 :
                    laboratory(dict['monster'], dict['user'][4])
#==================================================================================================
            else : 
            # Kalau role adalah admin
                if cmd_help == 1 :
                    logout(dict['user'])
                    is_Logged_in = False
                    user_idx = 1
                    
                elif cmd_help == 2 :
                    print("\nLoading...")
#==================================================================================================
        elif cmd_main == "exit" :
            print ("\nTerima kasih!")
            print ("Sampai jumpa.")
            print ("\n")
            exit('data')
            is_Playing = False

        while cmd_main != "exit" and cmd_main != "help" :
            print ("Loading...")
            print ("\nCommand tidak tersedia.")
            print ("Masukkan command kembali.")
            print("\nMasukkan command \"Help\" untuk daftar command yang dapat kamu panggil.")
            print("Masukkan command \"Exit\" untuk keluar dari program.")
            cmd_main = input("\n >>> Masukkan command : ").lower()
            if cmd_main == "help" :
                menu_help(dict['user'], user_idx, dict['user'][user_idx][1], is_Logged_in)
                cmd_help = (int(input("\n>>> Pilih fungsi : ")))

                if not is_Logged_in :
                    if cmd_help == 1 :
                        is_Logged_in, user_idx = login(dict['user'])

                    elif cmd_help == 2 :
                        register(dict['user'])
                        save(dict)

                elif dict['user'][user_idx][3] == "agent" and is_Logged_in:
                    if cmd_help == 1 :
                        logout(dict['user'])
                        is_Logged_in = False
                        user_idx = 1

                    elif cmd_help == 3 :
                        laboratory(dict['monster'], dict['user'][4])
#==================================================================================================
                else : 
                # Kalau role adalah admin
                    if cmd_help == 1 :
                        logout(dict['user'])
                        is_Logged_in = False
                        user_idx = 1
                        
                    elif cmd_help == 2 :
                        print("\nLoading...")
#==================================================================================================
            elif cmd_main == "exit" :
                print ("\nTerima kasih!")
                print ("Sampai jumpa.")
                print("\n")
                exit('data')
                is_Playing = False
