import random

from art import logo, vs

from game_data import data

score = 0
game = True
compare_2 = random.choice(data)

while game:
    print(logo)

    compare_1 = compare_2

    name_1 = compare_1["name"]
    description_1 = compare_1["description"]
    country_1 = compare_1["country"]
    print(f"Compare A: {name_1}, a {description_1}, from {country_1}")


    compare_2 = random.choice(data)

    while compare_1 == compare_2:
        compare_2 = random.choice(data)


    name_2 = compare_2["name"]
    description_2 = compare_2["description"]
    country_2 = compare_2["country"]

    print(vs)
    print(f"Against B: {name_2}, a {description_2}, from {country_2}")


    A = compare_1["follower_count"]

    B = compare_2["follower_count"]


    person_choose = input("Who has more followers? Type 'A' or 'B': ").lower()

    if (person_choose == "a" and A > B) or (person_choose == "b" and B > A):
        score += 1
        print(f"You're right, your score is {score}")

    else:
        print(f"You are wrong. Game end. Your final score is {score}")
        game = False

