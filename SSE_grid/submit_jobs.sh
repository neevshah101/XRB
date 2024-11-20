#!/bin/bash
# --------------------
### Directives Section
# --------------------
#SBATCH --job-name=mass_10
#SBATCH --account=binboom
#SBATCH --partition=standard
#SBATCH --nodes=1
#SBATCH --ntasks=16
#SBATCH --time=72:00:00
#SBATCH -o mass_10.out
# --------------------
### Code Section
# --------------------
export OMP_NUM_THREADS=16
cd /home/u16/neevshah/Projects/XRB/SSE_grid/mass_10
./clean && ./mk
./rn

#SBATCH --job-name=mass_20
#SBATCH --account=binboom
#SBATCH --partition=standard
#SBATCH --nodes=1
#SBATCH --ntasks=16
#SBATCH --time=72:00:00
#SBATCH -o mass_20.out
# --------------------
### Code Section
# --------------------
export OMP_NUM_THREADS=16
cd /home/u16/neevshah/Projects/XRB/SSE_grid/mass_20
./clean && ./mk
./rn

#SBATCH --job-name=mass_30
#SBATCH --account=binboom
#SBATCH --partition=standard
#SBATCH --nodes=1
#SBATCH --ntasks=16
#SBATCH --time=72:00:00
#SBATCH -o mass_30.out
# --------------------
### Code Section
# --------------------
export OMP_NUM_THREADS=16
cd /home/u16/neevshah/Projects/XRB/SSE_grid/mass_30
./clean && ./mk
./rn

#SBATCH --job-name=mass_40
#SBATCH --account=binboom
#SBATCH --partition=standard
#SBATCH --nodes=1
#SBATCH --ntasks=16
#SBATCH --time=72:00:00
#SBATCH -o mass_40.out
# --------------------
### Code Section
# --------------------
export OMP_NUM_THREADS=16
cd /home/u16/neevshah/Projects/XRB/SSE_grid/mass_40
./clean && ./mk
./rn

#SBATCH --job-name=mass_50
#SBATCH --account=binboom
#SBATCH --partition=standard
#SBATCH --nodes=1
#SBATCH --ntasks=16
#SBATCH --time=72:00:00
#SBATCH -o mass_50.out
# --------------------
### Code Section
# --------------------
export OMP_NUM_THREADS=16
cd /home/u16/neevshah/Projects/XRB/SSE_grid/mass_50
./clean && ./mk
./rn

