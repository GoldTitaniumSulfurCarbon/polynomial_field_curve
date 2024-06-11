

num_points = int(input("How many data points do you have? "))
point_list = [] #Creates an empty list containing tuples of the points.
augmented_matrix = [[0]*(num_points+1)]*num_points

for i in range (num_points): #Gets input from user, and stores the x and y values into a tuple.
    x = int(input("X value: "))
    y = int(input("Y value: "))
    ith_point = (x, y)
    point_list.append(ith_point)
    print(point_list)


# Now for the actual testing
print(f"The matrix to solve for is:\n") # The "matrix" here is only for display purposes. IT CANNOT BE USED TO SOLVE FOR RREF OR PLOT WITHIN THE CLASS.
#THIS CAN ONLY BE USED TO PLUG IN TO ANOTHER MATRIX CALCULATOR FOR THE TIME BEING (ie: TI84 or WolframAlpha)
for i in range (num_points): # column
    power = num_points # Gets the power based on amount of points given, then fills each row with x^(n-1) points, with the exponent decrasing every collumn for the coefficient matrix.
    # Final collumn is the y value of the tuple, and the equality to solve for in the augmented matrix.
    for j in range (num_points): # row
        x_value = point_list[i][0]
        augmented_matrix[i][j] = pow(x_value, (power-1))
        power -=1
    augmented_matrix[i][num_points] = point_list[i][1]
    print(augmented_matrix[i])# Prints out Each row individually when done. This will give the proper augmented matrix as a display, but the actual 2d list is bugged.





#Prints out the augmented matrix. Not functional, as every row is the final one.
#for i in range(num_points):
#   print(augmented_matrix[i])
