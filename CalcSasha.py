list = []
while True:
    x = input("Марка машины")
    y = int(input("Сколько КМ в день?"))
    sum = y * 5 
    if (sum > 50):
        list.append(x)
    if x == '':
        break
    print(list)