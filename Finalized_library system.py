import random
from datetime import date

class Book:
    def __init__(self, title, author, year, publisher, number_of_copies, publication_date):
        # initialize the attributes of the Book object
        self.book_id = random.randint(5000, 9999)
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher
        self.number_of_copies = number_of_copies
        self.publication_date = publication_date

    def update_title(self, title):
        self.title = title

    def update_author(self, author):
        self.author = author

    def update_year(self, year):
        self.year = year

    def update_publisher(self, publisher):
        self.publisher = publisher

    def update_number_of_copies(self, number_of_copies):
        self.number_of_copies = number_of_copies

    def update_publication_date(self, publication_date):
        if publication_date > date.today():
            raise ValueError('Publication date cannot be in the future')
        self.publication_date = publication_date

    # Getting methods for each attribute
    def get_book_id(self):
        return self.book_id

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_number_of_copies(self):
        return self.number_of_copies

    def get_publication_date(self):
        return self.publication_date


class BookList:
    def __init__(self):
        self.book_collection = {}

    def add_book(self, book):
        self.book_collection[book.get_book_id()] = book

    def search_book(self, search_key, value):
        search_results = []
        for book in self.book_collection.values():
            if search_key.lower() == 'title' and book.get_title().lower() == value.lower():
                search_results.append(book)
            elif search_key.lower() == 'author' and book.get_author().lower() == value.lower():
                search_results.append(book)
            elif search_key.lower() == 'publisher' and book.get_publisher().lower() == value.lower():
                search_results.append(book)
            elif search_key.lower() == 'publication_date' and str(book.get_publication_date()) == value:
                search_results.append(book)
        return search_results

    def remove_book(self, title):
        for book_id, book in list(self.book_collection.items()):
            if book.get_title().lower() == title.lower():
                del self.book_collection[book_id]

    def show_total_books(self):
        return len(self.book_collection)


class Users:
    def __init__(self, username, firstname, surname, house_number, street_name,
                 postcode, email_address, dob):
        self.username = username
        self.firstname = firstname
        self.surname = surname
        self.house_number = house_number
        self.street_name = street_name
        self.postcode = postcode
        self.email_address = email_address
        self.dob = dob

    # Getter methods
    def get_username(self):
        return self.username

    def get_firstname(self):
        return self.firstname

    def get_surname(self):
        return self.surname

    def get_house_number(self):
        return self.house_number

    def get_street_name(self):
        return self.street_name

    def get_postcode(self):
        return self.postcode

    def get_email_address(self):
        return self.email_address

    def get_dob(self):
        return self.dob

    # Setter methods
    def update_username(self, new_username):
        self.username = new_username

    def update_firstname(self, new_firstname):
        self.firstname = new_firstname

    def update_surname(self, new_surname):
        self.surname = new_surname

    def update_house_number(self, new_house_number):
        self.house_number = new_house_number

    def update_street_name(self, new_street_name):
        self.street_name = new_street_name

    def update_postcode(self, new_postcode):
        self.postcode = new_postcode

    def update_email_address(self, new_email_address):
        self.email_address = new_email_address

    def update_dob(self, new_dob):
        self.dob = new_dob


class UserList:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.get_username()] = user

    def remove_user(self, username):
        if username in self.users:
            del self.users[username]
        else:
            print("User not found.")

    def count_users(self):
        return len(self.users)

    def user_surname(self, surname):
        for user in self.users.values():
            if user.get_surname() == surname:
                return user
        return None  # Return None if user with specified surname not found

    def user_firstname(self, firstname):
        matching_users = []
        for user in self.users.values():
            if user.get_firstname() == firstname:
                matching_users.append(user)
        return matching_users

