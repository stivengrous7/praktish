a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

print("Выберите операцию:")
print("+  сложение")
print("-  вычитание")
print("*  умножение")
print("/  деление")

op = input("Операция: ")

if op == "+":
    print("Результат:", a + b)
elif op == "-":
    print("Результат:", a - b)
elif op == "*":
    print("Результат:", a * b)
elif op == "/":
    if b != 0:
        print("Результат:", a / b)
    else:
        print("Ошибка: деление на ноль")
else:
    print("Неизвестная операция")
    
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        raise ValueError("Деление на ноль")
    return a / b
