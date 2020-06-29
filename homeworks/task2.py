'''2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.'''

file = open('file_task2', 'r')
try:
    text=file.readlines()
    print(f'Количество строк равно {len(text)}')
    for n,line in enumerate(text,1):
        words=line.split()
        print(f'Количество слов в строке {n} равно {len(words)}')
except:
    raise
finally:
    file.close()