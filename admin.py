import pandas as pd
import csv

admin = {
            'Name': ["Harry", "Potter", "Humera"],
            'Gmail': ["harry@gmail.com", "Potter@gmail.com", "Humera@gmail.com"],
            'DOB': ["01/02/1999", "03/08/2001", "01/02/2000"]
        }
adm = pd.DataFrame(admin)
print(adm)
adm.to_csv("adminsdata.csv", index=False)


inpt1 = input("Enter your Name: ")
if inpt1 == "Harry":
    print("Welcome Harry")
elif inpt1 == "Potter":
    print("Welcome Potter")
elif inpt1 == "Humera":
    print("Welcome Humera")
        

