# 1- Определить, присутствует ли в заданном списке строк, некоторое число

import check as ch 
def check_for_availability():
 lines=ch.get_list()
 print('Введём число для проверки')
 num=ch.get_input_number()
 have_number = [l for x in lines for l in x if l == str(num)]
 print(have_number)
 result = lambda have_number:'Такой элемент есть в списке' if have_number else 'Такого элемента нет'
 print(result(have_number))
check_for_availability() 
