%Start timing
tic

%Calculates spectral radius of each matrix and displays results
n = 500;
A = 500;
a = zeros(n);
for i = 1:n
    a(i) = max(abs(eig(rand(A))));
end
disp(a)

%End timing
time = toc;

 
%Display the time of computation
fprintf('The parallel method is executed in %5.2f seconds.  \n', time);