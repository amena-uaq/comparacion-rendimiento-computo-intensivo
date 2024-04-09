#install.packages("magick")
# install.packages("tictoc")
library(magick)
library(tictoc)

raw_data = magick::image_read("Samuel_Zeller_Tokyo_DSCF3800.JPG")
tic()
resultant_data = magick::image_convolve(raw_data, kernel = "Gaussian:27x127")
toc()
