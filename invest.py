def invest(amount, rate, time):
    """Compound interest of the investment

    invest method takes 3 values amount, rate and time in years
    and outputs total value of the investment each year.
    """
    print("Annual rate of return: {}". format(rate))
    for n in range(0, time):
        amount = amount + (amount * rate)
        print("Year {}: ${}".format(time, amount))
        print()
        n += 1


invest(100, 0.05, 8)
invest(2000, 0.025, 5)
