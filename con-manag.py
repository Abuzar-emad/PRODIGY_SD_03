#("Simple Contacts Managment System")
import os

file_con = 'data.txt'

def load_con():
    con_info = {}
    if os.path.exists(file_con):
        with open(file_con, 'r') as file:
            for line in file:
                name, pnum, email = line.strip().split(',')
                con_info[name] = {'pnum': pnum, 'email': email}
    return con_info

def save_con(con_info):
    with open(file_con, 'w') as file:
        for name, value in con_info.items():
            file.write(f"{name},{value['pnum']},{value['email']}\n")

def add_contacts(con_info):
    name = input("Please Enter Name: ").strip()
    pnum = input("Please Enter Phone number: ").strip()
    email = input("Please Enter Email: ").strip()
    if name in con_info:
        print("This contact already exists")
    else:
        con_info[name] = {'pnum': pnum, 'email': email}
        save_con(con_info)
        print("Contact added")

def print_contacts(name, value):
    return f"\nName: {name}\nPhone: {value['pnum']}\nEmail: {value['email']}"

def view_con(con_info):
    if not con_info:
        print("There are no contacts to display")
    else:
        for name, value in con_info.items():
            print(print_contacts(name, value))

def edit_contacts(con_info):
    view_con(con_info)
    if not con_info:
        return
    else:
        name = input("Enter name of contact to edit: ").strip()
        if name in con_info:
            phone = input("Enter new phone number: ").strip()
            mail = input("Enter new email: ").strip()
            con_info[name]['pnum'] = phone
            con_info[name]['email'] = mail
            save_con(con_info)
            print(f"Contact \"{name}\" updated")
        else:
            print("Contacts not found")

def del_con(con_info):
    view_con(con_info)
    if not con_info:
        return
    else:
        name = input("Enter name of contact to delete: ").strip()
        if name in con_info:
            del con_info[name]
            save_con(con_info)
            print(f"Contact \"{name}\" deleted")
        else:
            print("No Such Contacts")

def main():
    con_info = load_con()
    while True:
        print("\nPlease enter your option:")
        print("1. Add new contact")
        print("2. View contacts list")
        print("3. Edit contacts")
        print("4. Delete contacts")
        print("5. Exite")
        
        option = input("Enter your choice: ")
        if option == '1':
            add_contacts(con_info)
        elif option == '2':
            view_con(con_info)
        elif option == '3':
            edit_contacts(con_info)
        elif option == '4':
            del_con(con_info)
        elif option == '5':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
