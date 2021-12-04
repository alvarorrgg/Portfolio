import os
import datetime
# Falta en get_info y el modify


class contact_info:
    def __init__(self) -> None:
        self.name = ""
        self.surname = ""
        self.surname_2 = ""
        self.birthday = ""
        self.phone_number = ""
        self.email = ""
        self.relation = ""
        self.extra = ""
        self.info = ""

    def clean_class(self):
        self.name = ""
        self.surname = ""
        self.surname_2 = ""
        self.birthday = ""
        self.phone_number = ""
        self.email = ""
        self.relation = ""
        self.extra = ""
        self.info = ""

    def print_info(self):
        info = self.info.split("|")
        for i in range(len(info)):
            if "(1)" in info[i]:
                print(f"Name: {info[i][3:]}")
            elif "(2)" in info[i]:
                print(f"First surname: {info[i][3:]}")
            elif "(3)" in info[i]:
                print(f"Second surname: {info[i][3:]}")
            elif "(4)" in info[i]:
                print(f"Birthday: {info[i][3:]}")
            elif "(5)" in info[i]:
                print(f"Phone: {info[i][3:]}")
            elif "(6)" in info[i]:
                print(f"Email: {info[i][3:]}")
            elif "(7)" in info[i]:
                print(f"Relation: {info[i][3:]}")
            elif "(8)" in info[i]:
                print(f"Extra info: {info[i][3:]}")
        return

    def create_info(self):
        if len(self.name) == 0:
            return False
        else:
            self.info += ("(1)"+self.name + "|")
            if len(self.surname) != 0:
                self.info += ("(2)"+self.surname + "|")
            if len(self.surname_2) != 0:
                self.info += ("(3)"+self.surname_2 + "|")
            if len(self.birthday) != 0:
                self.info += ("(4)"+self.birthday + "|")
            if len(self.phone_number) != 0:
                self.info += ("(5)"+self.phone_number + "|")
            if len(self.email) != 0:
                self.info += ("(6)"+self.email + "|")
            if len(self.relation) != 0:
                self.info += ("(7)"+self.relation + "|")
            if len(self.extra) != 0:
                self.info += ("(8)"+self.extra + "|")
            self.info = self.info[0:-1] + "\n"
            return True


def print_info_str(info):
    info = info.split("|")
    for i in range(len(info)):
        if "(1)" in info[i]:
            print(f"Name: {info[i][3:]}")
        elif "(2)" in info[i]:
            print(f"First surname: {info[i][3:]}")
        elif "(3)" in info[i]:
            print(f"Second surname: {info[i][3:]}")
        elif "(4)" in info[i]:
            print(f"Birthday: {info[i][3:]}")
        elif "(5)" in info[i]:
            print(f"Phone: {info[i][3:]}")
        elif "(6)" in info[i]:
            print(f"Email: {info[i][3:]}")
        elif "(7)" in info[i]:
            print(f"Relation: {info[i][3:]}")
        elif "(8)" in info[i]:
            print(f"Extra info: {info[i][3:]}")
    return


def contact_book_has_contact(book_name, info):
    info = info[:-1]
    info_array = info.split("|")
    em_ph_index = [-1, -1]
    em_ph_index_file = [-1, -1]
    for i in range(len(info_array)):
        if "(5)" in info_array[i]:
            em_ph_index[0] = i
        elif "(6)" in info_array[i]:
            em_ph_index[1] = i
    with open(book_name, "r") as g:
        line = g.readline()
        while line:
            em_ph_index_file = [-1, -1]
            info_array_file = line.split("|")
            for i in range(len(info_array_file)):
                if "(5)" in info_array_file[i]:
                    em_ph_index_file[0] = i
                elif "(6)" in info_array_file[i]:
                    em_ph_index_file[1] = i
            if em_ph_index[0] != -1 and em_ph_index[1] != -1 and em_ph_index_file[0] != -1 and em_ph_index_file[1] != -1:
                if info_array[em_ph_index[0]] == info_array_file[em_ph_index_file[0]] and info_array[em_ph_index[1]] == info_array_file[em_ph_index_file[1]]:
                    g.close()
                    print("There is a contact with that email and phone number")
                    return True
            elif em_ph_index[0] != -1 and em_ph_index_file[0] != -1:

                if info_array[em_ph_index[0]] == info_array_file[em_ph_index_file[0]]:
                    g.close()
                    print("There is a similar contact with that phone number")
                    return True
            elif em_ph_index[1] != -1 and em_ph_index_file[1] != -1:
                if info_array[em_ph_index[1]].strip() == info_array_file[em_ph_index_file[1]].strip():
                    g.close()
                    print("There is a similar contact with that email. ")
                    return True

            line = g.readline()
    return False


