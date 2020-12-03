# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random as rnd
import pandas as pd
import Phystech
import string

users: Phystech = []
def generate_df() -> object:
    # Use a breakpoint in the code line below to debug your script.
    """Задание с двумя звёздочками -- сгенерировать 20 случайных пользователей, случайным образом
    просимулировать их взаимодействия, затем собрать pandas.DataFrame с данными о том, когда пользователи были онлайн и
    сколько у разных пользователей общих друзей, а потом визуализировать эти данные в seaborn с помощью line plots и heatmap
    соответственно."""
    # Создаем пользователей
    for i in range(rnd.randint(10, 100)):
        first_name: str = "{0}{1}".format(str(string.ascii_uppercase[rnd.randint(0, 22)]), "".join(
            [string.ascii_lowercase[rnd.randint(0, 22)] for i in range(rnd.randint(3, 12))])) + " "
        second_name: str = "{0}{1}".format(str(string.ascii_uppercase[rnd.randint(0, 22)]), "".join(
            [string.ascii_lowercase[rnd.randint(0, 22)] for i in range(rnd.randint(3, 12))]))
        full_name = first_name + second_name
        login: str = "".join([string.ascii_lowercase[rnd.randint(0, 22)] for i in range(rnd.randint(3, 12))])
        password: str = "".join([string.ascii_letters[rnd.randint(0, 22)] for i in range(rnd.randint(3, 12))])

        users.append(Phystech.Phystech(full_name, login, password))
    print(users)
if __name__ == '__main__':
    generate_df()
