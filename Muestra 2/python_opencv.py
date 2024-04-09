import numpy
import cv2
import time

raw_data = cv2.imread("./Samuel_Zeller_Tokyo_DSCF3800.JPG")

timer_start = time.time()
resultant_data = cv2.GaussianBlur(raw_data, (127, 127), 27)
timer_stop = time.time()

cv2.imwrite("python_opencv_Samuel_Zeller_Tokyo_DSCF3800.JPG", resultant_data)
print(f"Duración total del programa: {timer_stop - timer_start} segundos")