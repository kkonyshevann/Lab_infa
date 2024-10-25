money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
month = 0
if spend <= salary + money_capital:
    month += 1
    money_capital = money_capital - (spend - salary)

for i in range(1,100):
    spend += spend * 0.05
    if spend <= salary + money_capital:
        month += 1
        money_capital = money_capital - (spend - salary)
    else:
        print("Количество месяцев, которое можно протянуть без долгов:", month)
        break



