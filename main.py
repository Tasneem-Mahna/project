class Client:
    def __init__(self, full_name, age , id, id_no, phone_num):
        self.full_name = full_name
        self.age = age
        self.id = id
        self.id_no = id_no
        self.phone_num = phone_num

class Librarian:
    def __init__(self, full_name, age, id, id_no, emp_type):
        self.full_name = full_name
        self.age = age
        self.id = id
        self.id_no = id_no
        self.emp_type = emp_type


    def get_id_no(self):
       return self.id_no

    def borrow_book(self):
        while(True):
            name_book = input("choose the book to borrow it (C++, JAVA, Electronics )")
            if name_book.Book.get_status() is "Active":
               id_number= input("enter the id number :")
            if Book.get_status() is id_number:
               borrow_orderd = []
               borrow_orderd.append(id_number, name_book)

            else :
                print("The id_number is not exist")
        else:
            print("The  book is not active")

class Book:

    def __init__(self, title , id,auther, status, diescription):
        self.title = title
        self.id = id
        self.auther = auther
        self.status = status
        self.diescription = diescription

    def get_status(self):
         return self.status

    def get_id_no(self):
         return self.id_no
list_client =[]
list_client.append(Client("98", "Tasneem Mhana", 18, "8754", "05934567809"))
for E in list_client:
    print(E.id, E.full_name, E.age, E.id_no, E.phone_num)


list_librarian = []
list_librarian.append(Librarian("98", "Tasneem mhana", "18", "part"))
for A in list_librarian:
    print(A.id, A.full_name, A.age, A.id_no, A.emp_type)


list_book=[]
list_book.append(Book("1", "C++", "The book contains about the C++ language ", "Active"))
list_book.append(Book("2", "JAVA", "The book contains about the JAVA language ",  "Inactive"))
list_book.append(Book("3", "Electronics", "The book contains important information on Physics", "Active"))

total_borrowed_books = 0
total_available_books = 0
total_borrowed_orders = 0


#tasneem

