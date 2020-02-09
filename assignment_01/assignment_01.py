import numpy as np
import fileinput

def read_input():
    lines = []
    for line in fileinput.input():
        lines.append(line.strip().replace(" ", ""))
    return lines

def read_matrix():
    matrix = [] 
    f = open("matrix1.txt", "r")
    for x in f:
        matrix.append(x.strip().split(","))
    f.close()
    return np.array(matrix)

def print_matrix(A):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in A]))

def find_coordinates(A, element):
    x, y = np.where(A == element) 
    return x[0], y[0]

def find_letter(A, coordinates):
    return A[coordinates[0],coordinates[1]]

def encrypt(text):
    text_list = list(text)
    A = read_matrix()
    coordinates = [find_coordinates(A, x) for x in text_list]
    x_coordinates, y_coordinates = zip(*coordinates)
    mixed_coordinates = x_coordinates + y_coordinates
    paired_coordinates = [mixed_coordinates[i:i + 2] for i in range(0, len(mixed_coordinates), 2)]
    message = [find_letter(A, c) for c in paired_coordinates]
    print(''.join([str(elem) for elem in message]))

def decrypt(text):
    text_list = list(text)
    A = read_matrix()
    coordinates = [find_coordinates(A, x) for x in text_list]
    mixed_coordinates = [elem for coord in coordinates for elem in coord]
    x_coordinates = mixed_coordinates[:len(mixed_coordinates)//2]
    y_coordinates = mixed_coordinates[len(mixed_coordinates)//2:]
    original_coordinates = zip(x_coordinates,y_coordinates)
    message = [find_letter(A, c) for c in original_coordinates]
    print(''.join([str(elem) for elem in message]))



method, text = read_input()

if(method == "ENCRYPT"):
    encrypt(text) 
else:
    decrypt(text)