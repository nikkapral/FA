"""
(15 баллов) Напишите функцию, которая для строки вида 
«Иванов: 100, 45, 89 вычисляет сумму баллов.
Строка является параметром функции.
Функция возвращает вычисленное целое число.
"""

def counter(input_str):
    
    #Разделение строки на список и определение переменных
    name, values = input_str.split(": ")

    #Список кол-вом баллов
    values_list = values.split(", ")

    #Конвертация каждого элемента списка в целочисленный тип
    values_list = [int(x) for x in values_list]

    #Возврат суммы баллов
    return sum(values_list)


if __name__ == "__main__":
    result = counter("Иванов: 100, 45, 89")
    print(result)