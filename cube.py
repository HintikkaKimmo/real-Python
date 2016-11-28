def cube_number(num):
    cube = num * num * num
    return cube


def multiply_number(num1, num2):
    multiply = num1 * num2
    return multiply


cube_input = cube_number(float(input("Provide cube number: ")))
print(cube_number(cube_input))

multiply_num1 = float(input("Please provide number one: "))
multiply_num2 = float(input("Please provide number two: "))
print(multiply_number(multiply_num1, multiply_num2))
