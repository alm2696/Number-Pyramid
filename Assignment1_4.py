# Define the number of rows for the pattern
num_rows = 5

# Loop through each row
for x in range(1, num_rows + 1):
    # Print leading spaces
    for y in range(num_rows - x):
        print("  ", end="")
    
    # Print numbers in increasing order
    for y in range(1, x + 1):
        print(y, end=" ")

    # Print numbers in decreasing order (excluding 1 for the last iteration)
    for y in range(x - 1, 0, -1):
        print(y, end=" ")
    
    # Move to the next line for the next row
    print()
