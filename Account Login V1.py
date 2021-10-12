import time
import sys
import os
import random
import string
from pathlib import Path
import os.path
k = 1
p = 3
#
l = 1
p = 3
#
a = 1
b = 3
#
c = 1
d = 3
#
e = 1
f = 3
#
m = 1
z = 1
#
t = 1
m = 3
#
limit = 3
tries = 0
#______________________________________________________________________________________________________________________________________________________#
print ("Login - 1")
print ("Sign-up - 2")
choice = input()
if choice == "1":
    while k < p:
        print ("Enter your username:")
        enter_user = input()
        check_user = open ("All_users.txt", 'r')
        if enter_user in check_user.read():
            if os.path.isfile(enter_user+".txt"):
                while a < b:
                    print ("Enter your password:")
                    enter_pass = input()
                    check_pass = open (enter_user+".txt", 'r')
                    print ("______________________________")
                    if enter_pass == check_pass.read():
                        while t < m:
                            time.sleep(0.5)
                            print ("Hello, " + enter_user)
                            time.sleep(0.5)
                            print ("Messages - 1")
                            print ("Settings - 2")
                            print ("Log out - 3")
                            main_opt = input()
                            if main_opt == "1":
                                print ("Work in progress")
                                print ("Back - 1")
                                beta_opt = input()
                                if beta_opt == "1":
                                    print ("______________________________")
                                    time.sleep(0.5)
                                    continue
                                else:
                                    print ("______________________________")
                                    time.sleep(0.5)
                                    continue
                            if main_opt == "2":
                                print ("Change password - 1")
                                print ("Change username - 2")
                                print ("Delete account - 3")
                                print ("Back - 4")
                                set_opt = input()
                                if set_opt == "1":
                                    print ("Enter current password:")
                                    cur_pass = input()
                                    confirm_pass = open (enter_user+".txt", 'r')
                                    if cur_pass in confirm_pass.read():
                                        print ("Enter new password:")
                                        new_pass = input()
                                        time.sleep(0.5)
                                        print ("Enter your new password again:")
                                        new_double_pass = input()
                                        if new_double_pass == new_pass:
                                            print ("Changing password")
                                            change_pass = open (enter_user+".txt", 'w')
                                            change_pass.truncate(0)
                                            time.sleep(0.2)
                                            change_pass.write(new_double_pass)
                                            time.sleep(0.5)
                                            change_pass.close()
                                            print ("Your password has been changed")
                                            sys.exit()
                                        else:
                                            print ("They do not match")
                                            sys.exit()
                                    if cur_pass not in confirm_pass.read():
                                        print ("That is not your current password")
                                        sys.exit()
                                if set_opt == "2":
                                    print ("Enter your current username:")
                                    cur_user = input()
                                    change_user = open ("All_users.txt", 'r')
                                    if cur_user in change_user.read():
                                        print ("Enter new username:")
                                        new_username = input()
                                        time.sleep(0.5)
                                        print ("Enter your new username again:")
                                        new_double_username = input()
                                        if new_username == new_double_username:
                                            print ("Changing")
                                            time.sleep(0.5)
                                            save_cur_pass = open (cur_user+".txt", 'r')
                                            saved = (save_cur_pass.read())
                                            save_cur_pass.close()
                                            change_user.close()
                                            check_pass.close()
                                            time.sleep(1)
                                            os.remove(cur_user+".txt")
                                            create_new_user_file = open (new_double_username+".txt", 'w')
                                            create_new_user_file.write(saved)
                                            create_new_user_file.close()
                                            database_read_old_user = open ("All_users.txt", 'r')
                                            lines = database_read_old_user.readlines()
                                            database_read_old_user.close()
                                            database_change_user = open ("All_users.txt", 'w')
                                            for line in lines:
                                                if line.strip("\n") != cur_user:
                                                    database_change_user.write(line)
                                            database_change_user.close()
                                            database_change_user_new = open ("All_users.txt", 'w')
                                            database_change_user_new.write(new_double_username+"\n")
                                            database_change_user_new.close()
                                            print ("Your username has been changed")
                                            time.sleep(1)
                                            sys.exit()
                                        else:
                                            print ("They do not match")
                                            sys.exit()
                                    if cur_user not in change_user.read():
                                        print ("That username does not exist")
                                        time.sleep(0.5)
                                        sys.exit()
                                if set_opt == "3":
                                    print ("Are you sure, this action is irreversable")
                                    del_ac = input()
                                    if del_ac == "Yes":
                                        print ("Deleting")
                                        delete_account = open (enter_user+".txt", 'a')
                                        delete_account.truncate(0)
                                        delete_account.close()
                                        time.sleep(0.5)
                                        check_pass.close()
                                        os.remove(enter_user+".txt")
                                        database_delete = open ("All_users.txt", 'r')
                                        lines = database_delete.readlines()
                                        database_delete.close()
                                        remove_database = open ("All_users.txt", 'w')
                                        for line in lines:
                                            if line.strip("\n") != enter_user:
                                               remove_database.write(line)
                                        remove_database.close()
                                        time.sleep(1)
                                        print ("Your account has been deleted")
                                        sys.exit()
                                    if del_ac == "No":
                                        print ("Don't worry, nothing has been deleted")
                                        sys.exit()
                                if set_opt == "4":
                                    print ("______________________________")
                                    time.sleep(0.5)
                                    continue
                                else:
                                    print ("Error")
                                    sys.exit()
                            if main_opt == "3":
                                print ("Logging out")
                                time.sleep(0.5)
                                check_user.close()
                                check_pass.close()
                                sys.exit()
                            else:
                                print ("Error")
                                sys.exit()
                    if enter_pass not in check_pass.read():
                        print ("Wrong password")
                        tries = tries + 1
                        if tries == limit:
                            time.sleep(0.5)
                            print ("You have tried too many times")
                            time.sleep(1)
                            print ("Have you forgotten your password?")
                            forgotten = input()
                            if forgotten == "Yes":
                                print ("Enter a new password")
                                forgot_pass = input()
                                reset_pass = open (enter_user+".txt", 'a')
                                reset_pass.truncate(0)
                                reset_pass.close()
                                time.sleep(1)
                                reset_new = open (enter_user+".txt", 'w')
                                time.sleep(0.1)
                                reset_new.write(forgot_pass)
                                reset_new.close()
                                time.sleep(0.5)
                                print ("Your password has been changed")
                                continue
                            if forgotten == "No":
                                print ("Please wait 60 seconds before trying again")
                                time.sleep(60)
                                tries = tries - 3
                                continue
                        if limit > tries:
                            time.sleep(0.5)
                            print ("Try again")
                            continue
            else:
                print ("No account found with that name")
                sys.exit()
        if enter_user == "Admin":
            print ("Enter secure password:")
            secure = input()
            check_admin_pass = open ("Admin_Pass.txt", 'r')
            if secure == check_admin_pass.read():
                print ("Logged into admin account")
                time.sleep(0.5)
                while c < d:
                    print ("List all users - 1")
                    print ("Delete user - 2")
                    print ("Log out - 3")
                    print ("Beta test, pass encryption - 4")
                    admin_opt = input()
                    if admin_opt == "1":
                        print ("Retrieving all users:")
                        time.sleep(0.5)
                        get_all_users = open ("All_users.txt", 'r')
                        stat = os.path.getsize("All_users.txt")
                        if stat > m:
                            time.sleep(0.5)
                            print (get_all_users.read())
                            time.sleep(5)
                            print ("______________________________")
                        else:
                            print ("There are no current users")
                            print ("______________________________")
                            time.sleep(0.5)
                    if admin_opt == "2":
                        stat = os.path.getsize("All_users.txt")
                        if stat > m:
                            print ("Which user would you like to delete:")
                            delete_user_admin = input()
                            list_of_users = open ("All_users.txt", 'r')
                            if delete_user_admin in list_of_users.read():
                                print ("Are you sure, this action cannot be reversed")
                                warning_admin = input()
                                if warning_admin == "Yes":
                                    print ("Deleting")
                                    time.sleep(0.5)
                                    database_deletion = open ("All_users.txt", 'r')
                                    lines = database_deletion.readlines()
                                    database_deletion.close()
                                    admin_account_delete = open ("All_users.txt", 'w')
                                    for line in lines:
                                        if line.strip("\n") != delete_user_admin:
                                            admin_account_delete.write(line)
                                    admin_account_delete.close()
                                    time.sleep(0.2)
                                    os.remove(delete_user_admin+".txt")
                                    time.sleep(0.2)
                                    print ("The selected account has been deleted")
                                    sys.exit()
                                if warning_admin == "No":
                                    print ("Cancelled")
                                    sys.exit()
                            if delete_user_admin not in list_of_users.read():
                                print ("That account does not exist")
                                sys.exit()
                        if stat < m:
                            print ("There are no users to delete")
                            print ("______________________________")
                            time.sleep(0.5)
                    if admin_opt == "3":
                        print ("Logging out")
                        time.sleep(0.5)
                        sys.exit()
                    if admin_opt == "4":
                        print ("Work in progress")
                        time.sleep(0.5)
                        print ("______________________________")
                        continue
                    else:
                        time.sleep(0.5)
            else:
                print ("Wrong password")
                sys.exit()
        else:
            print ("No account found with that name")
            time.sleep(0.75)
            print ("Would you like to create an account - 1, or try again - 2")
            mis_opt = input()
            if mis_opt == "1":
                print ("Create a username:")
                create_username = input()
                double_user = open ("All_users.txt", 'r')
                if create_username not in double_user.read():
                    print ("Create a password:")
                    create_password = input()
                    double_user.close()
                    save_user = open (create_username+".txt", 'a')
                    save_user.write(create_password)
                    time.sleep(0.5)
                    save_user.close()
                    database_save = open ("All_users.txt", 'a')
                    database_save.write(create_username+"\n")
                    time.sleep(0.5)
                    database_save.close()
                    print ("Your account has been created")
                    sys.exit()
                if create_username in double_user.read():
                    print ("That username has already been taken")
                    time.sleep(0.5)
                    continue
            if mis_opt == "2":
                time.sleep(0.5)
                print ("______________________________")
                time.sleep(0.5)
                continue
if choice == "2":
    while l < p:
        print ("Create a username:")
        create_username = input()
        double_user = open ("All_users.txt", 'r')
        if create_username not in double_user.read():
            print ("Create a password:")
            create_password = input()
            double_user.close()
            save_user = open (create_username+".txt", 'a')
            save_user.write(create_password)
            time.sleep(0.5)
            save_user.close()
            database_save = open ("All_users.txt", 'a')
            database_save.write(create_username+"\n")
            time.sleep(0.5)
            database_save.close()
            print ("Your account has been created")
            sys.exit()
        if create_username in double_user.read():
            print ("That username has already been taken")
            time.sleep(0.5)
            continue
else:
    print ("______________________________")
    time.sleep(0.5)
