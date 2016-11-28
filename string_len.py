def string_len(word):
    if len(word) > 5:
        print("Word length is more than 5 letters!")
    elif len(word) == 5:
        print("Word length is equal to 5!")
    else:
        print("Word is shorter than 5 letters!")


len_input = input("Provide word for length measurement: ")
string_len(len_input)
