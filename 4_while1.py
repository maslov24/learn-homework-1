"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user(answer):
    """
    Замените pass на ваш код
    """
    while answer != "Хорошо":
        print("На вопрос 'Как дела?', отвечают: 'Хорошо'")
        answer = input("Как дела?")

    
if __name__ == "__main__":
    hello_user(input("Как дела?"))
