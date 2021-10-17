
# Library Management System

# Nouns, Verbs, adjectives


class LMS():

    library_list = ["Positions", "Attraction", "Health", "Fun", "Boxing", "LBG"]
    def __init__(self,customer_name) -> None:
        print("Welcome to Library Management System")
        print(f"In this library available books are: {LMS.library_list}" )
        self.customer_name = customer_name
        self.customer_list = []

    @staticmethod
    def display_library_list():
        print(LMS.library_list)

    
    def customer_borrow_book(self,book_name):
        if book_name in LMS.library_list:
            LMS.library_list.remove(book_name)
            self.customer_list.append(book_name)


        else:
            print("Book is not available")

        print(self.customer_list)

    def customer_return_book(self,book_name):
        LMS.library_list.append(book_name)
    
    

c1 = LMS("goutham")
c1.customer_borrow_book("Fun")
c1.display_library_list()

c2 = LMS("tamanna")      
