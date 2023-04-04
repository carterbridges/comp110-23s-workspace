"""Example functions to learn syntax"""
def my_max(number1: int, number2: int) -> int:
    """Returns the maximum value out of two numbers"""
    if number1 >= number2:
        return number1
    else: #number1 < number 2
        return number2

max_number: int = my_max(25467, 479204)
print(max_number)