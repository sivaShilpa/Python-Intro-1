def calculator():
    num1 = input("Enter number 1: ")
    num2 = input("Enter number 2: ")
    oprn = input("Enter operation (+, *, /, -): ")

    if oprn == "+":
        return int(num1)+int(num2)
    elif oprn == "*":
        return int(num1)*int(num2)
    elif oprn == "/":
        return float(int(num1)/int(num2))
    elif oprn == "-":
        return int(num1)-int(num2)



