list = []
while True:
    x = input("Марка машины")
    y = int(input("Сколько КМ в день?"))
    if y > 50: 
        list.append(y)
    if y == '':
        break
    sum = y * 5
    print(x , sum)