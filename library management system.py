import pandas as pd
import csv

class Books:
    def books_data(self):
        books = {
            'Name': ["Harry Potter chamber of secrets", "harry potter and philosopher stone", "Harry Potter and the Prisoner of Azkaban", "Harry Potter and the Goblet of Fire", "Harry Potter and the Order of the Phoenix", "Harry Potter and the Deathly Hallows"],
            'Rating': ["5 Stars", "4.5 Stars", "3.9 Stars", "4.9 Stars", "5 Stars", "4.5 Stars"],
            'DOI': ["01/02/1999", "03/08/2001", "04/05/2002", "01/02/2006", "03/08/2008", "04/05/2010"]
        }
        b = pd.DataFrame(books)
        b.to_csv("booksdata.csv", index=False)
        print(b)
    
    def add_new_books(self):
        name = input("Enter Name Of Book: ")
        Rating = input("Enter Rating in stars: ")
        DOI = input("Enter DOI: ")
        with open('booksdata.csv', 'a', newline='') as bks:
            csv_writer = csv.writer(bks)
            csv_writer.writerow([name, Rating, DOI])
        print("Data added to CSV file successfully.")
    
    def remove_books(self):
        ind = int(input("Enter index you want to remove: "))
        booksdata = pd.read_csv('booksdata.csv')
        if ind >= 0 and ind < len(booksdata):
            booksdata.drop(booksdata.index[ind], inplace=True)
            booksdata.to_csv("booksdata.csv", index=False)
            print("Book removed successfully.")
            print(f"Remaining books are:\n{booksdata}")
        else:
            print("Invalid index.")

class Issuebooks(Books):
    def __init__(self):
        super().__init__()
        self.books_borrowed = []

    def issue_books(self):
        ind = int(input("Enter index of the book to borrow: "))
        booksdata = pd.read_csv('booksdata.csv')
        if ind >= 0 and ind < len(booksdata):
            borrowed_book = booksdata.iloc[ind].to_dict()
            self.books_borrowed.append(borrowed_book)
            self.remove_books()  
            booksdata = pd.DataFrame(self.books_borrowed) 
            booksdata.to_csv("borrowedbooks.csv", index=False, header=True)
            print(f"Book borrowed successfully.\n {booksdata}")
        else:
            print("Invalid index.")

class Admin(Issuebooks):  
    def admins_data(self):  
        admin = {
            'Name': ["Harry", "Potter", "Humera"],
            'Gmail': ["harry@gmail.com", "Potter@gmail.com", "Humera@gmail.com"],
            'DOB': ["01/02/1999", "03/08/2001", "01/02/2000"]
        }
        adm = pd.DataFrame(admin)
        
        print(adm)
        adm.to_csv("adminsdata.csv", index=False)

    def admin_login(self):  
        inpt1 = input("Enter your Name: ")
        if inpt1 == "Harry":
            print("Welcome Harry")
            self.func2bprfmd() 
        elif inpt1 == "Potter":
            print("Welcome Potter")
            self.func2bprfmd()  
        elif inpt1 == "Humera":
            print("Welcome Humera")
            self.func2bprfmd()  

    def func2bprfmd(self):
        ipt = int(input("""What function do you want to perform? 
                         1) Show books data
                         2) Add books
                         3) Remove books
                         4) Issue books
                         Enter the corresponding number: """))
        if ipt == 1:
            userch = input("Do you want to show the list of books? y/n: ")
            if userch.lower() == 'y':
                self.books_data()  
            else:
                print(" ")
        elif ipt == 2:
            userch1 = input("Do you want to add books? y/n: ")
            if userch1.lower() == 'y':
                self.add_new_books()  
            else:
                print(" ")
        elif ipt == 3:
            userch1 = input("Do you want to remove books? y/n: ")
            if userch1.lower() == 'y':
                self.remove_books() 
            else:
                print(" ")
        elif ipt == 4:
            userch1 = input("Do you want to issue books? y/n: ")
            if userch1.lower() == 'y':
                self.issue_books()  
            else:
                print(" ")

        inpt2 = input("Do you want to proceed further? y/n:")
        if inpt2 == 'y':
            self.func2bprfmd()
        elif inpt2 == 'n':
            exit

ob1 = Books()
ob2 = Issuebooks()
ob3 = Admin()
ob3.admins_data()  
ob3.admin_login()
