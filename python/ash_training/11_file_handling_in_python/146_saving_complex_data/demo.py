def save_user_data():
    name = input("enter name: ")
    email = input('enter email: ')
    contact = input('enter contact: ')

    user_data = f"Name: {name}\nEmail: {email}\nContact: {contact}\n"


    with open('user_data.txt', 'a') as file:
        file.write(user_data)


def read_user_data():
    with open('user_data.txt', 'r') as file:
        print(file.read())



read_user_data()