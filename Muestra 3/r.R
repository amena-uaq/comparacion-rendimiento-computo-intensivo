#install.packages("tictoc")
library(tictoc)

matrix_size <- 100000


tic()

first_matrix <- matrix(single(rep(1.0, matrix_size^2)), nrow = matrix_size, ncol = matrix_size, byrow = TRUE)
second_matrix <- matrix(single(rep(2.0, matrix_size^2)), nrow = matrix_size, ncol = matrix_size, byrow = TRUE)


result <- first_matrix %*% second_matrix

toc()
