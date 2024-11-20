import os
import shutil
import numpy as np

# Array of initial masses
initial_donor_masses = [60] #list(np.arange(1,100,2).astype(int)) # Example masses
initial_accretor_masses = [40]
initial_period = [6]
winds = [['Bjorklund','Decin']]

# Paths
base_folder = "template_binary"
output_base = "m1_"
batch_script_name = "submit_array_jobs.sh"

# Create folders and modify files
for i,mass in enumerate(initial_donor_masses):
    # Create the folder name
    wind = winds[i][0] + winds[i][1]
    folder_name = f"{output_base}{mass}_m2_{initial_accretor_masses[i]}_p_{initial_period[i]}_wind_{wind}"
    
    # Copy the single_star folder
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)  # Remove if folder already exists
    shutil.copytree(base_folder, folder_name)
    
    # Path to the inlist_binary file
    inlist_path = os.path.join(folder_name, "inlist_binary")
    
    # Modify the inlist_binary file
    with open(inlist_path, "r") as file:
        lines = file.readlines()
    
    with open(inlist_path, "w") as file:
        for line in lines:
            if line.strip().startswith("m1"):
                file.write(f"m1 = {mass} ! donor mass in Msun\n")
            elif line.strip().startswith("m2"):
                file.write(f"m2 = {initial_accretor_masses[i]} ! accretor mass in Msun\n")
            elif line.strip().startswith("initial_period_in_days"):
                file.write(f"initial_period_in_days = {initial_period[i]} \n")
            else:
                file.write(line)
                
    # Path to the inlist_both file
    inlist_path = os.path.join(folder_name, "inlist_both")
    
    # Modify the inlist_both file
    with open(inlist_path, "r") as file:
        lines = file.readlines()
    
    with open(inlist_path, "w") as file:
        for line in lines:
            if line.strip().startswith("x_character_ctrl(1)"):
                file.write(f"x_character_ctrl(1) = '{winds[i][0]}' ! donor mass in Msun\n")
            elif line.strip().startswith("x_character_ctrl(2)"):
                file.write(f"x_character_ctrl(2) = '{winds[i][1]}' ! accretor mass in Msun\n")
            else:
                file.write(line)

# Generate batch submission script for array jobs
with open(batch_script_name, "w") as batch_file:
    batch_file.write("#!/bin/bash\n")
    batch_file.write("# --------------------\n")
    batch_file.write("### Directives Section\n")
    batch_file.write("# --------------------\n")
    batch_file.write(f"""\
#SBATCH --job-name=binary_array
#SBATCH --account=binboom
#SBATCH --partition=standard
#SBATCH --nodes=1
#SBATCH --ntasks=16
#SBATCH --time=72:00:00
#SBATCH -o mass_%A_%a.out
#SBATCH --array=0-{len(initial_donor_masses)-1}
# --------------------
### Code Section
# --------------------
export OMP_NUM_THREADS=16

# Array of folder names
folders=({" ".join(f"{output_base}{mass}_m2_{initial_accretor_masses[i]}_p_{initial_period[i]}_wind_{wind}" for i,mass in enumerate(initial_donor_masses))})

# Navigate to the appropriate folder
cd /groups/mrenzo/Neev/Projects/XRB/binary/${{folders[$SLURM_ARRAY_TASK_ID]}}
./clean && ./mk
./rn
""")

print("Folders and array job submission script created successfully!")