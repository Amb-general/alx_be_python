# pattern_drawing.py

# Prompt user for input
size = int(input("Enter the size of the pattern: "))

# Start row counter
row = 0

# Outer loop (while loop for rows)
while row < size:
    # Inner loop (for loop for columns)
    for col in range(size):
        print("*", end="")  # print star without new line
    print()  # move to the next line after each row
    row += 1

