import time
import numpy

arrays_size = 5000000000

timer_start = time.time()

X = numpy.full(arrays_size, 1, dtype=numpy.float32)
Y = numpy.full(arrays_size, 2, dtype=numpy.float32)

X * Y

timer_stop = time.time()

print(f"Duración total del programa: {timer_stop - timer_start} segundos")
