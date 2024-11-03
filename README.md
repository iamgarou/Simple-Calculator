# Simple-Calculator
Calculator Program
This Python program implements a simple calculator that performs basic arithmetic operations, area calculations, and power computations. It provides a user-friendly console interface for easy interaction.

Features
Basic Arithmetic Operations:

Addition
Subtraction
Multiplication
Division
Power (Exponentiation)
Square Root
Area Calculations:

Area of a Square
Area of a Rectangle
Area of a Circle
Area of a Cube
Area of a Cuboid
Area of a Sphere
Usage
Initialize the Calculator: Create an instance of the Calculator class.

python
Copy code
user = Calculator()
Display the Calculator Menu: Call the simple_math_cal method to display available operations.

python
Copy code
user.simple_math_cal()
Select an Operation: Input your choice (1-7) for the desired operation.

Perform the Calculation: Based on your choice, input the required numbers to perform the calculation.

Example Usage
Here’s a step-by-step example of how to use the calculator:

python
Copy code
# Step 1: Create a calculator instance
user = Calculator()

# Step 2: Display the calculator options
user.simple_math_cal()

# Step 3: User chooses an operation, for example, Addition (1)
user_choice = int(input("Your choice: "))

# Step 4: Input the numbers for the operation
if user_choice == 1:  # Addition
    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    user.add(n1, n2)  # This will print the result of the addition
Example Operations
Addition Example:

python
Copy code
user.add(5, 3)  # Output: 8
Square Root Example:

python
Copy code
user.sqrt(16)  # Output: 4.0
Area of a Circle Example:

python
Copy code
user.circle(5)  # Output: 78.53981633974483 (area for radius 5)
Conclusion
This Calculator program is a simple and effective tool for performing mathematical calculations and area computations. It is implemented using basic Python constructs and demonstrates the use of classes and methods for organizing functionality.

Feel free to contribute or modify the code to enhance its features!

License
This project is open source and available under the MIT License.

