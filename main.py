class User:
    def __init__(self, user_id, name, access_level='user'):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_access_level(self):
        return self.__access_level

    def set_access_level(self, access_level):
        self.__access_level = access_level


class Admin(User):
    def __init__(self, user_id, name, access_level='admin'):
        super().__init__(user_id, name, access_level)
        self.__user_list = []

    def add_user(self, user):
    # Добавляет пользователя в список.
        self.__user_list.append(user)

    def remove_user(self, user):
    # Удаляет пользователя из списка.
        if user in self.__user_list:
            self.__user_list.remove(user)
            print(f"Пользователь {user.get_name()} удален из списка.")
        else:
            print("Такого пользователя нет в списке.")

    def list_users(self):
    # Выводит список пользователей.
        print("Список пользователей:")
        for user in self.__user_list:
            print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")


# Пример использования
if __name__ == "__main__":
    # Создаем обычных пользователей
    user1 = User(1, "John")
    user2 = User(2, "Alice")
    user3 = User(3, "Bob")

    # Создаем администратора
    admin = Admin(0, "Admin")

    # Добавляем пользователей в список администратора
    admin.add_user(user1)
    admin.add_user(user2)
    admin.add_user(user3)

    # Выводим список пользователей
    admin.list_users()

    # Удаляем пользователя из списка
    admin.remove_user(user2)

    # Выводим обновленный список пользователей
    admin.list_users()
