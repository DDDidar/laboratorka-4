pos = int (input("Введите кол-во элементов последовательности: "))
count = 1
if pos == 0:
    print("Введите кол-во элементов последовательности верно")
else:
    xpos = int (input("Введите первый член последовательности: "))
    ipos = 0
    sumpos = xpos
 
    for ipos in range(pos - 1):   
        if pos == 0:
                break
    else:
        for ipos in range(pos - 1): 
            for ipos in range(pos != 0):   
                if pos == 0:
                    break
                else:
                    pos -= 1
                    xpos = input("Следующее число: ")
                    count += 1
                    sumpos += int (xpos)   
                    ipos = ipos + 1
            
print("Сумма = " + str (sumpos))
print("Кол-во элементов = " + str (count))
