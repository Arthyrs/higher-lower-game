from art import logo, vs
from game_data import data
import random
import os


def profile(profile):
    name = profile["name"]
    description = profile["description"]
    country = profile["country"]
    return f"{name}, a {description}, from {country}."


def compare(a_profile, b_profile):
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_input == "a" and a_profile["follower_count"] > b_profile["follower_count"]:
        return 1
    elif user_input == "b" and a_profile["follower_count"] < b_profile["follower_count"]:
        return 1


def game():
    a_profile = random.choice(data)
    score = 0
    end = False
    while not end:
        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}.")

        b_profile = random.choice(data)
        while a_profile == b_profile:
            b_profile = random.choice(data)

        print(f"Compare A: {profile(a_profile)}")
        print(vs)
        print(f"Against B: {profile(b_profile)}")

        result = compare(a_profile, b_profile)
        if result:
            a_profile = b_profile
            score += result
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            end = True


game()
