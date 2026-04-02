c = parcluster('local');
p = c.parpool(4);

tic
%Create GPU arrays defining the growth rate, r, and the population, x
numSimulations = 100;
X = zeros(numSimulations,N,"gpuArray");

%Use a simple algorithm to iterate the logistic map. Because the algorithm 
% uses GPU-enabled operators on gpuArray input data, the computations run on the GPU.
parfor i = 1:numSimulations
    X(i,:) = rand(1,N,"gpuArray");
    for n=1:numIterations
        X(i,:) = r.*X(i,:).*(1-X(i,:));
    end
end

%When the computations are done, plot the growth rate against the population.
figure
plot(r,X,'.',MarkerSize=1)
xlabel("Growth Rate")
ylabel("Population")

toc

p.delete;