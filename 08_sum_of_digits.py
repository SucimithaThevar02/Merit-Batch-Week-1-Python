num = abs(int(input("Enter an integer: ")))
digit_sum = 0

while num > 0:
    digit_sum += num % 10
    num //= 10

print("Sum of digits:", digit_sum)
