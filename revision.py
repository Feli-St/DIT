numbers = []

for i in range(5):
    print("Enter a number:")
    num = int(input(">"))
    numbers.append(num)

product = numbers[0]
for i in range(len(numbers)-2):
    print(f"{product} x {numbers[i+1]} = {product * numbers[i+1]}")
    product = product * numbers[i+1]
    
    
