b1 = float(input("Введіть перший член (b1): "))
q = float(input("Введіть знаменник (q): "))
n = int(input("Введіть кількість членів (n): "))

current_b = b1

print(f"Перші {n} члени геометричної прогресії:")
for i in range(n):
     print(current_b, end=" ")
     current_b *= q

