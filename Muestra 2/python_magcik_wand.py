import wand
from wand.image import Image
from wand.image import BaseImage
import time

with Image(filename="Samuel_Zeller_Tokyo_DSCF3800.JPG") as raw_data:
    timer_start = time.time()
    resultant_data = BaseImage.gaussian_blur(raw_data, radius=127, sigma=27)
    timer_stop = time.time()
    raw_data.save("python_magick_Samuel_Zeller_Tokyo_DSCF3800.JPG")
print(f"Duración total del programa: {timer_stop - timer_start} segundos")
