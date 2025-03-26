def get_int():
    while True:
        try:
            num = int(input(">"))
            if num >= 2 and num <= 10:
                return num
            else:
                print("Enter a number between 2 and 10")
        except ValueError:
            print("Enter a valid number")


numbers = []

for i in range(5):
    print("Enter a number:")
    num = get_int()
    numbers.append(num)

product = numbers[0]
for i in range(1, len(numbers)-1):
    print(f"{product} x {numbers[i]} = {product * numbers[i]}")
    product = product * numbers[i]
    
    
