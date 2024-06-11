# TODO: With the fixed array, convert it into a matrix, get it in reduced row-echelon form, then extract the final column as coefficients
import numpy
import sympy
num_points = int(input("How many data points do you have? "))
point_list = [] #Creates an empty list containing tuples of the points.
augmented_matrix = [[0]*(num_points+1)]*num_points

for i in range (num_points): #Gets input from user, and stores the x and y values into a tuple.
    x = int(input("X value: "))
    y = int(input("Y value: "))
    ith_point = (x, y)
    point_list.append(ith_point)


# Now for the actual testing
for i in range (num_points): # column
    power = num_points # Gets the power based on amount of points given, then fills each row with x^(n-1) points, with the exponent decrasing every collumn for the coefficient matrix.

    row = [0] * (num_points + 1) # Placeholder row to fill up
    for j in range(num_points):  # row
        x_value = point_list[i][0]
        row[j] = pow(x_value, (power - 1))
        power -= 1
    augmented_matrix[i] = row
    augmented_matrix[i][num_points] = point_list[i][1]  # Sets the final column to be equal to the y-values of the points, to satisfy the system of equations


matrix = numpy.matrix(augmented_matrix)
rref_matrix = sympy.Matrix(matrix).rref()
rref_list = numpy.array(rref_matrix[0].tolist(), dtype=float) # Only gets the matrix, and converts into float
print(f"Polynomial Coefficients after reduced row-echelon form:")
for i in range (num_points):
    print(f"Coefficient {i+1}: {rref_list[i][num_points]}")