def add_to_contact_book(book_name):
    contact = contact_info()
    f = open(book_name, "a")
    while True:
        contact.name = input("Please input the contact name: ")
        if len(contact.name) != 0 and contact.name.isalpha():
            break
        else:
            print("~~~~")
            if len(contact.name) == 0:
                print("This field is mandatory.")
            else:
                print("This needs to be an alphabetic field")
            print("~~~~")

    while True:
        contact.surname = input("Introduce first surname: ")
        if len(contact.surname) == 0 or contact.surname.isalpha():
            break
        else:
            print("~~~~")
            print("This needs to be an alphabetic field")
            print("~~~~")

    while True:
        contact.surname_2 = input("Introduce second surname: ")
        if len(contact.surname_2) == 0 or contact.surname_2.isalpha():
            break
        else:
            print("~~~~")
            print("This needs to be an alphabetic field")
            print("~~~~")

    while True:
        contact.birthday = input("Introduce birthday (YYYY-MM-DD): ")
        if len(contact.birthday) == 0:
            break
        else:
            format = '%Y-%m-%d'
            try:
                datetime.datetime.strptime(contact.birthday, format)
                break
            except ValueError:
                print("~~~~")
                print("That date does not exist. ")
                print("~~~~")
                continue

    while True:
        contact.phone_number = input("Please write the phone number: ")
        if len(contact.phone_number) != 0:
            if len(contact.phone_number) != 9 or not contact.phone_number.isdecimal():
                print("~~~~")
                print("Wrong phone input: Input must be 9 numbers.")
                contact.phone_number = ""
                print("~~~~")
                continue

        while True:
            contact.email = input("Please write the email: ")
            if len(contact.email) != 0 and contact.email.count("@") != 1:
                print("~~~~")
                print("Wrong form of email: It must contain an @ character ")
                contact.email = ""
                print("~~~~")
            else:
                break

        if len(contact.email) == 0 and len(contact.phone_number) == 0:
            print("~~~~")
            print("You have to enter either a phone number or an email.")
            print("~~~~")
            continue
        else:
            break

    contact.relation = input("What is your relation with the contact: ")
    contact.extra = input("Write any extra info: ")
    print("#####################################################################")
    contact.create_info()

    if contact_book_has_contact(book_name, contact.info) == True:
        f.close()
        contact.clean_class()
        return True

    print("Do you want to add this info to your contact book?")
    contact.info = contact.info
    contact.print_info()
    print("#####################################################################")
    decision = input(
        "Write 'No' or 'N' to delete info, Enter to add: ").upper()
    print("\n")
    if decision == "NO" or decision == "N":
        print("Contact not added...")
        f.close()
        contact.clean_class()

    else:
        print("Adding contact...")
        f.write(contact.info)
        f.close()

    return True


def delete_from_contact_book(book_name):
    name = input("Introduce the name of the contact you want to delete: ")
    while name.isalpha() == False:
        print("Thats not a valid input.")
        name = input("Introduce the name of the contact you want to delete: ")

    name = name.upper()
    new_file = []
    deleted_lines = []
    split_line = []
    flag = 0
    temp = 0
    with open(book_name, "r") as g:
        line = g.readline()
        while line:
            split_line = line.split("|")
            split_line[0] = split_line[0].replace("(1)", "")
            split_line[0] = split_line[0].upper()
            if name in split_line[0]:
                deleted_lines.append(line)
            else:
                new_file.append(line)
            line = g.readline()
    if len(deleted_lines) == 0:
        print("There are no valid names.")
        return True
    print("~~~~")
    for i in range(len(deleted_lines)):
        print(f"{i+1}: {deleted_lines[i]}")
    print("~~~~")
    nums = input(
        "Introduce between comas the number of the contacts you want to delete(enter to not delete): ")
    if len(nums) == 0:
        return True
    nums = nums.split(",")
    nums = set(nums)
    for i in nums:
        try:
            a = int(i)
        except:
            flag = 1
            continue
        if a > len(deleted_lines) or a < -1:
            flag = 1
            continue
        else:
            deleted_lines.pop(a-temp-1)
            temp += 1
    if flag == 1:
        print("There were invalid inputs, we skipped those")
    for j in deleted_lines:
        new_file.append(j)
    g = open(book_name, "w")
    for k in new_file:
        g.write(k)
    return True


