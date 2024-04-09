matrix_size = 100000;

tic;
first_matrix = ones(matrix_size, matrix_size, 'single');
second_matrix = 2 * ones(matrix_size, matrix_size, 'single');

result_matrix = first_matrix * second_matrix;
elapsed_time = toc;

printf("Duración total del programa: %f segundos\n", elapsed_time);
