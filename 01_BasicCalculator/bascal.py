import math

ans = 0

while True:
    print("\n WELCOME TO BASIC CALCULATOR")
    print("a. Addition")
    print("b. Subtraction")
    print("c. Multiplication")
    print("d. Division")
    print("e. Power")
    print("f. Square Root")
    print("g. Factorial")
    print("h. Sine")
    print("i. Cosine")
    print("j. Tangent")
    print("k Natural Log")
    print("l Log Base 10")
    print("m. Pi")
    print("n. Euler's Number")
    print("o. Modulus")
    print("p. Exit")

    selected = input("\nChoose an operation. Type the letter: ").lower()

    try:
        if selected == "a":
            a = float(input("First number: "))
            b = float(input("Second number: "))
            ans = a + b

        elif selected == "b":
            a = float(input("First number: "))
            b = float(input("Second number: "))
            ans = a - b

        elif selected == "c":
            a = float(input("First number: "))
            b = float(input("Second number: "))
            ans = a * b

        elif selected == "d":
            a = float(input("First number: "))
            b = float(input("Second number: "))
            ans = a / b

        elif selected == "e":
            x = float(input("Base: "))
            y = float(input("Exponent: "))
            ans = x ** y

        elif selected == "f":
            x = float(input("Number: "))
            ans = math.sqrt(x)

        elif selected == "g":
            x = int(input("Number: "))
            ans = math.factorial(x)

        elif selected == "h":
            x = float(input("Angle in degrees: "))
            ans = math.sin(math.radians(x))

        elif selected == "i":
            x = float(input("Angle in degrees: "))
            ans = math.cos(math.radians(x))

        elif selected == "j":
            x = float(input("Angle in degrees: "))
            ans = math.tan(math.radians(x))

        elif selected == "k":
            x = float(input("Number: "))
            ans = math.log(x)

        elif selected == "l":
            x = float(input("Number: "))
            ans = math.log10(x)

        elif selected == "m":
            ans = math.pi

        elif selected == "n":
            ans = math.e

        elif selected == "o":
            a = int(input("First number: "))
            b = int(input("Second number: "))
            ans = a % b

        elif selected == "p":
            print("Calculator closed.")
            break

        else:
            print("Invalid choice.")
            continue

        print(f"Result = {ans}")
    
    except ValueError:
        print("Syntax Error")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except Exception as e:
        print("Math Error:", e)