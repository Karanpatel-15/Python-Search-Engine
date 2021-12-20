'''
Class: COMP 1405Z

Title: Tutorial #4 (Problems 1)
Name: Karan Patel
Student ID: 101218041
'''

def mult_scalar(matrix, scale):

	scalaredMatrix = matrix

	#loop for all rows in matrix
	for row in range(len(matrix)):
		#loop for all column in matrix
		for column in range(len(matrix[row])):
			#update New matrix with scaled value
			scalaredMatrix[row][column] = scale*matrix[row][column]

	#return updated matric
	return scalaredMatrix

def mult_matrix(matrixA, matrixB):
	#if the number of columns in matrixA are the same as number of rows in matrixB then the matrix are valid, otherwise they are not valid
	if(len(matrixA[0]) != len(matrixB)):
		return None

	#initiliza result matrix (multipliedMatrix) using rows of matrixA and columns of matrixB
	multipliedMatrix = [[None for j in range(len(matrixB[0]))] for i in range(len(matrixA))]

	sum = 0
	#Loop for all rows in matrixA
	for rowA in range(len(matrixA)):

		#loop till all columns in MatrixB have been calculated with the current row of matrixA
		for columnB in range(len(matrixB[0])):

			#loop for all columns in current rowA in matrixA
			for columnA in range(len(matrixA[0])):
				#muliply the associated values from both matrixs and add to sum
				sum += matrixA[rowA][columnA] * matrixB[columnA][columnB]

			#update result Matrix and result sum to 0
			multipliedMatrix[rowA][columnB] = sum
			sum = 0

	#return result matrix
	return multipliedMatrix

def euclidean_dist(a,b):
	vectorA = a
	vectorB = b

	#if vector dimentions dont match return None
	if(len(vectorA[0]) != len(vectorB[0])):
		return None

	#sum of everything under squareroot
	underRootSum = 0

	#loop for n dimentions
	for i in range(len(vectorA[0])):
		#add (ai - ai)^2 to underRootSum
		underRootSum += (vectorA[0][i] - vectorB[0][i])**2

	#return Square Root of underRootSum to complete formule
	return underRootSum**(1/2)
