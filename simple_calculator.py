import math

class Calculator:
    def simple_math_cal(self):
        # Display the list of simple mathematical operations
        print("Calculator:")
        print("1. Addition.")
        print("2. Subtract.")
        print("3. Multiply.")
        print("4. Division.")
        print("5. Power.")
        print("6. Square Root.")
        print("7. To find Areas.")

    def add(self, n1, n2):
        # Perform addition and print the result
        print(n1 + n2)

    def sub(self, n1, n2):
        # Perform subtraction and print the result
        print(n1 - n2)

    def mult(self, n1, n2):
        # Perform multiplication and print the result
        print(n1 * n2)

    def div(self, n1, n2):
        # Perform division and print the result
        print(n1 / n2)

    def power(self, n1, n2):
        # Calculate n1 raised to the power of n2 using recursion
        if n2 == 0:
            return 1
        n = n1 * self.power(n1, n2 - 1)
        return n

    def sqrt(self, n1):
        # Calculate the square root of n1 and print the result
        print(math.sqrt(n1))

    def areas(self):
        # Display the list of area calculation options
        print("\nAreas:")
        print("1. Area of Square.")
        print("2. Area of Rectangle.")
        print("3. Area of Circle.")
        print("4. Area of Cube.")
        print("5. Area of Cuboid.")
        print("6. Area of Sphere.")
    
    def square(self, s):
        # Calculate and print the area of a square
        print(s * s)
    
    def cube(self, s):
        # Calculate and print the surface area of a cube
        print(6 * s * s)

    def circle(self, r):
        # Calculate and print the area of a circle
        print(math.pi * r * r)
    
    def sphere(self, r):
        # Calculate and print the surface area of a sphere
        print(4 * math.pi * r * r)

    def rectangle(self, s1, s2):
        # Calculate and print the area of a rectangle
        print(s1 * s2)

    def cuboid(self, s1, s2, s3):
        # Calculate and print the surface area of a cuboid
        print(2 * (s1 * s2 + s2 * s3 + s1 * s3))

# Create an instance of the Calculator class
user = Calculator()
# Display the options for simple math calculations
user.simple_math_cal()

# Get user input for the choice of operation
try:
    user_choice = int(input("Your choice: "))
    # Validate user choice for available operations
    if user_choice < 1 or user_choice > 7:
        print("\nChoose a number from the option.\n")
except ValueError:
    print("\nInput must be an Integer.\n")

# For operations that require two numbers
if user_choice >= 1 and user_choice <= 5:
    try:
        n1 = int(input("n1: "))
        n2 = int(input("n2: "))
    except ValueError:
        print("\nInput must be an Integer.\n")
    
    # Call the corresponding method based on user choice
    if user_choice == 1:
        user.add(n1, n2)  # Addition
    if user_choice == 2:
        user.sub(n1, n2)  # Subtraction
    if user_choice == 3:
        user.mult(n1, n2)  # Multiplication
    if user_choice == 4:
        user.div(n1, n2)  # Division
    if user_choice == 5:
        print(user.power(n1, n2))  # Power calculation

# For square root operation
if user_choice == 6:
    try:
        n1 = int(input("n1: "))
    except ValueError:
        print("\nInput must be an Integer.\n")
    user.sqrt(n1)  # Calculate square root

# For area calculations
if user_choice == 7:
    user.areas()  # Display area options
    try:
        user_choice_2 = int(input("Your choice: "))
        # Validate user choice for area calculations
        if user_choice_2 < 1 or user_choice_2 > 6:
            print("\nChoose a number from the option.\n")
    except ValueError:
        print("\nInput must be an Integer.\n")

    # For square and cube area calculations
    if user_choice_2 == 1 or user_choice_2 == 4:
        try:
            n1 = int(input("side: "))
        except ValueError:
            print("\nInput must be an Integer.\n")
        if user_choice_2 == 1:
            user.sq
