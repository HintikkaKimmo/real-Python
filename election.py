from random import random

candidate_a = 0
candidate_b = 0


for i in range(0, 10000):
    election_won = 0
    result = random()
    while True:
        if result > 0.87:
            election_won += 1
        if result > 0.65:
            election_won += 1
        if result > 0.17:
            election_won += 1
        break
    if election_won >= 2:
        candidate_a += 1
    else:
        candidate_b += 1


print("Total wins for candidate A: {}. Total wins for candidate B {}".format(candidate_a, candidate_b))
