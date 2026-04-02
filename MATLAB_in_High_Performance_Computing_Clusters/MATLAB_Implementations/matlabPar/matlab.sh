#!/bin/bash
#SBATCH --job-name=matlab-test
#SBATCH --output=%x.o%j
#SBATCH --error=%x.e%j
#SBATCH --partition=nocona
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
module --ignore-cache load matlab/R2024a
export PATH=$PATH:/opt/ttu/apps/licensed/matlab/R2024a/bin
#export PATH=$PATH:/opt/apps/nfs/custom/cpu/matlab/R2024a/bin
matlab -batch parTest
