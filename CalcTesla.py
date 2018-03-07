list = []
while True:
    x = input("Какая модель авто?: ")
    if x=='':
        break
    y = int(input("Сколько км до работы?"))
    sum = y * 5
    if (sum > 50):
       list.append(x)
print(list)
