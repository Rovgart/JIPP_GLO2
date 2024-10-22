import re
import numpy as np

# # Listy skadane

# numbers= [1,2,3,4,5,6]
# result= [x**2 for x in numbers if x%2 ==0]

# result1= list(map(lambda x:x*2, numbers))
# print(result1)

# result2= list(filter(lambda x:x%2==0, numbers))
# print(result2)

# reduce(lambda x,y: x+y, numbers)


# Zadanie 1 

# def task1(text):
#     paragraph= text.strip().split('\n')
#     numParagraph= len(paragraph)
    
#     #zdania 
#     zdania= text.strip().split('.')
#     zdanie= re.split(pattern=r'[.!?]+', text)
#     numZdania
    
    

def validate_addition(matrix1, matrix2):
    return matrix1.shape == matrix2.shape

def validate_multiplication(matrix1, matrix2):
    return matrix1.shape[1] == matrix2.shape[0]

def add_matrices(matrix1, matrix2):
    if validate_addition(matrix1, matrix2):
        return np.add(matrix1, matrix2)
    else:
        raise ValueError("Macierze muszą mieć te same wymiary do dodawania.")

def multiply_matrices(matrix1, matrix2):
    if validate_multiplication(matrix1, matrix2):
        return np.dot(matrix1, matrix2)
    else:
        raise ValueError("Liczba kolumn pierwszej macierzy musi być równa liczbie wierszy drugiej macierzy.")

def transpose_matrix(matrix):
    return np.transpose(matrix)

def execute_operation(operation_str):
    try:
        return eval(operation_str)
    except Exception as e:
        raise ValueError(f"Nieprawidłowa operacja: {e}")

matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

def main(operation):
    try:
        result = execute_operation(operation)
        print("Wynik operacji:")
        print(result)
    except ValueError as e:
        print(f"Błąd: {e}")


if __name__ == "__main__":

    operation_add = "add_matrices(matrix_a, matrix_b)"
    operation_multiply = "multiply_matrices(matrix_a, matrix_b)"
    operation_transpose = "transpose_matrix(matrix_a)"

    main(operation_add)

    main(operation_multiply)

    main(operation_transpose)
