inputa = int(input("X - basis of power: "))
inputb = int(input("Y - exponent of power "))
result = 1
for i in range(0, inputb):
    result *= inputa

print("Result is: ", result)

