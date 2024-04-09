import time
import numpy

matrix_size = 100000

timer_start = time.time()

first_matrix = numpy.full((matrix_size, matrix_size), 1, dtype=numpy.float32)
second_matrix = numpy.full((matrix_size, matrix_size), 2, dtype=numpy.float32)

numpy.dot(first_matrix, second_matrix)

timer_stop = time.time()
print(f"Duración total del programa: {timer_stop - timer_start} segundos")
