class User:

    def __init__(self, list_size, first_name, last_name, age, id_no, phone_number):
        self.id = str(list_size + 1)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.id_no = id_no
        self.phone_number = phone_number

    def get_user(self):
        return {self.id: [self.first_name, self.last_name, self.age, self.id_no, self.phone_number]
                }


class Librarian(User):

    def __init__(self, list_size, first_name, last_name, age, id_no, phone_number, salary= 0):
        super().__init__(list_size, first_name, last_name, age, id_no, phone_number)

        self.salary = float(salary)

    def get_librarian(self):
        return {self.id: [self.last_name, self.first_name, self.age, self.id_no, self.phone_number, self.salary]
                }


class Book:

    def __init__(self, list_size, title, description, author):
        self.id = str(list_size + 1)
        self.title = title
        self.description = description
        self.author = author
        self.status = "Active"

    def get_book_details(self):
        return {self.id: [self.title, self.description, self.author, self.status]}

    def get_status(self):
        return self.status


import datetime

class BorrowingOrder:

    def __init__(self, list_size, days, book_id, client_id):
        self.id = str(list_size + 1)
        self.start_date = datetime.datetime.now()
        self.days = days
        self.end_date = self.start_date + datetime.timedelta(days=days)
        self.book_id = book_id
        self.client_id = client_id
        self.status = "Ordered"

    def get_orders_details(self):
        return {self.id: [self.days, self.book_id, self.client_id, self.status]}

    def get_status(self):
        return self.status


    def set_status(self):
        if self.end_date >= datetime.datetime.now():
            self.status = "Active"
        elif self.end_date < datetime.datetime.now():
            self.status = "Expired"
        else:
            self.status = "Canceled"
            return self.status


users_list = {'1': ['Mustafa', 'Redwan', 30, '800000071', '0592663635'],
              '2': ['Mohaned', 'Mohammed', 20, '800000071', '0592000000'],
              '3': ['Mohaned', 'Said', 25, '800000072', '0592000001']}
books_list = {'1': ['Our Class is a Family',
                    'Teachers do so much more than just teach academics. They build a sense of community within their classrooms, creating a home away from home where they make their students feel safe, included, and loved.',
                    'Shannon Olsen ', 'Active'], '2': ['Our Class is a Family',
                                                       'Teachers do so much more than just teach academics. They build a sense of community within their classrooms, creating a home away from home where they make their students feel safe, included, and loved.',
                                                       'Shannon Olsen ', 'Active'],
              '2': ['A Letter From Your Teacher: On the First Day of School',
                    'rom the author and illustrator of Our Class is a Family, this heartwarming picture book helps teachers in welcoming their new group of students on the first day of school. Through a letter written from the teacher’s point of view, students are given the message that their new teacher is someone they will get to form a special bond with. Their teacher is not only there to help them academically, but also to cheer them on, and to provide a caring, safe environment for them to learn and grow. ',
                    'Shannon Olsen', 'Active'], '1': ['Our Class is a Family',
                                                      'Teachers do so much more than just teach academics. They build a sense of community within their classrooms, creating a home away from home where they make their students feel safe, included, and loved.',
                                                      'Shannon Olsen ', 'Active'],
              '3': ['A Letter From Your Teacher: On the First Day of School',
                    'rom the author and illustrator of Our Class is a Family, this heartwarming picture book helps teachers in welcoming their new group of students on the first day of school. Through a letter written from the teacher’s point of view, students are given the message that their new teacher is someone they will get to form a special bond with. Their teacher is not only there to help them academically, but also to cheer them on, and to provide a caring, safe environment for them to learn and grow. ',
                    'Shannon Olsen', 'Active'], '3': ["I'm Glad My Mom Died ",
                                                      'A heartbreaking and hilarious memoir by iCarly and Sam & Cat star Jennette McCurdy about her struggles as a former child actor—including eating disorders, addiction, and a complicated relationship with her overbearing mother—and how she retook control of her life.',
                                                      'Jennette McCurdy ', 'Active'], '1': ['Our Class is a Family',
                                                                                            'Teachers do so much more than just teach academics. They build a sense of community within their classrooms, creating a home away from home where they make their students feel safe, included, and loved.',
                                                                                            'Shannon Olsen ', 'Active'],
              '2': ['A Letter From Your Teacher: On the First Day of School',
                    'rom the author and illustrator of Our Class is a Family, this heartwarming picture book helps teachers in welcoming their new group of students on the first day of school. Through a letter written from the teacher’s point of view, students are given the message that their new teacher is someone they will get to form a special bond with. Their teacher is not only there to help them academically, but also to cheer them on, and to provide a caring, safe environment for them to learn and grow. ',
                    'Shannon Olsen', 'Active'], '4': ["I'm Glad My Mom Died ",
                                                      'A heartbreaking and hilarious memoir by iCarly and Sam & Cat star Jennette McCurdy about her struggles as a former child actor—including eating disorders, addiction, and a complicated relationship with her overbearing mother—and how she retook control of her life.',
                                                      'Jennette McCurdy ', 'Active'],
              '4': ['The Body Keeps the Score: Brain, Mind, and Body in the Healing of Trauma ',
                    'Essential reading for anyone interested in understanding and treating traumatic stress and the scope of its impact on society.” —Alexander McFarlane, Director of the Centre for Traumatic Stress Studies',
                    'Bessel van der Kolk M.D.', 'Active']}
