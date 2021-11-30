import os
import datetime
# Falta hacer que compruebe si el registro ya está en el contact book.


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
            print("This needs to be an alphabetic field")

    while True:
        contact.surname = input("Introduce first surname: ")
        if len(contact.surname) == 0 or contact.surname.isalpha():
            break
        else:
            print("This needs to be an alphabetic field")

    while True:
        contact.surname_2 = input("Introduce second surname: ")
        if len(contact.surname_2) == 0 or contact.surname_2.isalpha():
            break
        else:
            print("This needs to be an alphabetic field")

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
                print("That date does not exist. ")
                continue

    while True:
        contact.phone_number = input("Please write the phone number: ")
        if len(contact.phone_number) != 0:
            if len(contact.phone_number) != 9 or not contact.phone_number.isdecimal():
                print("Wrong phone input: Input must be 9 numbers.")
                contact.phone_number = ""
                continue

        while True:
            contact.email = input("Please write the email: ")
            if len(contact.email) != 0 and contact.email.count("@") != 1:
                print("Wrong form of email: It must contain an @ character ")
                contact.email = ""
            else:
                break

        if len(contact.email) == 0 and len(contact.phone_number) == 0:
            print("You have to enter either a phone number or an email.")
            continue
        else:
            break

    contact.relation = input("What is your relation with the contact: ")
    contact.extra = input("Write any extra info: ")
    contact.create_info()

    if contact_book_has_contact(book_name, contact.info) == True:
        f.close()
        contact.clean_class()
        return True

    print("Do you want to add this info to your contact book?")
    contact.info = contact.info
    contact.print_info()
    decision = input(
        "Write 'No' or 'N' to delete info, Enter to add: ").upper()

    if decision == "NO" or decision == "N":
        f.close()
        contact.clean_class()
        return True

    else:
        print("Adding contact...")
        f.write(contact.info)
        f.close()

    return True


def delete_from_contact_book(book_name):
    return True


def modify_contact_book(book_name):
    return True


def get_info(book_name):
    return True


def show_contact_book(book_name):
    f = open(book_name, "r")
    print(
        f"This is your contact book:\n\n\n ###########################################\n{f.read()}\n###########################################\n\n")
    f.close()
    return True


def file_error(book_name):
    if len(book_name) == 0:
        print("\nEmpty name please write something.\n")
        return False
    cap = book_name.upper()
    if cap == "QUIT" or cap == "Q":
        print("\nExiting...\n")
        exit()
    if book_name.count(".") != 1:
        print("\nThe extension of your file is wrong. Your extension should be .txt\n")
        return False
    else:
        name_split = book_name.split(".")
        if (name_split[1] != "txt"):
            print("\nThe extension isnt supported: Try .txt\n")
            return False
        else:
            if os.path.isfile(f"./{book_name}") == True:
                return True
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
                        return True
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

    while True:
        book_name = input(
            "\nPlease insert the name of your contact book (with file extension) (Quit or Q to exit): \n")

        if file_error(book_name) == True:
            break
    while True:
        action = input(
            "\nWhat do you want to do: \n (Add or a to add data)\n (Delete or del to delte data) \n (Modify or mod to change data) \n (Show or S to show contact_book)\n (Get or g to get info of contact) \n(Quit or Q to quit)\n Action: ")

        if check_action(action, book_name) == "QUIT" or check_action(action, book_name) == "Q":
            exit()
        else:
            print("That action does not exist try again.")


if __name__ == "__main__":
    main()
