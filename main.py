import math

# Ввод коэффициентов
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

# Вычисление дискриминанта
discriminant = b**2 - 4 * a * c

# Проверка количества корней
if discriminant > 0:
  # Два различных корня
  x1 = (-b + math.sqrt(discriminant)) / (2 * a)
  x2 = (-b - math.sqrt(discriminant)) / (2 * a)
  print(f"Уравнение имеет два корня: x1 = {x1:.2f}, x2 = {x2:.2f}")
elif discriminant == 0:
  # Один корень (кратный)
  x = -b / (2 * a)
  print(f"Уравнение имеет один корень: x = {x:.2f}")
else:
  # Нет действительных корней
  print("Уравнение не имеет корней")