def modify_contact_book(book_name):
    name = ""
    name = input("Introduce the name of the contact you want to modify: ")
    while name.isalpha() == False:
        print("Thats not a valid input.")
        name = input("Introduce the name of the contact you want to modify: ")

    name = name.upper()
    new_file = []
    mod_lines = []
    split_line = []
    surname_1 = ""
    surname_2 = ""
    birthday = ""
    number = ""
    mail = ""
    extra = ""
    relation = ""
    count = 0
    with open(book_name, "r") as g:
        line = g.readline()
        while line:
            split_line = line.split("|")
            split_line[0] = split_line[0].replace("(1)", "")
            split_line[0] = split_line[0].upper()
            if name.upper() in split_line[0].upper():
                print(name)
                mod_lines.append(line)
            else:
                print(name)
                new_file.append(line)
            print("Hola")
            line = g.readline()

    if len(mod_lines) == 0:
        print("There are no valid names.")
        return True
    print("~~~~")
    for i in range(len(mod_lines)):
        print(f"{i+1}: {mod_lines[i]}")
    print("~~~~")
    while True:
        mod_index = input(
            "Enter the number of the contact you want to delete: ")
        if mod_index.isdecimal == False:
            print("Thats not a number")
            continue
        elif int(mod_index) > len(mod_lines):
            print("Bigger index than expected.")
            continue
        else:
            mod_index = int(mod_index)
            break

    for i in range(len(mod_lines)):
        if i+1 == mod_index:
            continue
        else:
            new_file.append(mod_lines[i])

    mod_item = mod_lines[mod_index-1]
    mod_item_arr = mod_item.split("|")
    print("Enter new info, press 'Enter' to keep old info")
    for i in mod_item_arr:
        count += 1
        if count == len(mod_item_arr):
            i = i[:-1]
        if "(1)" in i:
            while True:
                name = input(f"Enter new name ({i[3:]}): ")
                if len(name) == 0:
                    name = i
                    break
                elif name.isalpha() == False:
                    print("Wrong input, only letters allowed...")
                    continue
                else:
                    name = "(1)" + name
                    break
        elif "(2)" in i:
            while True:
                surname_1 = input(f"Enter new 1st surname ({i[3:]}): ")
                if len(surname_1) == 0:
                    surname_1 = i
                    break
                elif surname_1.isalpha() == False:
                    print("Wrong input, only letters allowed...")
                    continue
                else:
                    surname_1 = "(2)" + surname_1
                    break
        elif "(3)" in i:
            while True:
                surname_2 = input(f"Enter new 2nd surname ({i[3:]}): ")
                if len(surname_2) == 0:
                    surname_2 = i
                    break
                elif surname_2.isalpha() == False:
                    print("Wrong input, only letters allowed...")
                    continue
                else:
                    surname_2 = "(3)" + surname_2
                    break
        elif "(4)" in i:
            while True:
                birthday = input(f"Enter new birthday ({i[3:]}): ")
                if len(birthday) == 0:
                    birthday = i
                    break
                else:
                    format = '%Y-%m-%d'
                    try:
                        datetime.datetime.strptime(birthday, format)
                        birthday = "(4)" + birthday
                        break
                    except ValueError:
                        print("~~~~")
                        print("That date does not exist. ")
                        print("~~~~")
                        continue
        elif "(5)" in i:
            while True:
                number = input(f"Enter new phone number ({i[3:]}): ")
                if len(number) == 0:
                    number = i
                    break
                elif len(number) != 9 or not number.isdecimal():
                    print("~~~~")
                    print("Wrong phone input: Input must be 9 numbers.")
                    print("~~~~")
                    continue
                else:
                    number = "(5)" + number
                    break
        elif "(6)" in i:
            while True:
                mail = input(f"Enter new email ({i[3:]}): ")
                if len(mail) == 0:
                    mail = i
                    break
                elif mail.count("@") != 1:
                    print("~~~~")
                    print("your email must contain 1 @")
                    print("~~~~")
                    continue
                else:
                    mail = "(6)" + mail
                    break
        elif "(7)" in i:
            while True:
                relation = input(f"Enter new relation ({i[3:]}): ")
                if len(relation) == 0:
                    relation = i
                    break
                else:
                    relation = "(7)" + relation
                    break
        elif "(8)" in i:
            while True:
                extra = input(f"Enter new extra info ({i[3:]}): ")
                if len(extra) == 0:
                    extra = i
                    break
                else:
                    extra = "(8)" + extra
                    break
    mod_item = ""
    mod_item += name + "|"
    if len(surname_1) != 0:
        mod_item += (surname_1 + "|")
    if len(surname_2) != 0:
        mod_item += (surname_2 + "|")
    if len(birthday) != 0:
        mod_item += (birthday + "|")
    if len(number) != 0:
        mod_item += (number + "|")
    if len(mail) != 0:
        mod_item += (mail + "|")
    if len(relation) != 0:
        mod_item += (relation + "|")
    if len(extra) != 0:
        mod_item += (extra)
    mod_item += "\n"
    new_file.append(mod_item)
    with open(book_name, "w") as g:
        for i in new_file:
            print(new_file)
            g.write(i)
    return True


