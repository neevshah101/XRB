#!/bin/bash
# --------------------
### Directives Section
# --------------------
#SBATCH --job-name=mass_array
#SBATCH --account=binboom
#SBATCH --partition=standard
#SBATCH --nodes=1
#SBATCH --ntasks=16
#SBATCH --time=3:00:00
#SBATCH -o mass_%A_%a.out
#SBATCH --array=0-49
# --------------------
### Code Section
# --------------------
export OMP_NUM_THREADS=16

# Array of folder names
folders=(mass_1 mass_3 mass_5 mass_7 mass_9 mass_11 mass_13 mass_15 mass_17 mass_19 mass_21 mass_23 mass_25 mass_27 mass_29 mass_31 mass_33 mass_35 mass_37 mass_39 mass_41 mass_43 mass_45 mass_47 mass_49 mass_51 mass_53 mass_55 mass_57 mass_59 mass_61 mass_63 mass_65 mass_67 mass_69 mass_71 mass_73 mass_75 mass_77 mass_79 mass_81 mass_83 mass_85 mass_87 mass_89 mass_91 mass_93 mass_95 mass_97 mass_99)

# Navigate to the appropriate folder
cd /home/u16/neevshah/Projects/XRB/SSE_grid/${folders[$SLURM_ARRAY_TASK_ID]}
./clean && ./mk
./rn
