def can_fit_all(n, w, h, board_size):

    row = board_size // w
    col = board_size // h
    total_leaves = row * col
    return total_leaves >= n

def min_board_size(num_of_leaves, width, height):

    left = min(width, height)
    right = max(width, height) * num_of_leaves
    result = right 
    count = 0 

    while left <= right:
        mid = (left + right) // 2
        if can_fit_all(num_of_leaves, width, height, mid):
            result = mid  
            right = mid - 1  
        else:
            left = mid + 1  
        count += 1

    print(count)
    return result

if __name__ == '__main__':
    result = min_board_size(100_000000, 10_000_000_0000000, 999_999_999)
    print(f'Minimum board size => {result}x{result}')








































"""Viktor Yasin, [10.05.2024 11:51]
Цей код складається з трьох основних частин: двох функцій, які вирішують задачу, і набору тестів, які перевіряють правильність роботи цих функцій.

Функції can_fit_all та min_board_size: Ці функції вирішують задачу знаходження мінімального розміру дошки, на якій можна розмістити певну кількість листків певного розміру. Функція can_fit_all перевіряє, чи можна розмістити всі листки на дошці певного розміру. Функція min_board_size використовує бінарний пошук для знаходження мінімального розміру дошки, на якій можна розмістити всі листки.
Функції quick_sort, food_required та how_much_hamsters_can_you_handle_subtract: Ці функції вирішують задачу визначення максимальної кількості хом’яків, яких можна годувати певною кількістю їжі. Функція quick_sort сортує хом’яків за кількістю їжі, яку вони споживають. Функція food_required обчислює загальну кількість їжі, необхідної для годування певної кількості хом’яків. Функція how_much_hamsters_can_you_handle_subtract використовує ці дві функції для визначення максимальної кількості хом’яків, яких можна годувати.
Тестові випадки: Ця частина коду використовує модуль unittest Python для створення набору тестових випадків, які перевіряють роботу функцій can_fit_all, min_board_size та how_much_hamsters_can_you_handle_subtract. Кожен тестовий випадок викликає одну з цих функцій з певними вхідними даними і перевіряє, чи співпадає отриманий результат з очікуваним.
Цей код демонструє важливі принципи програмування, такі як:

Алгоритми: Функції can_fit_all, min_board_size, quick_sort, food_required та how_much_hamsters_can_you_handle_subtract використовують різні алгоритми для вирішення задач.
Тестування: Модуль unittest використовується для створення тестових випадків, які перевіряють правильність роботи коду.
Бінарний пошук: Функція min_board_size використовує бінарний пошук, що є ефективним алгоритмом пошуку для вирішення цієї задачі.
Сортування: Функція quick_sort використовує алгоритм швидкого сортування, один з найефективніших алгоритмів сортування.
Рекурсія: Функція quick_sort використовує рекурсію, що є важливим концептом в програмуванні.
Умовні оператори: Усі функції використовують умовні оператори (if, else), що є основою багатьох алгоритмів.
Цикли: Функції min_board_size та how_much_hamsters_can_you_handle_subtract використовують цикли (while), що є важливими для ітераційних алгоритмів.
Функціональне програмування: Використання спискових включень у функції quick_sort є прикладом функціонального стилю програмування.
Модульність: Код розбитий на декілька незалежних функцій, що дозволяє легко тестувати і перевикористовувати код.
Тестування: Модуль unittest використовується для створення тестових випадків, які перевіряють правильність роботи коду.
Виключення: Використання оператора print для виведення повідомлення про помилку у функції how_much_hamsters_can_you_handle_subtract є прикладом обробки виключень.
Типізація: Використання анотацій типів у функції food_required допомагає зрозуміти, які типи даних очікується отримати і повернути функцією.
Використання глобальних змінних: Використання глобальних змінних у функції min_board_size є прикладом використання глобального простору імен.
Використання локальних змінних: Використання локальних змінних у всіх функціях є прикладом використання локального простору імен.
Використання параметрів функції: Використання параметрів у всіх функціях є прикладом передачі аргументів до функцій.
Використання значень за замовчуванням: Використання значень за замовчуванням у функції how_much_hamsters_can_you_handle_subtract є прикладом використання значень за замовчуванням.
Використання повернення значень: Використання повернення значень у всіх функціях є прикладом повернення результатів з функцій.
Використання списків: Використання списків у всіх функціях є прикладом використання структур даних.

Viktor Yasin, [10.05.2024 11:54]
Функція quick_sort використовує рекурсію для сортування списку. Ось як це працює:

Базовий випадок: Якщо список містить 0 або 1 елемент, він вже відсортований, тому функція просто повертає список.
Рекурсивний випадок: Якщо список містить більше ніж один елемент, вибирається “опорний” елемент (у цьому випадку - середній елемент списку). Потім список розбивається на три частини:
Елементи, які менші за опорний.
Елементи, які дорівнюють опорному.
Елементи, які більші за опорний.
Рекурсивний виклик: Функція quick_sort викликається рекурсивно для списків елементів, які менші та більші за опорний. Це означає, що функція “викликає сама себе” для цих підсписків.
Об’єднання результатів: Результати рекурсивних викликів (відсортовані підсписки) об’єднуються зі списком елементів, які дорівнюють опорному, щоб отримати відсортований список."""