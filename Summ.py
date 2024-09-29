input_data = open('input.txt', 'r') 

n = input_data.read()  
#--------------------------------------------------------------------
Sum = 0
n = int(n)
if n > 0:
    for i in range(1, n + 1):
        Sum += i
else:
    for i in range(n, 2):
        Sum += i
#--------------------------------------------------------------------
output_data = open('output.txt', 'w') # Открываем для записи (литера 'w') файл и кладем его в переменную
output_data.write (str(Sum))

# ВАЖНО!!! 
# не забываем закрывать открытые ранее файлы!
input_data.close() 
output_data.close()