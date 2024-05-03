def calculate_sum():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    c = float(input("Введите третье число: "))
    sum_ab = a + b
    sum_abc = sum_ab + c
    print(f'Сумма всех трех чисел равна: {sum_abc}')
    
calculate_sum()
