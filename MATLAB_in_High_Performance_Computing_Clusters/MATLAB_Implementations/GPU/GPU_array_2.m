
tic
n = 500;
A = 500;
%a = zeros(n);
a = zeros(n,"gpuArray");
for i = 1:n
    a(i) = max(abs(eig(rand(i))));
end
toc

