import sys
times = 0
num = 0
try:
    num = float(input("Enter the number : "))
    times = int(input("Enter the number of times you want to multiply the number: "))
except ValueError:
    print("[Error] - Invalid Input")
    sys.exit
ans = 0
if num >= 1:
    for i in range(1, times + 1):
        ans = num * i
        print(f"{num} * {i} = {ans}")
else: 
    print("Please enter a positive value. ")