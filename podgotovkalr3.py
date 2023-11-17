# 1
# my_car.go()
# 2
# class Book:
#     def __init__(self, title, author, publisher):
#         self._title = title
#         self._author = author
#         self._publisher = publisher
#
#     def get_title(self):
#         return self._title
#
#     def get_author(self):
#         return self._author
#
#     def get_publisher(self):
#         return self._publisher
#
#     def set_title(self, title):
#         self._title = title
#
#     def set_author(self, author):
#         self._author = author
#
#     def set_publisher(self, publisher):
#         self._publisher = publisher
#
#     def __str__(self):
#         return f"Title: {self._title}, Author: {self._author}, Publisher: {self._publisher}"
#
# book1 = Book("The Catcher in the Rye", "J.D. Salinger", "Little, Brown and Company")
#
# print(book1)
# 3
# class Pet:
# def init(self):
# self._name = None
# self._animal_type = None
# self._age = None
#
#     def set_name(self, name):
#         self._name = name
#
#     def set_animal_type(self, animal_type):
#         self._animal_type = animal_type
#
#     def set_age(self, age):
#         self._age = age
#
#     def get_name(self):
#         return self._name
#
#     def get_animal_type(self):
#         return self._animal_type
#
#     def get_age(self):
#         return self._age
#
# def main():
#     pet = Pet()
#     print("Введите имя вашего домашнего животного:")
#     pet.set_name(input())
#     print("\nВведите тип вашего домашнего животного (например, собака, кот, птица):")
#     pet.set_animal_type(input())
# 5
# class PersonInfo:
#     def __init__(self, name, address, age, phone_number):
#         self.name = name
#         self.address = address
#         self.age = age
#         self.phone_number = phone_number
#
#     def get_name(self):
#         return self.name
#
#     def get_address(self):
#         return self.address
#
#     def get_age(self):
#         return self.age
#
#     def get_phone_number(self):
#         return self.phone_number
#
#     def set_name(self, new_name):
#         self.name = new_name
#
#     def set_address(self, new_address):
#         self.address = new_address
#
#     def set_age(self, new_age):
#         self.age = new_age
#
#     def set_phone_number(self, new_phone_number):
#         self.phone_number = new_phone_number
#
# person1 = PersonInfo("Ваше имя", "Ваш адрес", 25, "Ваш номер телефона")
# person2 = PersonInfo("Имя друга 1", "Адрес друга 1", 30, "Номер телефона друга 1")
# person3 = PersonInfo("Имя друга 2", "Адрес друга 2", 28, "Номер телефона друга 2")
# 6
# class Employee:
#     def __init__(self, name, employee_id, department, position):
#         self.name = name
#         self.employee_id = employee_id
#         self.department = department
#         self.position = position
#
#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"Employee ID: {self.employee_id}")
#         print(f"Department: {self.department}")
#         print(f"Position: {self.position}")
#         print("\n")
#
# employee1 = Employee("Сьюзан Мейерс", 47899, "Бухгалтерия", "Вице-президент")
# employee2 = Employee("Марк Джоунс", 39119, "ИТ", "Программитс")
# employee3 = Employee("Джой Роджерс", 81774, "Производственный", "Инженер")
#
# employee1.display_info()
# employee2.display_info()
# employee3.display_info()
# 7
# class RetailItem:
#     def __init__(self, description, units_in_stock, price):
#         self.description = description
#         self.units_in_stock = units_in_stock
#         self.price = price
#
#     def display_info(self):
#         print("Description:", self.description)
#         print("Units in stock:", self.units_in_stock)
#         print("Price: $", format(self.price, ".2f"))
#
# item1 = RetailItem("Пиджак", 12, 59.95)
# item2 = RetailItem("Дизайнерские джинсы", 40, 34.95)
# item3 = RetailItem("Рубашка", 20, 24.95)
#
# print("Item 1:")
# item1.display_info()
# print("\nItem 2:")
# item2.display_info()
# print("\nItem 3:")
# item3.display_info()
# 9
# class Employee:
#     def __init__(self, emp_id, name, department, position):
#         self.emp_id = emp_id
#         self.name = name
#         self.department = department
#         self.position = position
#
# def add_employee(dictionary):
#     emp_id = input("Введите идентификационный номер сотрудника: ")
#     name = input("Введите имя сотрудника: ")
#     department = input("Введите отдел сотрудника: ")
#     position = input("Введите должность сотрудника: ")
#
#     new_employee = Employee(emp_id, name, department, position)
#     dictionary[emp_id] = new_employee
#     print("Сотрудник добавлен в словарь.")
#
# def find_employee(dictionary):
#     emp_id = input("Введите идентификационный номер сотрудника для поиска: ")
#     if emp_id in dictionary:
#         employee = dictionary[emp_id]
#         print(f"Имя: {employee.name}, Отдел: {employee.department}, Должность: {employee.position}")
#     else:
#         print("Сотрудник не найден.")
#
# def update_employee(dictionary):
#     emp_id = input("Введите идентификационный номер сотрудника для изменения данных: ")
#     if emp_id in dictionary:
#         employee = dictionary[emp_id]
#         print(
#             f"Текущие данные сотрудника - Имя: {employee.name}, Отдел: {employee.department}, Должность: {employee.position}")
#         employee.name = input("Введите новое имя сотрудника: ")
#         employee.department = input("Введите новый отдел сотрудника: ")
#         employee.position = input("Введите новую должность сотрудника: ")
#         print("Данные сотрудника обновлены.")
#     else:
#         print("Сотрудник не найден.")
#
# def remove_employee(dictionary):
#     emp_id = input("Введите идентификационный номер сотрудника для удаления: ")
#     if emp_id in dictionary:
#         del dictionary[emp_id]
#         print("Сотрудник удален из словаря.")
#     else:
#         print("Сотрудник не найден.")
#
# employees_dict = {}
#
# while True:
#     print("\nМеню:")
#     print("1. Найти сотрудника")
#     print("2. Добавить нового сотрудника")
#     print("3. Изменить данные существующего сотрудника")
#     print("4. Удалить сотрудника")
#     print("5. Выйти из программы")
#
#     choice = input("Выберите действие: ")
#
#     if choice == '1':
#         find_employee(employees_dict)
#     elif choice == '2':
#         add_employee(employees_dict)
#     elif choice == '3':
#         update_employee(employees_dict)
#     elif choice == '4':
#         remove_employee(employees_dict)
#     elif choice == '5':
#         print("Программа завершена.")
#         break
#     else:
#         print("Неверный выбор. Пожалуйста, выберите существующий пункт меню.")
