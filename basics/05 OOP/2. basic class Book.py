class Book:
    def __init__(self, author, title="unknown", isbn="unknown", year="unknown"):
        self.author = author
        self.title = title
        self.isbn = isbn
        self.year = year

    def printData(self):
        print(self.author, self.title, self.isbn, self.year)

book1 = Book("Lucy Maud Montgomery", "Ania z Zielonego Wzgórza", "9788375174700", 2024)
book1.printData()

book2 = Book("Adam", year = 2010)
book2.printData()