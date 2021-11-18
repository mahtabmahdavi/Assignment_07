class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def Add(self, other):
        return self.numerator * other.denominator + self.denominator * other.numerator, self.denominator * other.denominator

    def Mul(self, other):
        return self.numerator * other.numerator, self.denominator * other.denominator

    def Sub(self, other):
        return self.numerator * other.denominator - self.denominator * other.numerator, self.denominator * other.denominator

    def Div(self, other):
        return self.numerator * other.denominator, self.denominator * other.numerator


def menu():
    print("1. Addition of two fractions")
    print("2. Multiply two fractions")
    print("3. Subtraction of two fractions")
    print("4. Divide into two fractions")
    print("5. Exit")


def get_numerator():
    input_numerator = int(input("\nEnter the numerator of your fraction: "))
    return input_numerator


def get_denominator():
    input_denominator = int(input("Enter the denominator of your fraction: "))

    while input_denominator == 0:
        print("\nZero is invalid for the denominator.")
        input_denominator = int(input("Enter the denominator of your fraction: "))

    return input_denominator


while True:
    menu()
    choice = int(input("--> "))

    if choice == 1:
        first_obj = Fraction(get_numerator(), get_denominator())
        second_obj = Fraction(get_numerator(), get_denominator())
        result1 , result2 = Fraction.Add(first_obj, second_obj)
        print("Result =", result1, "\\", result2, "\n")
    
    elif choice == 2:
        first_obj = Fraction(get_numerator(), get_denominator())
        second_obj = Fraction(get_numerator(), get_denominator())
        result1 , result2 = Fraction.Mul(first_obj, second_obj)
        print("Result =", result1, "\\", result2, "\n")

    elif choice == 3:
        first_obj = Fraction(get_numerator(), get_denominator())
        second_obj = Fraction(get_numerator(), get_denominator())
        result1 , result2 = Fraction.Sub(first_obj, second_obj)
        print("Result =", result1, "\\", result2, "\n")

    elif choice == 4:
        first_obj = Fraction(get_numerator(), get_denominator())
        second_obj = Fraction(get_numerator(), get_denominator())
        result1 , result2 = Fraction.Div(first_obj, second_obj)
        print("Result =", result1, "\\", result2, "\n")

    elif choice == 5:
        break
    
    else:
        print("\nTry again!\n")
