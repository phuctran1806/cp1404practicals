import random

print(random.randint(5, 20)) # line 1
# I saw 5, 15, 9, 20 on line 1
# The smallest number I could have seen was 5, and the largest was 20

print(random.randrange(3, 10, 2)) # line 2
# I saw 3, 5, 7, 9 on line 2
# The smallest number I could have seen was 3, and the largest was 9
# Line 2 couldn't produce a 4

print(random.uniform(2.5, 5.5)) # line 3
# I saw 4.564640470376859, 3.7355470552600925, 2.522601690260572, 5.489607835651491 on line 3
# The smallest number I could have seen was 2.522601690260572, and the largest was 5.489607835651491

random_number = random.randint(1, 100)
print(random_number)