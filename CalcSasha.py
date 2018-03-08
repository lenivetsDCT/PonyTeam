list = []
while True:
    x = input("Марка машины")
    if x == '':
        break
    y = int(input("Сколько КМ в день?"))
    sum = y * 5 
    if (sum > 50):
        list.append(sum)
print(list.sort(reverse=True))