# import math
open("simple_Calculator.txt", "w").write('''Simple Calculator
This is a simple calculator program implemented in Python. It provides a user-friendly command-line interface for performing basic arithmetic operations and calculating areas of various geometric shapes. The functionalities include:

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
Surface Area of a Cube
Surface Area of a Cuboid
Surface Area of a Sphere
Usage
Run the program in a Python environment.
Choose an operation by entering the corresponding number.
Provide the required input values when prompted.
The calculator will display the result for the chosen operation.
Installation
To run this project, you need to have Python installed on your machine. Clone the repository and execute the calculator.py file:

bash
Copy code
git clone <repository-url>
cd <repository-directory>
python calculator.py
Contributions
Feel free to fork the repository and submit pull requests for any improvements or additional features!

License
This project is open source and available under the MIT License.

''')
# class Calculator:
#     def simple_math_cal(self):
#         print("Calculator:")
#         print("1. Addition.")
#         print("2. Substract.")
#         print("3: Multiply.")
#         print("4: Division.")
#         print("5. Power.")
#         print("6. Square Root.")
#         print("7. To find Areas.")

#     def add(self, n1, n2):
#         print(n1+n2)

#     def sub(self, n1, n2):
#         print(n1-n2)

#     def mult(self, n1, n2):
#         print(n1*n2)

#     def div(self, n1, n2):
#         print(n1/n2)

#     def power(self, n1, n2):
#         if n2 == 0:
#             return 1
#         n =n1*self.power(n1,n2-1)
#         return n

#     def sqrt(self, n1):
#         print(math.sqrt(n1))

#     def areas(self):
#         print("\nAreas:")
#         print("1. Area of Square.")
#         print("2. Area of Rectangle.")
#         print("3: Area of Circle.")
#         print("4. Area of Cube.")
#         print("5. Area of Cuboid.")
#         print("6. Area of Sphere.")
    
#     def square(self, s):
#         print(s*s)
    
#     def cube(self, s):
#         print(6*s*s)

#     def circle(self, r):
#         print(math.pi*r*r)
    
#     def sphere(self, r):
#         print(4*math.pi*r*r)

#     def rectangle(self, s1, s2):
#         print(s1*s2)

#     def cuboid(self, s1,s2,s3):
#         print(2*(s1*s2+s2*s3+s1*s3))

# user = calculator()
# user.simple_math_cal()
# try:
#     user_choice = int(input("Your choice: "))
#     if user_choice<1 or user_choice>7:
#         print("\nChoose a number from the option.\n")
# except ValueError:
#     print("\nInput must be a Integer.\n")

# if user_choice>=1 and user_choice<=5:
#     try:
#         n1 = int(input("n1: "))
#         n2 = int(input("n2: "))
#     except ValueError:
#         print("\nInput must be a Integer.\n")
    
#     if user_choice == 1:
#             user.add(n1, n2)
#     if user_choice == 2:
#         user.sub(n1, n2)
#     if user_choice == 3:
#         user.mult(n1, n2)
#     if user_choice == 4:
#         user.div(n1, n2)
#     if user_choice == 5:
#         print(user.power(n1, n2))

# if user_choice == 6:
#     try:
#         n1 = int(input("n1: "))
#     except ValueError:
#         print("\nInput must be a Integer.\n")
#     user.sqrt(n1)

# if user_choice == 7:
#     user.areas()
#     try:
#         user_choice_2 = int(input("Your choice: "))
#         if user_choice_2<1 or user_choice_2>6:
#             print("\nChoose a number from the option.\n")
#     except ValueError:
#         print("\nInput must be a Integer.\n")

#     if user_choice_2 == 1 or user_choice_2 == 4:
#         try:
#             n1 = int(input("side: "))
#         except ValueError:
#             print("\nInput must be a Integer.\n")
#         if user_choice_2 == 1:
#             user.square(n1)
#         if user_choice_2 == 4:
#             user.cube(n1)

#     if user_choice_2 == 3 or user_choice_2 == 6:
#         try:
#             n1 = int(input("radius: "))
#         except ValueError:
#             print("\nInput must be a Integer.\n")
#         if user_choice_2 == 3:
#             user.circle(n1)
#         if user_choice_2 == 4:
#             user.sphere(n1)
        

#     if user_choice_2 == 2:
#         try:
#             n1 = int(input("length: "))
#             n2 = int(input("breath: "))
#         except ValueError:
#             print("\nInput must be a Integer.\n")
#         user.rectangle(n1, n2)

#     if user_choice_2 == 5:
#         try:
#             n1 = int(input("lenth: "))
#             n2 = int(input("breath: "))
#             n3 = int(input("hight: "))
#         except ValueError:
#             print("\nInput must be a Integer.\n")
#         user.cuboid(n1, n2, n3)
    

