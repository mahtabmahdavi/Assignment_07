import random

boys = ["ali", "reza", "yasin", "benyamin", "mehrdad", "sajjad", "aidin", "shahin"]
girls = ["sara", "zari", "neda", "homa", "eli", "goli", "mary", "mina"]
result = []

for i in range(8):
    random_boy = random.choice(boys)
    boys.remove(random_boy)

    random_girl = random.choice(girls)
    girls.remove(random_girl)

    result.append((random_boy, random_girl))


print(result)