# loans
class Loans:
    def __init__(self):
        ## Constructor to initialize the Loans object.

        self.borrowed_books = {}  # Dictionary to store borrowed books with user IDs

    def borrow_book(self, username, book):
        """
        Method for a user to borrow a book.

        Parameters:
        - user_id: ID of the user borrowing the book.
        - book: Book object to be borrowed.
        """
        # username is unique helping us to retrieve user info using username
        if username not in self.borrowed_books:
            self.borrowed_books[username] = [book]
        else:
            self.borrowed_books[username].append(book)

    def return_book(self, username, book):
        """
        Method for a user to return a book.

        Parameters:
        - user_id: ID of the user returning the book.
        - book: Book object to be returned.
        """
        if username in self.borrowed_books and book in self.borrowed_books[username]:
            self.borrowed_books[username].remove(book)
        else:
            print("Book not found in user's borrowed books.")

    def count_borrowed_books(self, username):
        """
        Method to count and return the total number of books a user is currently borrowing.

        Parameters:
        - user_id: ID of the user.

        Returns:
        - The total number of books the user is currently borrowing.
        """
        if username in self.borrowed_books:
            return len(self.borrowed_books[username])
        else:
            return 0

    def print_overdue_books(self, user_id_to_user_map):
        """
        Method to print out all the overdue books along with the users' username and first name.

        Parameters:
        - user_id_to_user_map: A dictionary mapping user IDs to User objects.
        """
        today = date.today()
        for username, books in self.borrowed_books.items():
            user = user_id_to_user_map.get(username)
            if user:
                for book in books:
                    if book.get_due_date() < today:
                        print(
                            f"Overdue Book: {book.get_title()} Borrower: {user.get_username()} - {user.get_firstname()}")

    # Additional methods for error checking and exception handling can be added as needed


