# nested loops ➿ = A loop within another loop (outer, inner)

for x in range(3):
    for t in range(1, 10):
        print(t, end="")
    print("")

# Example 1

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print("")