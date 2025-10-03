"""
Завдання 6. Жадібні алгоритми та динамічне програмування
Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм та алгоритм динамічного програмування для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.
Кожен вид їжі має вказану вартість і калорійність. Дані про їжу представлені у вигляді словника, де ключ — назва страви, а значення — це словник з вартістю та калорійністю.

items = {
  "pizza": {"cost": 50, "calories": 300},
  "hamburger": {"cost": 40, "calories": 250},
  "hot-dog": {"cost": 30, "calories": 200},
  "pepsi": {"cost": 10, "calories": 100},
  "cola": {"cost": 15, "calories": 220},
  "potato": {"cost": 25, "calories": 350}
}

Розробіть функцію greedy_algorithm жадібного алгоритму, яка вибирає страви, максимізуючи співвідношення калорій до вартості, не перевищуючи заданий бюджет.
Для реалізації алгоритму динамічного програмування створіть функцію dynamic_programming, яка обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті.
"""


def greedy_algorithm(products, money):
    product_calories = {}

    for key, params in products.items():
        pr = params.copy()
        pr.update({"calories/cost": params["calories"]/params["cost"]})
        product_calories.update({key: pr})

    product_calories = dict(sorted(product_calories.items(
    ), key=lambda item: item[1]["calories/cost"], reverse=True))
    print(product_calories)

    rest_money = money
    result = {}
    calories = 0

    for product, params in product_calories.items():
        if rest_money >= params["cost"]:
            count_product = rest_money // params["cost"]
            rest_money = rest_money % params["cost"]
            calories += params["calories"] * count_product
            result.update({product: count_product})
        if rest_money == 0:
            break

    return (result, calories)


def dynamic_programming(products, money):
    result = {}
    max_calories = [0] + [0] * (money // 5)
    last_used_product = [0] * (money // 5 + 1)

    for s in range(5, money+1, 5):
        for product, data in products.items():
            cost = data['cost']
            calories = data['calories']
            if s >= cost and max_calories[s//5 - cost // 5]+calories > max_calories[s//5]:
                max_calories[s//5] = max_calories[(s-cost) // 5] + calories
                last_used_product[s//5] = product
    # print(max_calories)
    # print(last_used_product)

    current_sum = money
    calories = 0
    while current_sum >= 10:
        product = last_used_product[current_sum // 5]
        cost = products[product]["cost"]
        result[product] = result.get(product, 0) + 1
        current_sum = current_sum - cost
        calories += products[product]["calories"]

    return (result, calories)


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

print(greedy_algorithm(items, 325))
print(dynamic_programming(items, 325))
