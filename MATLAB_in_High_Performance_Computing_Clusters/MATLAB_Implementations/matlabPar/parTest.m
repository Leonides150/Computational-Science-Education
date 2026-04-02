%Create a parallel cluster object
%c = parcluster;
c = parcluster('local'); % local is a cluster profile name


%Specify the partition the job will be running on
%c.AdditionalProperties.Partition='nocona';

%Specify the number of nodes (-N 2), save the profile, and display properties
%c.AdditionalProperties.NumberOfNodes=2;
%c.saveProfile
%c.AdditionalProperties

%Specify the total number of parallel workers in 2 nodes requested
%p = c.parpool(64);

% Query for available cores (assume either Slurm or PBS)
sz = str2num([getenv('SLURM_CPUS_PER_TASK')]); %#ok<ST2NM>
if isempty(sz), sz = maxNumCompThreads; end
if isempty(gcp('nocreate')), c.parpool(sz); end
	
%Start timing
tic

%Calculates spectral radius of each matrix and displays results
n = 10;
A = 500;
a = zeros(n);
parfor i = 1:n*n
    a(i) = max(abs(eig(rand(A))));
end
disp(a)

%End timing
time = toc;

 
%Display the time of computation
fprintf('The parallel method is executed in %5.2f seconds.  \n', time);


%Delete parallel workers
%c.delete
