'''2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.'''

def profile(**params):
    print(params)

print(profile(firsname=input('firsname: '),lastname=input('lastname: '), birthyear=input('birthyear: '), city=input('city: '), email=input('email: '), phone=input('phone: ')))