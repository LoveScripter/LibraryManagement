class library:
    def __init__(self,listofBooks):
        self.books=listofBooks

    def displayAvailabelBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print(" *"+book)
    def borrowBook(self,bookname):
        if bookname in self.books:
            print(f"You have been issued {bookname}, Please keep it safe and returned it within 30 dayes")
            self.books.remove(bookname)
            return True
        else:
            print("sorry, this book is already is issued to someone else,Please wait  until the book get free")
            return False
        
    def returnbook(self,bookname):
        self.books.appened(bookname)
        print("Thanks for returning it! Hope you enjoyed it...")

    
class Student:
    def requestBook(self):
        self.book=input("Enter the name of book you want: \n")
        return self.book

    
    def returnBook(self):
        self.book=input("Enter the name of book you want to return: \n")
        return self.book


if __name__=='__main__':
        centraLibrary=library(["python","Django","js","c++"])
        centraLibrary.displayAvailabelBooks()
        student = Student()
        
        while(True):
            welcomeMsg='''====Welcome to Central Library====
            Please choose an option
            1. List all the books
            2. Request the book
            3. Add/Return the book
            4. exit the library
            '''
            print(welcomeMsg)
            choice=int(input("Enter a choice: "))
            if choice==1:
                centraLibrary.displayAvailabelBooks()
            elif choice==2:
                centraLibrary.borrowBook(student.requestBook())
            elif choice==3:
                centraLibrary.returnbook(student.returnBook())
            elif choice==4:
                print("Thnaks for choosing Central Library.Have a great day ahead!")
                exit()
            else:
                print("Invalid choice!")
         
            





