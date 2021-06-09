import json
import logging
import sys
from logging.handlers import TimedRotatingFileHandler

#class for node
class node():
    def __init__(self,data=None):
        self.data= data
        self.next=None

#class for book
class book():
    def __init__(self,book_id,book_name,book_author):
        self.book_id=book_id
        self.book_name=book_name
        self.book_author=book_author
        self.book_status='Not Assigned'
        self.booked_against=None




#class for insert,update,delete,etc
class operation(book):

    def __init__(self):
        self.head = None

    def insert_book(self,book_id,book_name,book_author):
        new_book = book(book_id, book_name, book_author)
        if self.head is None:
            self.head=node(new_book)
        else:
            tmp=self.head
            while tmp.next is not None:
                tmp=tmp.next
            tmp.next = node(new_book)
        print("Book with id ",book_id," is inserted!")

    def show_book(self):
        if self.head is None:
            print("No Book To Display Information")
        else:
            tmp=self.head
            list_of_book=[]
            while tmp is not None:
                tmp_dic = {}
                data=tmp.data
                tmp_dic['book_id'] = data.book_id
                tmp_dic['book_name'] = data.book_name
                tmp_dic['book_author'] = data.book_author
                tmp_dic['book_status'] = data.book_status
                tmp_dic['booked_against'] = data.booked_against

                list_of_book.append(tmp_dic)
                tmp= tmp.next
            print("BOOK DETAILS:")
            print(json.dumps(list_of_book, indent = 1))

    def delete_book(self,book_id):
        found = False
        if self.head is None:
            print("No Book To Delete")
            found = False
        else:
            tmp=self.head
            if tmp.data.book_id == book_id:
                print("BOOK FOUND")
                found = True
                li=[]
                tmp_dic = {}
                data = tmp.data
                tmp_dic['book_id'] = data.book_id
                tmp_dic['book_name'] = data.book_name
                tmp_dic['book_author'] = data.book_author
                tmp_dic['book_status'] = data.book_status
                tmp_dic['booked_against'] = data.booked_against
                li.append(tmp_dic)
                print("BOOK DETAILS:")
                print(json.dumps(li,indent=1))
                print("DELETING ABOVE DETAILS")
                self.head=tmp.next
                del tmp
            else:
                previous=tmp
                tmp=tmp.next
                while tmp is not None:
                    if tmp.data.book_id == book_id:
                        print("BOOK FOUND")
                        found = True
                        li=[]
                        tmp_dic = {}
                        data = tmp.data
                        tmp_dic['book_id'] = data.book_id
                        tmp_dic['book_name'] = data.book_name
                        tmp_dic['book_author'] = data.book_author
                        tmp_dic['book_status'] = data.book_status
                        tmp_dic['booked_against'] = data.booked_against
                        li.append(tmp_dic)
                        print("BOOK DETAILS:")
                        print(json.dumps(li, indent=1))
                        print("DELETING ABOVE DETAILS")
                        previous.next=tmp.next
                        tmp.next=None
                        del tmp
                        break
                    previous=tmp
                    tmp=tmp.next

        if not found:
            print("BOOK NOT FOUND")

    def update_status(self,book_id,book_status,stu_name=None):
        tmp=self.head
        found= False
        while tmp is not None:
            if tmp.data.book_id == book_id:
                print("Book ID found..! Changing status to "+ str(book_status))
                tmp.data.book_status=book_status
                tmp.data.booked_against =stu_name
                print("BOOK_STATUS changes successfully!")
                found=True
                break
            tmp=tmp.next

        if not found:
            print("BOOK NOT FOUND")




if __name__ == '__main__':
    try:

        log_file =  "BOOK.log"
        logger = logging.getLogger("Rotating Log")
        severity = 'DEBUG'
        logger.setLevel(logging.INFO)
        handler = TimedRotatingFileHandler(log_file,
                                           when="h",
                                           interval=12)
        fileformatter = logging.Formatter('%(asctime)s %(levelname)-4s %(message)s')
        handler.setFormatter(fileformatter)
        logger.addHandler(handler)
        ob1 = operation()
        condition = True
        while condition is True:
            print("==============================================")
            print("Make Selection")
            print("Enter 1 for Librarian")
            print("Enter 2 for Student")
            print("Enter 3 for Exit")
            choice= int(input("Enter your choice: "))
            while choice  == 1:
                print("==============================================")
                print("Welcome Librarian")
                print("Make Selection")
                print("Enter 1 to add new book")
                print("Enter 2 to display all book")
                print("Enter 3 to delete a book")
                print("Enter 4 to update the status of book")
                print("Enter 0 to go back to main menu")
                lib_choice = int(input("Enter your choice: "))
                if lib_choice == 1:
                    print("==============================================")
                    book_id     =   int(input("Enter book_id(Interger value)1(Interger value): "))
                    book_name   =   (input("Enter book_name: "))
                    book_author =   (input("Enter book_author: "))
                    ob1.insert_book(book_id,book_name,book_author)
                    print("==============================================")

                if lib_choice == 2:
                    print("==============================================")
                    ob1.show_book()
                    print("==============================================")
                if lib_choice == 3:
                    print("==============================================")
                    book_id = int(input("Enter book_id(Interger value): "))
                    ob1.delete_book(book_id)
                    print("==============================================")
                if lib_choice == 4:
                    print("==============================================")
                    book_id = int(input("Enter book_id(Interger value): "))
                    book_status = (input("Enter book_status(Assigned/Not Assigned): "))
                    if book_status in ['Assigned','Not Assigned']:
                        ob1.update_status(book_id,book_status)
                    else:
                        print("Status is not apprpriate. Try Again")
                    print("==============================================")
                if lib_choice == 0:
                    choice = 0

            while choice  == 2:
                print("==============================================")
                print("Welcome Student")
                print("Make Selection")
                print("Enter 1 to display all book")
                print("Enter 2 to book books")
                print("Enter 0 to go back to main menu")
                stu_choice = int(input("Enter your choice: "))
                if stu_choice == 1:
                    print("==============================================")
                    ob1.show_book()
                    print("==============================================")
                elif stu_choice == 2:
                    print("==============================================")
                    book_id = int(input("Enter the book_id: "))
                    book_name = input("Enter the book_name: ")
                    stu_name = input("Enter your name: ")
                    ob1.update_status(book_id,'Assigned',stu_name)
                    print("==============================================")
                elif stu_choice == 0:
                    choice =0

            if choice == 3:
                condition =False


    except:
        logger.error(str(sys.exc_info()[1]))











