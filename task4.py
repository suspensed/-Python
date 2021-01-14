a = int(input())
b = []
while a > 0:
  b.append(a % 10)
  a = a // 10
highest = max(b)
print(f'Самое большое число: {highest}')

