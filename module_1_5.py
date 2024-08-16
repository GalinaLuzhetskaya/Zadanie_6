immutable_var = 1, 2, 'a', 'b'
print("Immutable tuple: ", immutable_var)
#immutable_var[0] = 20    объект "кортеж" не поддерживает назначение элементов
#print(immutable_var)
mutable_list = [1, 2, 'a', 'b']
print("Mutable list:", mutable_list)
mutable_list.append('Modified')
print("Mutable list:", mutable_list)