import os
import shutil
import numpy as np

# Array of initial masses
initial_masses = list(np.arange(1,100,2).astype(int)) # Example masses

# Paths
base_folder = "single_star"
output_base = "mass_"
batch_script_name = "submit_array_jobs.sh"

# Create folders and modify files
for mass in initial_masses:
    # Create the folder name
    folder_name = f"{output_base}{mass}"
    
    # Copy the single_star folder
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)  # Remove if folder already exists
    shutil.copytree(base_folder, folder_name)
    
    # Path to the inlist_extra file
    inlist_path = os.path.join(folder_name, "inlist_extra")
    
    # Modify the inlist_extra file
    with open(inlist_path, "r") as file:
        lines = file.readlines()
    
    with open(inlist_path, "w") as file:
        for line in lines:
            if line.strip().startswith("initial_mass"):
                file.write(f"initial_mass = {mass} !added by Neev for SSE\n")
            else:
                file.write(line)

# Generate batch submission script for array jobs
with open(batch_script_name, "w") as batch_file:
    batch_file.write("#!/bin/bash\n")
    batch_file.write("# --------------------\n")
    batch_file.write("### Directives Section\n")
    batch_file.write("# --------------------\n")
    batch_file.write(f"""\
#SBATCH --job-name=mass_array
#SBATCH --account=binboom
#SBATCH --partition=standard
#SBATCH --nodes=1
#SBATCH --ntasks=16
#SBATCH --time=3:00:00
#SBATCH -o mass_%A_%a.out
#SBATCH --array=0-{len(initial_masses)-1}
# --------------------
### Code Section
# --------------------
export OMP_NUM_THREADS=16

# Array of folder names
folders=({" ".join(f"{output_base}{mass}" for mass in initial_masses)})

# Navigate to the appropriate folder
cd /home/u16/neevshah/Projects/XRB/SSE_grid/${{folders[$SLURM_ARRAY_TASK_ID]}}
./clean && ./mk
./rn
""")

print("Folders and array job submission script created successfully!")

