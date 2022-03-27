# TASK 1 -- QUESTION 1

# raining = input("Is it raining? Y/N ")
# is_raining = raining == 'Y'
#
# if is_raining:
#     print('Take an umbrella')
# else:
#     print('You do not need an umbrella')

# TASK 1 -- QUESTION 2
# my_money = float(input('How much money do you have? '))
# boat_cost = 20 + 5
# if my_money > boat_cost:
#     print('You can afford the boat hire')
# else:
#     print('You cannot afford the boat hire')

# TASK 1 -- QUESTION 3
# book_year = int(input('What century is the book from? '))
# book_decade = int(input('What decade is the book from? '))
#
# if book_year == 18:
#     print('That is the Eighteenth Century.')
# elif book_year == 19:
#     print('That is the Nineteenth Century.')
# else:
#     print('Error, century not recognised.')
#
#
# if 00 <= book_decade <= 9:
#     print('Noughties.')
# elif 10 <= book_decade <= 19:
#     print('Teens.')
# elif 20 <= book_decade <= 29:
#     print('Twenties.')
# elif 30 <= book_decade <= 39:
#     print('Thirties.')
# elif 40 <= book_decade <= 49:
#     print('Forties.')
# elif 50 <= book_decade <= 59:
#     print('Fifties.')
# elif 60 <= book_decade <= 69:
#     print('Sixties.')
# elif 70 <= book_decade <= 79:
#     print('Seventies.')
# elif 80 <= book_decade <= 89:
#     print('Eighties.')
# elif 90 <= book_decade <= 99:
#     print('Nineties.')
# else:
#     print('Error, Decade not recognised.')
#

# TASK 2 -- QUESTION 1
# shopping_list = [
# 	"oranges",
# 	"cat food",
# 	"sponge cake",
# 	"long-grain rice",
# 	"cheese board",
# ]
# print(shopping_list[0])

# TASK 2 -- QUESTION 2
# def print_choc_price():
#
#     chocolates = {
#         'white': 1.50,
#         'milk': 1.20,
#         'dark': 1.80,
#         'vegan': 2.05,
#     }
#     choc_choice = input('What is your choice of chocolate today? ').lower()
#
#     if choc_choice not in chocolates:
#         choc_cost = f"Please type: white, milk, dark or vegan."
#         print(choc_cost)
#     else:
#         cost = format(chocolates[choc_choice], '.2f')
#         choc_cost = f"{choc_choice.title()} chocolate costs £{cost} per bar."
#         print(choc_cost)


# print_choc_price()

# TASK 2 -- QUESTION 3
# import random


# def lottery():
#     winnings = {0: 0, 1: 0, 2: 0, 3: 20, 4: 40, 5: 100, 6: 10000, 7: "1 million"}
#
#     lottery_numbers = random.sample(range(1, 60), 7)
#     player_numbers = random.sample(range(1, 60), 7)
#
#     matching_nums = 0
#     for num in player_numbers:
#         if num in lottery_numbers:
#             matching_nums += 1
#
#     reward = f'You chose {matching_nums} correctly and won £{winnings[matching_nums]}!'
#     if matching_nums <= 2:
#         print(f'Bad luck! {reward}')
#     else:
#         print(f'Congratulations! {reward}!')
#     print(f'The winning ticket numbers are: {sorted(lottery_numbers)}')
#     print(f'Your ticket numbers are: {sorted(player_numbers)}.')
#
#
# lottery()

# TASK 3 -- QUESTION 2
# poem = 'I like Python and I am not very good at poems'
# with open('poem.txt', 'w') as poem_file:
# 	poem_file.write(poem)


# TASK 3 -- Question 3
# import requests
# from pprint import pprint as pp
#
# file = open('C:\\Users\\hlarn\\Desktop\\song.txt.TXT', 'r')
# for content in file:
#     elton = "still"
#     if elton in content:
#             print(content)


# content = file.readlines()
# pp(content)

# elton_john = [
#     "\nYou could never know what it's like"
#     "\nYour blood like winter freezes just like ice"
#     "\nAnd there's a cold lonely light that shines from you"
#     "\nYou'll wind up like the wreck you hide behind that mask you use"
#
#     "\nAnd did you think this fool could never win?"
#     "\nWell look at me, I'm coming back again"
#     "\nI got a taste of love in a simple way"
#     "\nAnd if you need to know while I'm still standing, you just fade away"
#
#     "\nDon't you know I'm still standing better than I ever did"
#     "\nLooking like a true survivor, feeling like a little kid"
#     "\nI'm still standing after all this time"
#     "\nPicking up the pieces of my life without you on my mind"
#
#     "\nI'm still standing (Yeah, yeah, yeah)"
#     "\nI'm still standing (Yeah, yeah, yeah)"
# ]

# file.writelines(elton_john)
# file.close()

# TASK 4 -- QUESTION 1
# import random
# import requests
# import re

# def get_six_pokemon_names_and_moves():
#     # create random pokemon ids
#     pokemon_ids = random.sample(range(1, 898), 6)
#     # create string for pokemon moves
#     p_moves = ""
#     # create string for all pokemon data from the txt file
#     pokemon_data = ""
#
#     for id_no in pokemon_ids:
#         url = f'https://pokeapi.co/api/v2/pokemon/{id_no}/'
#         response = requests.get(url)
#         # print(response)
#         pokemon = response.json()
#
#         pokemon_name = pokemon['name']
#         # print(pokemon_name)
#
#         moves = pokemon['moves']
#         # print(moves)
#
#         for move in moves:
#             p_moves += move['move']['name'].title()
#             pokemon_moves = re.sub(r"(\w)([A-Z])", r"\1, \2", p_moves)
#             # print(pokemon_moves)
#
#             with open('pokemon.txt', 'r') as poke_file:
#                 pokemon_data = poke_file.read()
#
#             pokemon_data = pokemon_data + "Pokemon " + pokemon_name.title() + "'s moves are: " + pokemon_moves + "." + "\n"
#
#         with open('pokemon.txt', 'w+') as poke_file:
#             poke_file.write(pokemon_data)
#
#
# get_six_pokemon_names_and_moves()
