
c = parcluster('local');
p = c.parpool(10);

tic

spmd (10)
    n = 500;
    A = 500;
    a = zeros(n);
    for i = 1:n
        a(i) = max(abs(eig(rand(i))));
    end
end

toc

p.delete;
delete(p);