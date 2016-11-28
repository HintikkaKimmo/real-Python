def try_catcher():
    while True:
        try:
            user_int = int(input("Please provide an integer: "))
            print(user_int)
            break
        except ValueError:
            pass


try_catcher()

# TODO read more about try statements this was much harder than it should have been!


