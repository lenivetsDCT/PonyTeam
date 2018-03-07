list = []
while True:
    y = input("Какая модель авто?: ")
    x = int(input("Сколько км до работы?"))
    sum = y * 5
    if (len(x) > 50):
       list.append(x)
    if x=='':
       break
 print(list)
