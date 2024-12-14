#!/bin/bash
# --------------------
### Directives Section
# --------------------
#SBATCH --job-name=binary_array
#SBATCH --account=binboom
#SBATCH --partition=standard
#SBATCH --nodes=1
#SBATCH --ntasks=16
#SBATCH --time=72:00:00
#SBATCH -o no_rot_sc_th_basic_net_mid_z_25_15_5_%A_%a.out
#SBATCH --array=0-0
# --------------------
### Code Section
# --------------------
export OMP_NUM_THREADS=16

# Array of folder names
folders=(m1_25_m2_15_p_5_BD_no_rot_sc_th_basic_net_mid_z)

# Navigate to the appropriate folder
cd /groups/mrenzo/Neev/Projects/XRB/binary_star/${folders[$SLURM_ARRAY_TASK_ID]}
./clean && ./mk
./re 7000
