
A = rand(10);
d = 2;
%sum(gpuArray(A),d);
sum(A,gpuArray(d));