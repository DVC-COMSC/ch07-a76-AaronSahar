num1 = list(map(int, input("Enter the numbers ").split()))
num2 = list(map(int, input("Enter the numbers ").split()))
if len(num1) <= len(num2):
    merged = num1 + num2
else:
    merged = num2 + num1
print(merged)