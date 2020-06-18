user_list=[]
while True:
    input_element=input('Ввод элементов списка. Для завершения ввода нажать Enter: ')
    if input_element=='':
        break
    else:
        user_list.append(input_element)

print(user_list)
new_index=1
new_list=[]

for element in user_list:
    if user_list.index(element)%2==1:
        new_list.append(element)
for element in user_list:
    if user_list.index(element)%2==0:
        new_list.insert(new_index,element)
    new_index+=1
print(new_list)


