#!/bin/bash
# --------------------
### Directives Section
# --------------------
#SBATCH --job-name=m1_60_m2_40_p_6_S_NL_D
#SBATCH --account=binboom
#SBATCH --partition=standard
#SBATCH --nodes=1
#SBATCH --ntasks=16
#SBATCH --time=72:00:00
#SBATCH -o %x.out
# --------------------
### Code Section
# --------------------
export OMP_NUM_THREADS=16
cd /home/u16/neevshah/Projects/XRB/binary/m1_60_m2_40_p_6_S_NL_D
./clean && ./mk
./rn
