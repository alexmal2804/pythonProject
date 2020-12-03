# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random as rnd
import pandas as pd
from pandas import DataFrame

import Phystech
import string
import datetime as dt
import matplotlib.pyplot as plt
users: Phystech = []


def generate_df() -> object:
    # Use a breakpoint in the code line below to debug your script.
    """Задание с двумя звёздочками -- сгенерировать 20 случайных пользователей, случайным образом
    просимулировать их взаимодействия, затем собрать pandas.DataFrame с данными о том, когда пользователи были онлайн и
    сколько у разных пользователей общих друзей, а потом визуализировать эти данные в seaborn с помощью line plots и heatmap
    соответственно."""
    # Создаем пользователей
    for i in range(0, rnd.randint(100, 1000)):
        first_name: str = "{0}{1}".format(str(string.ascii_uppercase[rnd.randint(0, 22)]), "".join(
            [string.ascii_lowercase[rnd.randint(0, 22)] for i in range(rnd.randint(3, 12))])) + " "
        second_name: str = "{0}{1}".format(str(string.ascii_uppercase[rnd.randint(0, 22)]), "".join(
            [string.ascii_lowercase[rnd.randint(0, 22)] for i in range(rnd.randint(3, 12))]))
        full_name = first_name + second_name
        login: str = "".join([string.ascii_lowercase[rnd.randint(0, 22)] for i in range(rnd.randint(3, 12))])
        password: str = "".join([string.ascii_letters[rnd.randint(0, 22)] for i in range(rnd.randint(3, 12))])
        graduation_year: int = rnd.randint(1900, 2020)
        birthday: dt.datetime = dt.datetime(rnd.randint(1900, 2012), rnd.randint(1, 12), rnd.randint(1, 28))
        users.append(Phystech.Phystech(full_name, login, password, graduation_year, birthday))
        for j in range(rnd.randint(0, 10)):
            k = rnd.randint(0, i)
            if k not in users[i].friends:
                users[i].add_friend(rnd.randint(0, i))
    # print(users)
    # print([users[i].friends for i in range(0, len(users))])
    # , columns=['UID', 'Name', 'Last_online', 'birthday', 'Graduation_year', 'Friends']
    # f = pd.DataFrame([x.as_dict() for x in person_list])
    # a.set_index('Date')['3'].plot()
    df: DataFrame = pd.DataFrame(x.get_fields for x in users)
    print(df)
    df = df.sort_values('Birthday')
    plt.scatter(df['Birthday'], df['Graduation_year'])
    plt.show()
    df = df.sort_values('Graduation_year')
    plt.bar(df['Graduation_year'], df['Friend_list'])
    plt.show()
if __name__ == '__main__':
    generate_df()