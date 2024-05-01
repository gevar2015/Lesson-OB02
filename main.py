class User:
    def __init__(self, user_id, name, access_level='user'):
        self._user_id = user_id
        self._name = name
        self._access_level = access_level

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def __str__(self):
        return f"User ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level}"
class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')
        self._user_list = []  # Инициализирует пустой список для хранения объектов пользователей

    def add_user(self, user):
        """Метод для добавления нового пользователя в список управляемых пользователей."""
        self._user_list.append(user)
        print(f"User {user.get_name()} added with ID {user.get_user_id()}.")

    def remove_user(self, user_id):
        """Метод для удаления пользователя из списка по идентификатору."""
        for user in self._user_list:
            if user.get_user_id() == user_id:
                self._user_list.remove(user)
                print(f"User {user.get_name()} removed.")
                return
        print("User not found.")

    def list_users(self):
        """Метод для вывода списка всех пользователей."""
        if self._user_list:
            for user in self._user_list:
                print(user)
        else:
            print("No users in list.")
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
