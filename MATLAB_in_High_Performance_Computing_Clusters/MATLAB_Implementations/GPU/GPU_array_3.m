c = parcluster('local');
p = c.parpool(6);

tic
n = 500;
A = 500;
%a = zeros(n);
a = zeros(n,"gpuArray");
parfor i = 1:n
    a(i) = max(abs(eig(rand(i))));
end
toc

p.delete;
delete(p);