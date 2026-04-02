function [t, A] = serial_example(iter)
 
if nargin==0
    iter = 8;
end
 
disp('Start sim')
 
t0 = tic;
for idx = 1:iter
    A(idx) = idx;
    pause(2)
    idx
end
t = toc(t0);
 
disp('Sim completed')
 
save RESULTS A
 
end
