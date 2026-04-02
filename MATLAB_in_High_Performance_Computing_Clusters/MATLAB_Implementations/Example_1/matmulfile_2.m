load A.dat;
load B.dat;

n=10
A=rand(n)
B=rand(n)

atimesb = A*B
aeletimesb = A.*B

save -ascii atimesb.txt atimesb
save -ascii aeletimesb.txt aeletimesb

quit
