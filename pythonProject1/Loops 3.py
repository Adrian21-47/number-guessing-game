number = int(input("Enter a number: "))

print(f"10 times table for {number}")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")


