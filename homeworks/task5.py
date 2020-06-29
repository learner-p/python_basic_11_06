'''5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''

with open('file_task5.txt','w') as file:
    file.write(input('Ввод чисел:\n'))
with open('file_task5.txt') as file2:
    print(sum([int(i) for i in file2.read().split()]))