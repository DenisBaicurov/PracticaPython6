#6 - Сформировать список из N членов последовательности.
#Для N = 5: 1, -3, 9, -27, 81 и т.д.
import check as ch

def get_list():
   print (' Введём количество членов последовательности')
   get_len=ch.get_input_number()
   list_res = [(-3) ** i for i in range(get_len)]
   print(f'Сформированный список будет {list_res}')
get_list()   