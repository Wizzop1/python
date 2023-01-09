class Book:
    def __init__(self,book_name,book_code,book_price,book_year, book_author):
        self.book_name = book_name
        self.book_code = book_code
        self.book_price = book_price
        self.book_year = book_year
        self.book_author = book_author
    def sort_name(self,books):
        return print(self.books.sort(reversed=True))
    def author(self,books,author):
        self.author = input("Choose author: ")
        if author in self.books:
            return self.books
    def search_book(self,books,book_code):
        self.book_code = input('Choose book code: ')
        if self.book_code in self.books:
            return self.book_year
        else:
            return 'The book is not found'
books = Book(['Ivancho','Nqkoi','Vseki','Ne znam'],['500','499','498','497'],[20,15,40.5,45.9],['2000','1987','1999','1900'],['Nz','Az','Az','Nz'])
