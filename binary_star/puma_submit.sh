#!/bin/bash
# --------------------
### Directives Section
# --------------------
#SBATCH --job-name=binary_array
#SBATCH --account=binboom
#SBATCH --partition=standard
#SBATCH --nodes=1
#SBATCH --ntasks=16
#SBATCH --time=36:00:00
#SBATCH -o m1_45_m2_25_p_5_z_0.0146_mlt_6.0_%A_%a.out
#SBATCH --array=0-0
# --------------------
### Code Section
# --------------------
export OMP_NUM_THREADS=16

# Array of folder names
folders=(m1_45_m2_25_p_5_z_0.0146_mlt_6.0)

# Navigate to the appropriate folder
cd /groups/mrenzo/Neev/Projects/XRB/binary_star/${folders[$SLURM_ARRAY_TASK_ID]}
./clean && ./mk
./rn
