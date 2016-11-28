for n in range(2, 10):
    print(n)

print("-----------------------")

n = 2
while n < 10:
    print(n)
    n += 1


def doubles(num):
    """Doubles takes num as an input and outputs num 3 times itself"""
    n = 1
    while n < 3:
        num = num * num
        n += 1
        print(num)

num_input = int(input("Provide number to double: "))
print(doubles(num_input))

# TODO figure why I am getting None as part of the result for doubles
