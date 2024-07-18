# Print the Traingle Pattern

# To store the number of rows
rows=5

# Outer loop for rows
for i in range(1,rows+1):
    # Inner loop for columns
    for j in range(1,i+1):
        print("*",end="")
