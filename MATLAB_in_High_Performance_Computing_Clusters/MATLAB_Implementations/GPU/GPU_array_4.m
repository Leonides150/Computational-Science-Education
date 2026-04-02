
tic
%Create GPU arrays defining the growth rate, r, and the population, x
N = 200000;
r = gpuArray.linspace(0,4,N);
x = rand(1,N,"gpuArray");

%Use a simple algorithm to iterate the logistic map. Because the algorithm 
% uses GPU-enabled operators on gpuArray input data, the computations run on the GPU.
numIterations = 1000;
for n=1:numIterations
    x = r.*x.*(1-x);
end

%When the computations are done, plot the growth rate against the population.
plot(r,x,'.',MarkerSize=1)
xlabel("Growth Rate")
ylabel("Population")

toc