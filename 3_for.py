"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main(x):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    quantity_sold = 0
    quantity_numbers_sold = 0
    for item in x: 
        quantity_items_sold = 0
        
        for i in range(len(item['items_sold'])):
            quantity_items_sold+=item['items_sold'][i]
        average_quantity_items_sold = quantity_items_sold / len(item['items_sold'])
        print(f'''Моделей телефонов {item["product"]}, всего продано: {quantity_items_sold}
                   среднее количество продаж: {round(average_quantity_items_sold,1)}
     ''')
        quantity_sold += quantity_items_sold
        quantity_numbers_sold += len(item['items_sold'])
    average_quantity_sold = quantity_sold // quantity_numbers_sold
    print(f"Количество продаж всех моделей телефонов: {quantity_sold}")
    print(f"Cреднее количество продаж всех моделей телефонов: {average_quantity_sold}")
    # * Посчитать и вывести среднее количество продаж для каждого товара
    # * Посчитать и вывести суммарное количество продаж всех товаров
    # * Посчитать и вывести среднее количество продаж всех товаров

data_sell_fon = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]    
if __name__ == "__main__":
    main(data_sell_fon)
