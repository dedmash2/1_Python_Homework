"""
Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
Сколько журавликов сделал каждый ребенок, если известно,
что Петя и Сережа сделали одинаковое количество журавликов,
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

*Пример:*

6 -> 1 4 1
24 -> 4 16 4
60 -> 10 40 10

"""

S = int(input("Введите количество журавликов: "))
if S % 6 == 0:
    print(f"Петя и Серёжа сделали по {S//6}, а Катя сделала {S//6*4}.")
else:
    print("Введите число кратное 6!")
