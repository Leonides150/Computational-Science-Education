#!/bin/sh

#SBATCH --job-name=matlab-test
#SBATCH --output=%x.o%j
#SBATCH --error=%x.e%j
#SBATCH --partition nocona
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=10:00:00     ##10 hour runtime, you may change or remove this option. Default time is 48 hours
#SBATCH --cpus-per-task=8               # 8 cores per instance

####SBATCH --mem=512000MB

# Add MATLAB to system path
module load matlab

# Run code 
matlab -batch calc_pi
