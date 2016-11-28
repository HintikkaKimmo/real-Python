def convert_f2c(f):
    c = (f - 32) * 5/9
    return c


def convert_c2f(c):
    f = (c * 9/5) + 32
    return f

new_f = float(input("Provide F to be converted to C: "))
print(convert_f2c(new_f))

new_c = float(input("Provide C to be converted to F: "))
print(convert_c2f(new_c))
