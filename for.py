"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    my_list = [
        {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
        {'school_class': '4b', 'scores': [4, 7, 1, 6, 7]},
        {'school_class': '4c', 'scores': [4, 7, 1, 6, 7, 9, 1]},
        {'school_class': '4d', 'scores': [1, 1, 1]},
    ]

    total_sum = 0
    total_len = 0
    for x in my_list:
        cur_len = len(x["scores"])
        cur_sum = sum(x["scores"])
        if not cur_len:
            raise ValueError
        print(f'avg for {x["school_class"]}: {cur_sum / cur_len}')
        total_len += cur_len
        total_sum += cur_sum
    print(f'total: {total_sum / total_len}')

if __name__ == "__main__":
    main()
