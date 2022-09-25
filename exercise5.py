# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import check as ch

def get_list_result():
  list_number=[]   
  print('Введите длину списка')
  get_len=ch.get_input_number()
  for i in range(0,get_len):
    list_number.append(ch.get_real_number())
  print(f' Искомый список {list_number}')
  list_result = [list_number[i]* list_number[-1-i] for i in range(len(list_number)//2 + len(list_number)%2)]
  print(f' Произведение пар чисел в списке {list_result}')
get_list_result()  