def get_info(book_name):
    decision = input(
        "What type of parameter do you want to use to search for contact \nName \nPhone Number\nEmail\n")
    print("~~~~")

    decision = decision.upper()
    dec_choice = {"NAME": 1, "PHONE NUMBER": 5, "EMAIL": 6}
    info = []
    temp = []
    count = 0
    while True:
        if decision.upper() in dec_choice.keys():
            break
        else:
            print("Wrong parameter.")
            decision = input(
                "What type of parameter do you want to use to search for contact \nName \nPhone Number\nEmail\n")
            continue

    decision = decision.lower()
    while True:
        print("~~~~")
        search = input(f"Please intro the {decision} you want to search: ")
        print("~~~~")
        if len(search) == 0:
            print("Not searching...")
            return True
        if dec_choice[decision.upper()] == 1:
            if search.isalpha() == False:
                print("Wrong name ")
                continue
        elif dec_choice[decision.upper()] == 5:
            if len(search) != 9 or search.isdecimal() == False:
                print("Wrong Number ")
                continue
        else:
            if search.count("@") != 1:
                print("Wrong email ")
                continue
        break
    val = "(" + str(dec_choice[decision.upper()]) + ")"
    with open(book_name, "r") as g:
        line = g.readline()
        while line:
            temp = line.split("|")
            for i in temp:
                if val in i and search.upper() in i.upper():
                    info.append(line)
            line = g.readline()
    if len(info) > 1:
        print("Printing more than 1 contact.")
    if len(info) == 0:
        print("There wasnt any contact that fit that search.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i in info:
        print(f"{count+1}")
        print_info_str(i)
        count += 1
    return True


def show_contact_book(book_name):
    count = 1
    with open(book_name, "r") as g:
        line = g.readline()
        while line:
            print(f"{count}. {line}")
            line = g.readline()
            count += 1
    return True


def file_error(book_name):
    if len(book_name) == 0:
        print("\nEmpty name please write something.\n")
        return False
    cap = book_name.upper()
    if cap == "QUIT" or cap == "Q":
        print("\nExiting...\n")
        exit()
    if book_name.count(".") > 1:
        print("\nThe extension of your file is wrong. Your extension should be .txt\n")
        return False
    else:
        if book_name.count(".") == 0:
            book_name += ".txt"

        name_split = book_name.split(".")

        if (name_split[1] != "txt"):
            print("\nThe extension isnt supported: Try .txt\n")
            return False
        else:
            if os.path.isfile(f"./{book_name}") == True:

                return book_name
            else:
                while True:

                    decision = input(
                        "\nThe contact book doesnt exist, do you want to create a new one? (Yes or Y) (No or N) (Quit or Q to exit)\n")
                    decision = decision.upper()
                    if decision == "QUIT" or decision == "Q":
                        print("\nExiting...\n")
                        exit()
                    elif decision == "YES" or decision == "Y":
                        open(book_name, 'a').close()
                        return book_name
                    elif decision == "NO" or decision == "N":
                        return False
                    else:
                        print("\nPlease enter a correct input.\n")


def check_action(action, book_name):
    action = action.upper()
    action = action.strip()
    decisions = {"ADD": add_to_contact_book, "A": add_to_contact_book, "DELETE": delete_from_contact_book, "DEL": delete_from_contact_book,
                 "MODIFY": modify_contact_book, "MOD": modify_contact_book, "SHOW": show_contact_book, "S": show_contact_book, "QUIT": exit, "Q": exit, "GET": get_info, "g": get_info}
    try:
        return decisions[action](book_name)
    except:
        return action


def main():
    print("Hi, welcome ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    while True:
        book_name = input(
            "Please insert the name of your contact book (Quit or Q to exit): \n")
        book_name = file_error(book_name)
        if file_error(book_name) != False:

            break

    while True:
        action = input(
            "\nWhat do you want to do: \n Add or a to add data\n Delete or del to delte data \n Modify or mod to change data \n Show or S to show contact_book\n Get or g to get info of contact \n Quit or Q to quit\n Action: ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        check = check_action(action, book_name)
        if check == "QUIT" or check == "Q":
            exit()
        elif check != True:
            print("That action does not exist try again.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


if __name__ == "__main__":
    main()
