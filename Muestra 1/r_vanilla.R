#install.packages("tictoc")
library(tictoc)

arrays_size <- 5000000000

tic()
X <- as.single(rep(1,arrays_size))
Y <- as.single(rep(2,arrays_size))
X <- X * Y
toc()
