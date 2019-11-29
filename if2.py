"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""


def comparator(str1: str, str2: str) -> int:
    if not (isinstance(str1, str) and (isinstance(str2, str))):
        return 0;
    if str1 == str2:
        return 1
    if len(str1) > len(str2):
        return 2
    if str2 == 'learn':
        return 3
    return -1

def main():

    print(comparator(10, 'aaaa'))
    print(comparator({}, []))
    print(comparator('aaaa', 'aaaa'))
    print(comparator('aaaaa', 'aaaa'))
    print(comparator('aaaaa', 'learn'))
    print(comparator('aaaa', 'aaaaaaa'))

    
if __name__ == "__main__":
    main()
