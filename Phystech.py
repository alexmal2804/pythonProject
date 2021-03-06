"""
ДОП Задание к ДЗ (Необязательно к выполнению, но приносит доп. балл)

Дополните класс Phystech так, чтобы у пользователей появился список друзей. Пользователи должны быть в состоянии
добавлять других в друзья по uid, удалять других из друзей; смотреть на список общих друзей; проверять, приняли ли
заявку в друзья; видеть актуальный список входящих и исходящих заявок; запрещать конкретным пользователям добавлять себя
 в друзья.
При этом любое действие пользователя должно обновлять переменную self.last_online, а история её значений для каждого из
пользователей должна накапливаться в статическом поле класса (т.е. должен быть Dict[int, List[datetime]] -- отображение
из uid в историю сеансов.
"""
from datetime import datetime
from typing import Optional
from collections import defaultdict


class Phystech:
    uid = 0
    # Лог активностей
    list_online = defaultdict(list)
    # Стоп-лист
    stop_list = defaultdict(list)
    # Список друзей
    friend_list = defaultdict(list)

    def __init__(
            self,
            name: str,
            login: str,
            password: str,
            graduation_year: Optional[int] = None,
            birthday: Optional[datetime] = None,
            status: Optional[str] = None,
    ):
        self.name = name
        self.status = status
        self.__uid = Phystech.uid
        self.last_online = datetime.now()
        Phystech.list_online[self.__uid].append(self.last_online)
        Phystech.uid += 1

        self._birthday = birthday
        self._graduation_year = graduation_year
        self.__login = login
        self.__password = password
        self.friends = []

    @property
    def is_graduate(self) -> Optional[bool]:
        if self._graduation_year is not None:
            return datetime.now().year - self._graduation_year > 0
        return None

    # Ведение лога активностей
    def set_last_online(self):
        self.last_online = datetime.now()
        Phystech.list_online[self.get_uid()].append(self.last_online)

    def __str__(self) -> str:
        str_repr_lines = [
            f'НаФизтехе. Пользователь \"{self.name}\".',
            'День рождения: {}'.format(
                self._birthday if self._birthday is not None else '(скрыт)'
            ),
            f'Статус: \"{self.status}\".',
            f'Последний раз был онлайн {self.last_online}'
        ]
        if self.is_graduate is not None:
            if self.is_graduate:
                str_repr_lines.append(
                    f'Выпускник {self._graduation_year} года'
                )
        return '\n'.join(str_repr_lines)

    def __repr__(self) -> str:
        return '\n'.join([
            f'name:\t{self.name}'
            f'uid:\t{self.__uid}',
            f'last_online:\t{self.last_online}',
            f'birthday:\t{self._birthday}',
        ])

    # Чтение UID
    def get_uid(self) -> Optional[int]:
        if self.__uid is not None:
            return self.__uid
        else:
            return None

    # Добавление в друзья
    def add_friend(self, uid: int):
        if self.get_uid() not in Phystech.stop_list[uid]:
            self.friends.append(uid)
        else:
            print(f'Вы не можете добавить пользователя с идентификатором {uid} в друзья')
        self.set_last_online()

    # Удаление из списка друзей
    def del_friend(self, uid: int):
        if uid  in self.friends:
            self.friends.pop(uid)
        else:
            print(f'Пользователь с идентификатором {uid} не является вашим другом')
        self.set_last_online()

    # Включение пользователя в стоп-лист
    def set_stop_list(self, uid: int):
        Phystech.stop_list[self.get_uid()].append(uid)
        self.set_last_online()

    # Печать данных о друзьях, стоплисте и списке активностей
    def print_friends(self):
        print('\nМеня зовут', self.name)
        print('Мой список активноcтей ', self.get_uid(), Phystech.list_online[self.get_uid()])
        print('Мой список друзей ', self.friends)
        print('Мой стоп-лист', self.get_uid(), Phystech.stop_list[self.get_uid()])
        self.set_last_online()

    # формирование списка полей
    @property
    def get_fields(self) -> dict:
        return {'UID': self.get_uid(), 'Name': self.name, 'Last_online': self.last_online, 'Birthday': self._birthday,
                'Graduation_year': self._graduation_year, "Friend_list": len(self.friends)}
'''
ovchinkin = Phystech(
    name='Овчинкин Владимир Александрович',
    birthday=datetime(year=1946, month=6, day=9),
    status='Знаете, как много надо знать, чтобы понять, как мало мы знаем.',
    login='ovchinkin',
    graduation_year=2021,
    password='general_physics_rules'
)
paul_simon = Phystech(
    name='Пол Саймон',
    login='paul_simon',
    graduation_year=1986,
    password='I<3English',
    status='Sapere Aude!'
)

landau = Phystech(
    name='Лев Давидович Ландау',
    birthday=datetime(year=1908, month=1, day=22),
    status='Главное – делайте все с увлечением: это страшно украшает жизнь.',
    login='dau',
    password='I<3Physics'
)


ovchinkin.add_friend(landau.get_uid())
ovchinkin.add_friend(paul_simon.get_uid())
ovchinkin.print_friends()
landau.set_stop_list(paul_simon.get_uid())
landau.add_friend(ovchinkin.get_uid())
paul_simon.add_friend(landau.get_uid())
landau.print_friends()
landau.del_friend(ovchinkin.get_uid())
landau.print_friends()
'''
