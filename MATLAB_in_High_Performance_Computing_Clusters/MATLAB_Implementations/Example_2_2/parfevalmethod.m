
c = parcluster('local');
p = c.parpool(10);

tic
n = 500;
size = 500;
a = zeros(n); % Initialize as a column vector for easier indexing
feig = @(size) max(abs(eig(rand(size)))); % Corrected anonymous function input

futures = cell(n); % Cell array to store Future objects

for i = 1:n
    futures{i} = parfeval(feig, 1, i); % Store the Future object
end

% Retrieve the results from the Future objects
for i = 1:n
    a(i) = fetchOutputs(futures{i});  
end

toc

%Delete parallel workers
p.delete;
delete(p);