q = parcluster('local'); % local is a cluster profile name

m = 50;
n = 3;

parfevalTime = zeros(n,1);
for i = 1:n
    tic;
    f(1:q.NumWorkers) = parallel.FevalFuture;
    for N = 1:q.NumWorkers
      f(N) = parfeval(@rand,1,m);
    end
    mats = fetchOutputs(f);
    parfevalTime(i) = toc;
    clear f
end

disp(parfevalTime) % displays individual times for each iteration
disp(mean(parfevalTime)) %displays average time
