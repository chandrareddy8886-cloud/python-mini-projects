class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show_book(self):
        print(f"Title : {self.title}\nAuthor : {self.author}\n")


book1 = Book("Atomic Habits", "James Clear")
book2 = Book("The Alchemist", "Paulo Coelho")
book3 = Book("Rich Dad Poor Dad", "Robert Kiyosaki")
books = [book1, book2, book3]
for i in books:
    i.show_book()
