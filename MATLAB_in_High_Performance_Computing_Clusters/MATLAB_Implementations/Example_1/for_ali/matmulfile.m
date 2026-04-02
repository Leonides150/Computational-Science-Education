load A.dat;
load B.dat;
atimesb = A*B
aeletimesb = A.*B
save -ascii atimesb.txt atimesb
save -ascii aeletimesb.txt aeletimesb
quit
