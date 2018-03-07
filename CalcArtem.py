# x = input("Input x: ")
# print(x)

# x = int(input("Enter x: "))
# y = int(input("Enter y: ")) 
# sum = x + y
# print('Sum: ', sum, "LOLO")

list = []
while True:
    x = input("Enter brand: ")
    if (len(x) > 5): 
        list.append(x)
    if x == '':
         break
print(list)