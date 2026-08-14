#Part 1
#Example 1
def say_hello():
    """A simple function that prints a greeting"""
    print("Hello, World!")
    print("Welcome to Python functions!")

# Calling the function
print("Calling say_hello():")
say_hello()
print()

#Part 2
#example 2
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
 
    # Method to get the area
    def get_area(self):
        pass
 
    # Method to get the perimeter
    def get_perimeter(self):
        pass
 
 
rect = Rectangle(10, 5)
print(rect.get_area())       # Should print 50
print(rect.get_perimeter())  # Should print 30
 
 
#Part 3
#example 3
def greet_person(name):
    """Greets a person by name"""
    print(f"Hello, {name}! Nice to meet you.")
 
print("Calling greet_person with different names:")
greet_person("Alice")
greet_person("Bob")
greet_person("Charlie")
print()
 
 
#Part 4
#example  4  
def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()
 
 
print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)
 
 
#Part 3
#example 1
def add_numbers(a, b):
    """Adds two numbers and returns the result"""
    result = a + b
    return result
 
print("Using functions that return values:")
sum1 = add_numbers(5, 3)
sum2 = add_numbers(10, 7)
print(f"5 + 3 = {sum1}")
print(f"10 + 7 = {sum2}")
print(f"Sum of both results: {sum1 + sum2}")
print()
 
#example 2
def get_circle_info(radius):
    """Calculates circle area and circumference"""
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    volumn = 4.0 / 3 * pi * radius
    return area, circumference
 
print("Circle calculations:")
radius = 5
area, circumference = get_circle_info(radius)
print(f"Circle with radius {radius}:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
print()

#Part 4
#example 1
def greet_with_title(name, title="Mr./Ms."):
    """Greets person with optional title"""
    print(f"Hello, {title} {name}!")

print("Using default parameters:")
greet_with_title("Smith")  # Uses default title
greet_with_title("Johnson", "Dr.")  # Custom title
greet_with_title("Brown", "Prof.")  # Custom title
print()

#example 2
def create_profile(name, age=18, country="Unknown"):
    """Creates a user profile with default values"""
    print(f"Profile: {name}, Age: {age}, Country: {country}")

print("Multiple default parameters:")
create_profile("Alice")  # All defaults
create_profile("Bob", 25)  # Age specified
create_profile("Charlie", 30, "USA")  # All specified
print()


#โจท แปลงเงิน ไทย เป็น USD
def convert_currency(value, currency):
    if currency == "USD":
        print(f"{value} THB = {(value / 33.0):.2f} USD")
    elif currency == "THB":
        print(f"{value} USD = {(value * 33.0):.2f} THB")
 
convert_currency(100,"USD")
convert_currency(100,"THB")