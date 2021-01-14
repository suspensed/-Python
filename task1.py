#cd C:\Users\79632\desktop\python\GeekBrains

#1 
a = "1"
b = 2
try:
    c = int(input("введите число "))
except ValueError:
    print('вы ввели строку.')


d = input("Введите строку ")

print(a, b, c, d)