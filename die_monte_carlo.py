from random import randint

i = 0
ii = 0
iii = 0
iv = 0
v = 0
vi = 0

for trial in range(0, 10000):
    die = randint(1, 6)
    if die == 1:
        i += 1
    elif die == 2:
        ii += 1
    elif die == 3:
        iii += 1
    elif die == 4:
        iv += 1
    elif die == 5:
        v += 1
    else:
        vi += 1

print("i = {}, ii = {}, iii = {}, iv = {}, v = {}, vi = {}"
      .format(i, ii, iii, iv, v, vi))
