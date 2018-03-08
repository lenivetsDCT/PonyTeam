# x = input("Input x: ")
# print(x)

# x = int(input("Enter x: "))
# y = int(input("Enter y: ")) 
# sum = x + y
# print('Sum: ', sum, "LOLO")

models = ['Tesla', 'VW', 'BMW', 'Mercedes']
run_list = ['5', '7', '2', '1']

list = []
for model in models:
    run_element = models.index(model)
    total_km = int( run_list[run_element] ) * 5
    if (total_km > 15): 
        list.append(total_km)
print(sorted(list, reverse=True))