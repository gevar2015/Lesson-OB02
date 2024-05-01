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