orders_list = {}
Librarian_list = {}
inactive_list = []  # list of inactive book's id.

print (60 * "*", "Welcome to Palestine Liberary",60 * "*")

while True:
    t = int(input("Enter\n1. Add User \n2. Add Book\n3. Add Librarian\n4. Create Order\n5. Browse Books\n6. Return_Books \n7. Exit\n:"))
    if t == 1:
        first_name = input("Enter Your First Name: ")
        last_name = input("Enter Your Last Name: ")
        age = int(input("Enter Your Age: "))
        phone_number = input("Phone Number: ")
        id_no = input("Enter Your ID NO.: ")

        user = User(list_size=len(users_list), first_name=first_name, last_name=last_name, age=age,
                    phone_number=phone_number, id_no=id_no)
        user.get_user()
        users_list.update(user.get_user())
        print("User has been added Successfully")
        print(users_list)

    elif t == 2:
        title = input("Enter book's title: ")
        description = input("Enter Book's Description: ")
        author = input("Enter Book's Author: ")

        book = Book(list_size=len(books_list), title=title, description=description, author=author)
        book.get_book_details()
        books_list.update(book.get_book_details())
        print("Book has been added Successfully")
        print(books_list)

    elif t == 3:
        first_name = input("Enter Your First Name: ")
        last_name = input("Enter Your Last Name: ")
        age = int(input("Enter Your Age: "))
        phone_number = input("Phone Number: ")
        id_no = input("Enter Your ID NO.: ")
        salary = input("Enter Your Salary: ")

        librarian = Librarian(list_size=len(Librarian_list), first_name=first_name, last_name=last_name, age=age,phone_number=phone_number, id_no=id_no, salary= salary)
        librarian.get_librarian()
        Librarian_list.update(librarian.get_librarian())
        print("Librarian has been added Successfully\n")

    elif t == 4:
        user_id = input("Enter Your User ID: ")
        is_exist = False
        user_id_list = []

        user_id_list= list(users_list.keys())

        if len(user_id_list) <= 0:
            print("Please Fill the Following Info...\n")

            first_name = input("Enter Your First Name: ")
            last_name = input("Enter Your Last Name: ")
            age = int(input("Enter Your Age: "))
            phone_number = input("Phone Number: ")
            id_no = input("Enter Your ID NO.: ")
            user = User(list_size=len(users_list), first_name=first_name, last_name=last_name, age=age,
                        phone_number=phone_number, id_no=id_no)

            user.get_user()
            users_list.update(user.get_user())
            print("User has been added Successfully")
            print(users_list)
        else:
            for i in user_id_list:

                if user_id == i:
                    is_exist = True
                    break

                if user_id not in user_id_list:
                    first_name = input("Enter Your First Name: ")
                    last_name = input("Enter Your Last Name: ")
                    age = int(input("Enter Your Age: "))
                    phone_number = input("Phone Number: ")
                    id_no = input("Enter Your ID NO.: ")
                    user = User(list_size=len(users_list), first_name=first_name, last_name=last_name, age=age,
                                phone_number=phone_number, id_no=id_no)

                    user.get_user()
                    users_list.update(user.get_user())
                    print("User has been added Successfully")
                    break

        # Check the availabilty of book's id in books list.
        book_id = input("Enter book ID: ")
        is_there = False
        active_list = []  # list of active book's id.

        books_list_1 = list(books_list.keys())
        print("The availble books id in library are:",books_list_1)

        if len(books_list_1) <= 0:
            print("Sorry, No books are availble!!!")
            break
        else:
            for j in books_list_1:
                if j == book_id:
                    is_there = True
                    print("Success")
                    while True:
                        if book_id in inactive_list:
                            print("This book was borrowed\n Please choose another book!")
                            book_id = input("Enter book ID: ")
                        else:
                            break
                elif book_id not in books_list_1:
                    print("Enter a valid Book ID !!!\n")
                    book_id = input("Enter book ID: ")
                    break

            days = int(input("Enter Number of borrowing days: "))
            book_order = BorrowingOrder(list_size=len(orders_list), days=days, book_id=book_id, client_id=user_id)
            orders_list.update(book_order.get_orders_details())
            print("Order has been added Successfully")
            print("The books' orders list : ",orders_list)

        inactive_list = []  # list of inactive book's id.
        for value in orders_list.values():
            inactive_list.append(value[1])
            books_list_1.remove(value[1])
        print("The books which were borrowed:", inactive_list)

        # print(books_list_1)
        # print("I am here?????")
    elif t == 5:
        print(users_list)
        print(books_list)
        print(orders_list)

    elif t == 6:
        ord_id = input("Enter Your Order ID: ")
        orders_list_id = list(orders_list.keys())
        print(ord_id)
        print(orders_list_id)
        print(inactive_list)
        if len(orders_list_id)>0:
            for i in range(len(orders_list_id)):
                if ord_id in orders_list_id:
                    rm_book = inactive_list [i]
                    inactive_list.remove(rm_book)
                    print(inactive_list)
                    break
        else:
            print("The Entered order id is not valid!!!")
    elif t == 7:
        break

print("Total borrowed orders= ", len(orders_list))
print("Total borrowed books= ", len(inactive_list))
print("Total available books= ", len(books_list) - len(inactive_list))

print(60 * "*","The End",60 * "*")
print("Programmed By: Mustafa M. Redwan\n Thanks")



