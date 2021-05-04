from calculater_art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divison(n1, n2):
    return n1 / n2

 
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divison
}

def calculater():
    num1 = float(int(input("What is the first number = ")))

    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(int(input("What is the next number = ")))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"type 'yes' to continue with {answer} no type 'no' ") == "yes":
            num1 = answer
        else:
            should_continue = False
            calculater()
    
calculater()

    


