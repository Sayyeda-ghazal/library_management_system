import pandas as pd
books = {
            'Name': ["Harry Potter chamber of secrets", "harry potter and philosopher stone", "Harry Potter and the Prisoner of Azkaban", "Harry Potter and the Goblet of Fire", "Harry Potter and the Order of the Phoenix", "Harry Potter and the Deathly Hallows"],
            'Rating': ["5 Stars", "4.5 Stars", "3.9 Stars", "4.9 Stars", "5 Stars", "4.5 Stars"],
            'DOI': ["01/02/1999", "03/08/2001", "04/05/2002", "01/02/2006", "03/08/2008", "04/05/2010"]
        }
b = pd.DataFrame(books)
b.to_csv("booksdata.csv", index=False)
    