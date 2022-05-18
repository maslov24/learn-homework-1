"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {
"Привет!"  : 'Привет, друг!',
"Как дела": "Хорошо!", 
"Что делаешь?": "Программирую",
"Что программируешь?": "Программу, ТГ помощник",
"На каком языке пишешь?": "Питон",
"Хорошо программируешь?": "Учусь",
"Нравится программировать?": "Да",
}

def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    user_question = input('Я ТГ помощник! Давай дружить!').strip().lower().capitalize()
    while user_question not in answers_dict:
        user_question = input('Я ТГ помощник! Спрашивайте:').strip().lower().capitalize()
    print(answers_dict[user_question])
    
if __name__ == "__main__":
    ask_user(questions_and_answers)