if __name__ == '__main__':

    booklist = BookList()
    userlist = UserList()
    loans = Loans()

    book1 = Book('Data science essentials', 'Robert Dragon', '2002', 'WD Press', '12', date(1995, 6, 10))
    book2 = Book('Cyber Security essentials', 'Robert Dragon', '2002', 'WD Press', '12', date(1995, 6, 10))
    book3 = Book('Engineering Fundamentals', 'Robert Dragon', '2002', 'WD Press', '12', date(1995, 6, 10))

    booklist.add_book(book1)
    booklist.add_book(book2)
    booklist.add_book(book3)


    user1 = Users('ABC123','Jane','Haris','AB123','Street 21','postcode','jane12@gmail.com','12-09-1995')
    user2 = Users('RB987','James','Tryson','AB123','Street 21','postcode','jane12@gmail.com','12-09-1995')
    user3 = Users('C7783','Jane','Haris','AB123','Street 21','postcode','jane12@gmail.com','12-09-1995')
    user4 = Users('ABC123','Jane','Haris','AB123','Street 21','postcode','jane12@gmail.com','12-09-1995')

    userlist.add_user(user1)
    userlist.add_user(user2)
    userlist.add_user(user3)
    userlist.add_user(user4)

    # Example: John Doe borrows "Python Programming for Beginners"
    loans.borrow_book(user1.get_username(), book1)
    print(f"{user1.get_username()} borrowed '{book1.get_title()}'")

    # Example: Alice Johnson borrows "Web Development with Django"
    loans.borrow_book(user2.get_username(), book2)
    print(f"{user2.get_username()} borrowed '{book2.get_title()}'")

    # Example: Emily Smith borrows "Data Science for Beginners"
    loans.borrow_book(user3.get_username(), book3)
    print(f"{user3.get_username()} borrowed '{book3.get_title()}'")

    # Example: John Doe returns "Python Programming for Beginners"
    loans.return_book(user1.get_username(), book1)
    print(f"{user1.get_username()} returned '{book1.get_title()}'")

    # Example: Alice Johnson borrows "Data Science for Beginners"
    loans.borrow_book(user2.get_username(), book3)
    print(f"{user2.get_username()} borrowed '{book3.get_title()}'")

    # Example: Emily Smith returns "Data Science for Beginners"
    loans.return_book(user3.get_username(), book3)
    print(f"{user3.get_username()} returned '{book3.get_title()}'")

    # Example: John Doe borrows "Web Development with Django" again
    loans.borrow_book(user1.get_username(), book2)
    print(f"{user1.get_username()} borrowed '{book2.get_title()}'")

    print('************ show some of the user details in the system*************:')
    for user in userlist.users.values():
        print('Username:',user.get_username())
        print('Firstname:',user.get_firstname())
        print('Surname:',user.get_surname())
        print('House_number:',user.get_house_number())
        print('Street_number:',user.get_street_name())



    # Print all borrowed books for a specific user
   # user = user1
  #  borrowed_books = loans.borrowed_books(user.get_username())
   # print(f"\nBooks borrowed by {user.get_username()}:")
   # for book in borrowed_books:

  #  print(book.get_title())


    print('######### Show all available book list #####:')
    for book in booklist.book_collection.values():
        print('Book ID:', book.get_book_id())
        print('Book Title:', book.get_title())
        print('Book Author:', book.get_author())
        print('Publisher:', book.get_publisher())
        print('Number of copies exist:', book.get_number_of_copies())
        print('Publication date:', book.get_publication_date())

    print('\nSearch for a book:')
    search_results = booklist.search_book('title', 'Data science essentials')
    if search_results:
        print('Result found:', search_results[0].get_title())
    else:
        print('No result found')






    while True:
        print('Modify book information:')
        print('1. Modify books')
        print('2. Modify users information')
        section_choice = input('Choose the number of the option you wish to modify: ')
        if section_choice == '1':
            book_id = int(input('Enter the book ID you wish to modify: '))
            if book_id not in booklist.book_collection:
                print('Book not found.')
                continue

            book = booklist.book_collection[book_id]
            print('Book found. Book Details:')
            print(f'1. Title: {book.get_title()}')
            print(f'2. Author: {book.get_author()}')
            print(f'3. Year: {book.get_year()}')
            print(f'4. Publisher: {book.get_publisher()}')
            print(f'5. Number of Copies: {book.get_number_of_copies()}')
            print(f'6. Publication Date: {book.get_publication_date()}')

            attribute_choice = input('Select the attribute you wish to change: ')
            if attribute_choice == '1':
                new_title = input('Enter the new title: ')
                book.update_title(new_title)
                print(f'The {new_title} book has been updated successfully')
            elif attribute_choice == '2':
                new_author = input('Enter the new author: ')
                book.update_author(new_author)
                print(f'The {new_author} author has been updated successfully')
            elif attribute_choice == '3':
                new_year = input('Enter the new year: ')
                book.update_year(new_year)
                print(f'The year registered the book has been updated successfully')
            elif attribute_choice == '4':
                new_publisher = input('Enter the new publisher: ')
                book.update_publisher(new_publisher)
                print(f'The publisher name has been updated successfully')
            elif attribute_choice == '5':
                new_copies_no = input('Enter the new amount of copies available: ')
                book.update_number_of_copies(new_copies_no)
                print(f'The number of copies available for {new_title} book has been updated successfully')
            elif attribute_choice == '6':
                new_publication_date = input('Enter the new publication date (YYYY-MM-DD): ')
                book.update_publication_date(date.fromisoformat(new_publication_date))
                print(f'The publication date for {new_title} has been updated successfully')

        elif section_choice == '2':

            print('Modify user information:')
            # Add code for modifying user information here

            username = input('enter the username of the user you wish to update: ')
            if username not in userlist.users:
                print(f' username:{username} not found')
                continue
            user = userlist.users[username]
            print('user details')
            print(f'1. firstname: {user.get_firstname()}')
            print(f'2. surname: {user.get_surname()}')
            print(f'3. house_number: {user.get_house_number()}')
            print(f'4. street_name: {user.get_street_name()}')

            # prompt user attribute
            user_attribute = input('choose the user attribute you wish to change: ')
            if user_attribute == '1':
                new_firstname = ('enter the new first name: ')
                user.update_firstname(new_firstname)
                print('the first name has been modified')
            elif user_attribute == '2':
                new_surname = input('enter the new surname: ')
                user.update_surname(new_surname)
                print(' surname has been modified')
            elif user_attribute == '3':
                new_house_number = input('enter the new number for the house: ')
                user.update_house_number(new_house_number)
                print('house number has been modified')
            elif user_attribute == '4':
                new_street_name = input('enter the new name of the street: ')
                user.update_street_name(new_street_name)
                print('street name has been modified')
        else:
            print('Please choose a valid choice.')
