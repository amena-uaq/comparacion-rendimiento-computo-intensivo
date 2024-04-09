pkg load image;

tic;

raw_data = imread("Samuel_Zeller_Tokyo_DSCF3800.JPG");

filter = fspecial("gaussian", [127 127], 27);

resultant_data = imfilter(raw_data, filter);

imwrite(resultant_data, "octave_Samuel_Zeller_Tokyo_DSCF3800.JPG", "jpg");

toc;
