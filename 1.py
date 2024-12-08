grade = int(input("Яку оцінку ти отримав? "))
if grade < 49:
    print("Незадовільно")
elif 50 <= grade <=69:
    print("Задовільно")
elif 70<= grade <= 89:
    print("Добре")
elif 90<= grade <= 100:
    print("Відмінно")

a = int(input("Напиши перше число: "))
b = int(input("Напиши друге число: "))
operation = input("Напиши математичну дію: ")
if operation == '+':
    print(a+b)
elif operation == '-':
    print(a-b)
elif operation == '*':
    print(a*b)
elif operation == '/':
    if b == 0:
        print("Помилка: ділення на нуль.")
