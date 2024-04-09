import numpy
from PIL import Image
import scipy
from scipy import ndimage
import time

raw_data = Image.open("./Samuel_Zeller_Tokyo_DSCF3800.JPG")
numpy_data = numpy.asarray(raw_data)

timer_start = time.time()
resultant_data = scipy.ndimage.gaussian_filter(numpy_data, 27, radius=127)
timer_stop = time.time()

resultant_image = Image.fromarray(resultant_data)
resultant_image.save("python_numpy_Samuel_Zeller_Tokyo_DSCF3800.JPG")

print(f"Duración total del programa: {timer_stop - timer_start} segundos")
