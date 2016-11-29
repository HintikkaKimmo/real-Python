from random import randint

rolls = [0] * 6

for trial in range(0, 10000):
    die = randint(1, 6)
    rolls[die - 1] += 1

print("i = {}, ii = {}, iii = {}, iv = {}, v = {}, vi = {}"
      .format(* rolls))
