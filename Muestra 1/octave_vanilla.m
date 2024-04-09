tic;

arrays_size = 5000000000;

X = ones(arrays_size, 1, "single");
Y = 2 * ones(arrays_size, 1, "single");

X .* Y;

toc;
