p = parcluster('local'); % local is a cluster profile name

m = 50;
n = 3;

parforTime = zeros(n,1);

for i = 1:n
    tic;
    mats = cell(1,p.NumWorkers);
    parfor N = 1:p.NumWorkers
      mats{N} = rand(m);
    end
    parforTime(i) = toc;
end

disp(parforTime) % displays individual times for each iteration
disp(mean(parforTime)) %displays average time

