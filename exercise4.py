# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


def search_for_a_second():
 get_string = ["asd",'qwe', "zxc",'qwe', "ertqwe"] #ищем: "qwe"
 get_search_string = "qwe"

 try:
    second_element = [x for x in range(len(get_string))[get_string.index(get_search_string)+1::] if get_string[x] == get_search_string]
    if second_element:
        print (f'Второе вхождение элемента под индексом: {second_element[0]}')
    else:
        print('Данного элемента нет')
 except ValueError:
    print('Такого элемента нет в списке')
search_for_a_second()    