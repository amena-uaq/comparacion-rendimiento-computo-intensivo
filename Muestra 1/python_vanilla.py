import time

arrays_size = 5000000000

timer_start = time.time()

X = [1 for i in range(arrays_size)]
Y = [2 for i in range(arrays_size)]

[x * y for x, y in zip(X, Y)]

timer_stop = time.time()

print(f"Duración total del programa: {timer_stop - timer_start} segundos")
