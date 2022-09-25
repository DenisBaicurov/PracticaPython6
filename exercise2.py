# 2 - Найти сумму чисел списка стоящих на нечетной позиции
import check as ch
import random
def sum_of_odd_elements():
  get_mylist = [] 
  print ('получим размер списка')
  get_lengh=ch.get_input_number()
  for i in range(0,get_lengh):
    get_mylist.append(random.randint(-10,10))
  print (f'Получаем список {get_mylist}')
  odd_elements = [get_mylist[i] for i in range(len(get_mylist)) if i % 2 ==1]
  print(f'Сумма элементов на нечётной позиции будет{sum(odd_elements)}')
sum_of_odd_elements()  