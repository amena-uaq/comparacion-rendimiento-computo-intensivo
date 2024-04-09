import time
import numpy
import cupy

arrays_size = 5000000000
chunk_size = 1000000000

timer_start = time.time()

for i in range(0, arrays_size, chunk_size):
    chunk_start = i
    chunk_end = min(i + chunk_size, arrays_size)

    stream_X = cupy.cuda.Stream(non_blocking=True)
    stream_Y = cupy.cuda.Stream(non_blocking=True)

    with stream_X:
        gpu_X_chunk = cupy.full(chunk_end - chunk_start, 1, dtype=numpy.float32)
    with stream_Y:
        gpu_Y_chunk = cupy.full(chunk_end - chunk_start, 2, dtype=numpy.float32)

    stream_X.synchronize()
    stream_Y.synchronize()

    cupy.multiply(gpu_X_chunk, gpu_Y_chunk)


timer_stop = time.time()

print(f"Duración total del programa: {timer_stop - timer_start} segundos")
