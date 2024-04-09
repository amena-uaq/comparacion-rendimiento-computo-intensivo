import numpy
import cupy
import cupyx
from cupyx.scipy import ndimage
from PIL import Image
import scipy
from scipy import ndimage
import time

raw_data = Image.open("./Samuel_Zeller_Tokyo_DSCF3800.JPG")
numpy_data = numpy.asarray(raw_data)
cupy_data = cupy.array(numpy_data)

timer_start = time.time()
resultant_data = cupyx.scipy.ndimage.gaussian_filter(cupy_data, 27)
timer_stop = time.time()

resultant_image = Image.fromarray(resultant_data.get())
resultant_image.save("python_cupy_Samuel_Zeller_Tokyo_DSCF3800.JPG")

print(f"Duración total del programa: {timer_stop - timer_start} segundos")
