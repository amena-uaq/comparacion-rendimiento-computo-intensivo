import time
import numpy
import cupy

matrix_size = 100000
chunk_size = 100
submatrix_size = 1000

timer_start = time.time()

first_matrix = numpy.full((matrix_size, matrix_size), 1, dtype=cupy.float32)
second_matrix = numpy.full((matrix_size, matrix_size), 2, dtype=cupy.float32)


for i in range(chunk_size):
    cpu_submatrix_first = first_matrix[
        i * submatrix_size : (i + 1) * submatrix_size, :submatrix_size
    ]

    cpu_submatrix_second = second_matrix[
        i * submatrix_size : (i + 1) * submatrix_size, :submatrix_size
    ]

    gpu_submatrix_first = cupy.asarray(cpu_submatrix_first)
    gpu_submatrix_second = cupy.asarray(cpu_submatrix_second)

    cupy.dot(gpu_submatrix_first, gpu_submatrix_second)

timer_stop = time.time()

print(f"Duración total del programa: {timer_stop - timer_start} segundos")
