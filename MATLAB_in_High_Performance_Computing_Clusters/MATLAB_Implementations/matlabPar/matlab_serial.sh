#!/bin/bash
#SBATCH --job-name=matlab-test
#SBATCH --output=%x.o%j
#SBATCH --error=%x.e%j
#SBATCH --partition=nocona
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
module --ignore-cache load matlab/R2024a
#export PATH=$PATH:/opt/apps/nfs/custom/cpu/matlab/R2020b/bin
matlab -batch parTest_serial
