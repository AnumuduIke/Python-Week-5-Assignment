# Activity 1
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def get_info(self):
        return f"Book: {self.title} by {self.author}, Price: ${self.price}"

    def apply_discount(self, discount_percentage):
        self.price -= self.price * (discount_percentage / 100)


class EBook(Book):
    def __init__(self, title, author, price, file_size):
        super().__init__(title, author, price)  # Call the parent class constructor
        self.file_size = file_size  # EBook-specific attribute

    def get_info(self):
        book_info = super().get_info()  # Get info from the parent class method
        return f"{book_info}, File Size: {self.file_size}MB"

    def download(self):
        return f"Downloading {self.title}..."


book = Book("Python 101", "John Doe", 29.99)
ebook = EBook("Learn Python", "Jane Smith", 19.99, 5)


print(book.get_info())  
book.apply_discount(10)  
print(book.get_info())  

print(ebook.get_info())  
print(ebook.download())  


# Activity 2

class Vehicle:
    def move(self):
        pass  


class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")


vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()  
