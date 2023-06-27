"""
Вы пользуетесь общественным транспортом?
Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no

"""
num = input("Введите 6-ти значное число: ")
if int(num) in range(100000, 1000000):
    sum1 = int(num[0]) + int(num[1]) + int(num[2])
    sum2 = int(num[3]) + int(num[4]) + int(num[5])
    if sum1 == sum2 :
        print("yeah!")
    else:
        print("no(")
else:
    print("Введено некорректное число!")
