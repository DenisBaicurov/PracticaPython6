# Делаем прверку на ввод числа
def get_input_number():
    while True:
        input_number=input('Введите целое положительное число,больше 0 \n')
        if not input_number.isnumeric():
            print ('Неправильный ввод числа, повторите ввод')
        elif int(input_number)==0:
            print('Число не должно быть 0, повторите ввод')      
        else :
            break
    return int(input_number)  
def get_list():
    print ('Введите размер списка')
    get_number=get_input_number()
    lines=[input('Введите элемент массива: ') for _ in range(get_number)]
    return lines
    
  
        
      