import tkinter as tk

def calculate_sum():
    a = float(entry1.get())
    b = float(entry2.get())
    c = float(entry3.get())
    sum_ab = a + b
    sum_abc = sum_ab + c
    result_label.config(text=f'Сумма всех трех чисел равна: {sum_abc}')

# Создание графического интерфейса
root = tk.Tk()
root.title("Сумма чисел")

# Поля для ввода чисел
entry1 = tk.Entry(root)
entry1.pack()
entry2 = tk.Entry(root)
entry2.pack()
entry3 = tk.Entry(root)
entry3.pack()

# Кнопка для расчета суммы
calculate_button = tk.Button(root, text="Посчитать", command=calculate_sum)
calculate_button.pack()

# Место для отображения результата
result_label = tk.Label(root, text="")
result_label.pack()

# Запуск главного цикла
root.mainloop()

