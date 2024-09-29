input_data = open('input.txt', 'r') 

X = input_data.read() 

#--------------------------------------------------------------------
a = 1
a = int(a)
X = int(X)
n = X
n = int(X)
S = (float((a + X)/2)*n)


#--------------------------------------------------------------------
output_data = open('output.txt', 'w') # Открываем для записи (литера 'w') файл и кладем его в переменную
output_data.write (str(int(S)))

# ВАЖНО!!! 
# не забываем закрывать открытые ранее файлы!
input_data.close() 
output_data.close()