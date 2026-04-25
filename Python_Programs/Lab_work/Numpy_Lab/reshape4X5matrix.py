import numpy as np

# Step 1: Create numbers from 1 to 20
numbers = np.arange(1, 21, 1)

# Step 2: Check total elements
if numbers.size == 20:
    
    # Step 3: Reshape into 4 rows and 5 columns
    matrix = numbers.reshape(4, 5)
    
    # Step 4: Print the matrix
    print("4 x 5 Matrix is:")
    for row in matrix:
        for element in row:
            print(f"{element:2}", end=" ")
        print()

else:
    print("Error: Number of elements is not correct.")
    
    #output
 #4 x 5 Matrix is:
 
 #1  2  3  4  5 
 #6  7  8  9 10 
#11 12 13 14 15 
#16 17 18 19 20 