r = parcluster('local'); % local is a cluster profile name

m = 50;
n = 3;

spmdTime = zeros(n,1);
for i = 1:n
    tic;
    spmd
        mat = rand(m);
        mats = spmdCat({mat}, 1, 1);
    end
    allMats = mats{1};
    spmdTime(i) = toc;
end

disp(spmdTime) % displays individual times for each iteration
disp(mean(spmdTime)) %displays average time
