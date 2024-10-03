lst = ['hi', 'this', 'is', 'jojo']
with open(r"D:\Example\writelines_in_a_file.txt","a+") as f:
    for i in lst:
        f.writelines(f"{i} ")
        
f.close()

'''
class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def __str__(self):
        return (f"\nTitle: {self.title}\nAuthor: {self.author}\n\
Year: {self.year}\n")
    
class Library(Book):
    books = []
    def __init__(self):
        pass

    def add_book(self, obj):
        Library.books.append(obj)
    def view_all_books(self):
        for book in Library.books:
            print(book)
    def search_book(self, title):
        for book in Library.books:
            if book.title == title:
                print(book)

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book by Title")
        print("4. Exit")
        choice = int(input("Enter your choice (1-4): "))
        
        if choice == 1:
            name = input("Enter name: ")
            author = input("Enter type: ")
            yr = int(input("Enter initial bal: "))
            b = Book(name, author, yr)
            l = Library()
            l.add_book(b)
        if choice == 2:
            l = Library()
            l.view_all_books()
        if choice == 3:
            title = input("Enter the book title: ")
            l = Library()
            l.search_book(title)
        if choice == 4:
            break

main()
'''