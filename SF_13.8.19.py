quantity_ticket = int(input("Введите количество билетов: "))

all_price = 0

for i in range(quantity_ticket):
  age = int(input(f"Введите возраст для {i+1} билета: "))
  if 18 <= age < 25:
    all_price += 990
  elif age >= 25:
    all_price += 1390

if quantity_ticket > 3:
  all_price = all_price - all_price * 0.1
  print(f"Стоимость всех билетов = {int(all_price)} руб, c учётом скидки в 10%")
else:
  print(f"Стоимость всех билетов = {int(all_price)} руб")

