class User:
    # Конструктор класса с инициализацией ID пользователя, имени и уровня доступа.
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'  # Переменная, устанавливающая начальный уровень доступа как 'user'.

    # Метод для получения ID пользователя.
    def get_user_id(self):
        return self._user_id

    # Метод для получения имени пользователя.
    def get_name(self):
        return self._name

    # Метод для установки нового имени пользователя.
    def set_name(self, name):
        self._name = name

    # Метод для получения уровня доступа пользователя.
    def get_access_level(self):
        return self._access_level

    # Метод для представления объекта в виде строки.
    def __str__(self):
        # Возвращает форматированную строку с данными пользователя.
        return f"User ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level}"

    class Admin(User):
        # Конструктор класса, который также наследует от класса User.
        def __init__(self, user_id, name):
            super().__init__(user_id,
                             name)  # Вызывает конструктор базового класса User для инициализации user_id и name.
            self._access_level = 'admin'  # Устанавливает уровень доступа специфичный для администраторов.
            self._user_list = []  # Инициализирует пустой список для хранения объектов пользователей.

        # Метод для добавления нового пользователя в список управляемых пользователей.
        def add_user(self, user):
            self._user_list.append(user)
            print(f"User {user.get_name()} added with ID {user.get_user_id()}.")

            # Метод для удаления пользователя из списка по идентификатору.

        def remove_user(self, user_id):
            for user in self._user_list:  # Перебирает список пользователей.
                if user.get_user_id() == user_id:
                    self._user_list.remove(user)
                    print(f"User {user.get_name()} removed.")  # Выводит информацию об удалении пользователя.
                    return  # Прерывает цикл после удаления пользователя.
            print("User not found.")  # Выводит сообщение, если пользователь с заданным ID не найден.

        # Метод для вывода списка всех пользователей.
        def list_users(self):
            for user in self._user_list:  # Перебирает всех пользователей в списке.
                print(user)  # Выводит информацию о каждом пользователе (вызывается метод __str__ класса User).

# Создаем администратора
admin = Admin('001', 'Alice')

# Создаем несколько пользователей
user1 = User('002', 'Bob')
user2 = User('003', 'Charlie')

# Админ добавляет пользователей
admin.add_user(user1)
admin.add_user(user2)

# Вывод списка пользователей
admin.list_users()

# Удаление пользователя
admin.remove_user('002')

# Вывод обновленного списка пользователей
admin.list_users()