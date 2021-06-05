import json, time
def books():
    with open("books.json",'r') as f:
        books = json.load(f)
        return books

class Admin:
    def __init__(self, ids, name):
        if ids != "admin":
            print("Cannot Log you as Admin")
            raise InterruptedError("Wrong Admin Id")
        print("Successfully logged you as Admin")
        self.name = name

    def borrow_books(self, borrow):
        book = books()
        if borrow in book["books"]:
            book["books"].remove(borrow)
            book["admin_borrowed"].append(borrow)
            with open("books.json", 'w') as f:
                json.dump(book, f, indent=2)
            print(f"{self.name} successfully borrowed our book.\nPlease return book in time.")
        else:
            print(f"{self.name} that book isn't in the library, pleas try installing it")

    @staticmethod
    def book_list():
        print("===Books in our Library===")
        for i, book in enumerate(books()["books"]):
            print(i+1, book)

    def install_books(self, book):
        with open("books.json", 'r') as f:
            total = json.load(f)
            total = total["books"]
            total.append(book)
        with open("books.json", "w") as f:
            json.dump(total, f, indent=2)
            print(f"Thanks {self.name} for installing new books.")

    def return_books(self,book):
        with open("books.json",'r') as f:
            data = json.load(f)
        if book in data["admin_borrowed"]:
            with open("books.json", 'w') as f:
                data["admin_borrowed"].remove(book)
                data['books'].append(book)
                json.dump(data, f, indent=2)
            print(f"Thanks {self.name} for returning the book.")
        else:
            print("You haven't taken this book.")

    @staticmethod
    def borrowed_books():
        book = books()
        print("===Books Borrowed by Guests===")
        for i, n in enumerate(book["guest_borrowed"]):
            print(i + 1, n)
        print("===Books Borrowed by Admins===")
        for i, n in enumerate(book["admin_borrowed"]):
            print(i + 1, n)

    @staticmethod
    def help():
        print("===HELP MENU===\n1 to View Book List\n2 to Borrow Books\n3 to return Book\n4 to install new books\n5 to check borrowed books\n6 to exit")

class Guest:
    def __init__(self, name):
        self.name = name

    def borrow_books(self, borrow):
        book = books()
        if borrow in book["books"]:
            book["books"].remove(borrow)
            book["guest_borrowed"].append(borrow)
            with open("books.json",'w') as f:
                json.dump(book, f, indent=2)
            print(f"{self.name} thanks for borrowing our book.\nPlease return book in time.\nHave a nice time with it.")
        else:
            print(f"{self.name} that book isn't in the library sorry.")

    @staticmethod
    def book_list():
        print("===Books in our Library===")
        book = books()
        for i, book in enumerate(book["books"]):
            print(i+1, book)

    def return_books(self, book):
        with open("books.json", 'r') as f:
            data = json.load(f)
        if book in data["guest_borrowed"]:
            with open("books.json", 'w') as f:
                data["guest_borrowed"].remove(book)
                data['books'].append(book)
                json.dump(data, f, indent=2)
            print(f"Thanks {self.name} for returning the book.")
        else:
            print("You haven't taken this book.")

    @staticmethod
    def borrowed_books():
        book = books()
        print("===Books Borrowed by Guests===")
        for i,n in enumerate(book["guest_borrowed"]):
            print(i+1, n)

    @staticmethod
    def help():
        print(
            "===HELP MENU===\n1 to View Book List\n2 to Borrow Books\n3 to return Book\n4 to see borrowed books\n5 to check borrowed books\n6 to exit")

global admin, guest
print("=====Welcome to Oxford Library=====")
print("Please kindly log in to start using it.")
print("How would you like to login :\nAdministrator(a) or Guest(g)")
admin_login = False
guest_login = False
global name
while True:
    if admin_login is True or guest_login is True:
        break
    data = input(">")
    data.lower()
    if data == "administrator" or data == "a":
        admin_login = True
        password = input("Enter Admin ID to Enter.\nADMIN ID : ")
        password.lower()
        name = input("Enter your name : ")
        print(f"Logging you as admin with {name} name..")
        admin = Admin(password, name)

    elif data == "guest" or data == "g":
        guest_login = True
        name = input("Enter you name to login.\n")
        guest = Guest(name)
        print("You logged in as Guest")
    else:
        print("Please Enter a Valid option.")

while True:
    time.sleep(1)
    a = input("What do you wanna do ?\nType 'help' to get help menu.\n")
    if admin_login:
        if a == "1":
            admin.book_list()
        elif a == "2":
            b = input("Which book you want to borrow ?\n")
            b = b.capitalize()
            admin.borrow_books(b)
        elif a == "3":
            b = input("Which book you want to return ?\n")
            b = b.capitalize()
            admin.return_books(b)
        elif a == "4":
            b = input("Which book you want to install ?\n")
            b = b.capitalize()
            admin.install_books(b)
        elif a.lower() == "help":
            admin.help()
        elif a == "5":
            admin.borrowed_books()
        elif a == "6":
            print("Thanks for using Oxford Library.")
            break
        else:
            print("Please give a valid input")
    elif guest_login :
        if a == "1":
            guest.book_list()
        elif a == "2":
            b = input("Which book you want to borrow ?\n")
            b = b.capitalize()
            guest.borrow_books(b)
        elif a == "3":
            b = input("Which book you want to return ?\n")
            b = b.capitalize()
            guest.return_books(b)
        elif a.lower() == "help":
            guest.help()
        elif a == "4":
            guest.borrowed_books()
        elif a == "5":
            print("Thanks for using Oxford Library.")
            break
        else:
            print("Please give a valid input")
