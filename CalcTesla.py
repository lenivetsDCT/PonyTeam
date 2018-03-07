list = []
while True:
    x = input("Какая модель авто?: ")
    y = int(input("Сколько км до работы?"))
    sum = y * 5
    if (len(x) > 50):
       list.append(x)
    if x=='':
       break
 print(list)
