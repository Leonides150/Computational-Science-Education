
%Create a parallel cluster object
% local is a cluster profile name
c = parcluster('local');
p = c.parpool(10);

%Start timing
tic

%Calculates spectral radius of each matrix and displays results
%Distributed across several workers
n = 500;
A = 500;
a = zeros(n);
parfor i = 1:n
    a(i) = max(abs(eig(rand(i))));
end

%End timing
time = toc

%Display the time of computation
fprintf('The parallel method is executed in %5.2f seconds.  \n', time);

%Delete parallel workers
p.delete;
delete(p);