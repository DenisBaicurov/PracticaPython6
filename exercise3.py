#3 - Найти расстояние между двумя точками пространства(числа вводятся через пробел)

from re import T


def get_point(message)->list:
  
    print(' Получение координат точки \n в виде списка')
    while True:
       try: 
        coordinate=input(message)  
        get_lst=list(map(float,coordinate.split(' '))) 
        return get_lst
       except ValueError:
        print('Неверный ввод')
        continue 
      
point_a=get_point('Введите координаты точки (числа вводятся через пробел)') 
point_b=get_point('Введите координаты точки (числа вводятся через пробел)')   

result=round(sum([(j-i)**2 for i,j in zip(point_a,point_b)])**0.5, 2) 
print(f'Расстояние между 2 точками равно= {result}') 
   