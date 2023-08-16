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
            booksdata = self.remove_books()
            if booksdata is not None:
                booksdata.to_csv("booksdata.csv", index=False)
                borrowed_books_df = pd.DataFrame(self.books_borrowed)
                borrowed_books_df.to_csv("borrowedbooks.csv", index=False, header=True)
                print(f"Book borrowed successfully. \n {borrowed_books_df}")
        else:
            print("Invalid index.")
        
ob1 = Books()
ob2 = Issuebooks()

ipt = int(input("""What function do you want to perform? 
                 1) Show books data
                 2) Add books
                 3) Remove books
                 4) Issue books
                 Enter the corresponding number: """))

if ipt == 1:
    userch = input("Do you want to show the list of books? y/n: ")
    if userch.lower() == 'y':
        ob1.books_data()
    else:
        print(" ")
 
elif ipt == 2:
    userch1 = input("Do you want to add books? y/n: ")
    if userch1.lower() == 'y':
        ob1.add_new_books()
    else:
        print(" ")

elif ipt == 3:
    userch1 = input("Do you want to remove books? y/n: ")
    if userch1.lower() == 'y':
        ob1.remove_books()
    else:
        print(" ")

elif ipt == 4:
    userch1 = input("Do you want to issue books? y/n: ")
    if userch1.lower() == 'y':
        ob2.issue_books()
    else:
        print(" ")
