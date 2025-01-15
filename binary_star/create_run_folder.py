import os
import shutil


def update_inlists(template_folder, m1, m2, period, Z, mixing_length_alpha, do_tidal_sync, evolve_both_stars):
    """
    Update 'inlist_binary', 'inlist_both', and 'inlist_extra' files with specified parameters
    and copy to a new folder.

    Parameters:
    - template_folder (str): Path to the template folder.
    - m1 (float): Donor mass in solar masses.
    - m2 (float): Accretor mass in solar masses.
    - period (float): Initial period in days.
    - Z (float): Metallicity value.
    - mixing_length_alpha (float): Mixing length alpha parameter.
    - do_tidal_sync (bool): Value for 'do_tidal_sync' in 'inlist_binary'.
    - evolve_both_stars (bool): Value for 'evolve_both_stars' in 'inlist_binary'.
    """
    # Generate the folder name dynamically
    new_folder = f"m1_{m1}_m2_{m2}_p_{period}_z_{Z}_mlt_{mixing_length_alpha}"

    # Ensure the template folder exists
    if not os.path.exists(template_folder):
        raise FileNotFoundError(f"Template folder '{template_folder}' does not exist.")

    # Create the new folder if it doesn't exist
    os.makedirs(new_folder, exist_ok=True)

    # Update 'inlist_binary'
    template_inlist_binary_path = os.path.join(template_folder, "inlist_binary")
    if not os.path.exists(template_inlist_binary_path):
        raise FileNotFoundError(f"'{template_inlist_binary_path}' does not exist in the template folder.")

    with open(template_inlist_binary_path, "r") as file:
        binary_lines = file.readlines()

    updated_binary_lines = []
    for line in binary_lines:
        if "m1 =" in line:
            updated_binary_lines.append(f"m1 = {m1} ! donor mass in Msun\n")
        elif "m2 =" in line:
            updated_binary_lines.append(f"m2 = {m2} ! accretor mass in Msun\n")
        elif "initial_period_in_days =" in line:
            updated_binary_lines.append(f"initial_period_in_days = {period}\n")
        elif "do_tidal_sync =" in line:
            updated_binary_lines.append(f"do_tidal_sync = {'.true.' if do_tidal_sync else '.false.'}\n")
        elif "evolve_both_stars =" in line:
            updated_binary_lines.append(f"evolve_both_stars = {'.true.' if evolve_both_stars else '.false.'}\n")
        else:
            updated_binary_lines.append(line)

    new_inlist_binary_path = os.path.join(new_folder, "inlist_binary")
    with open(new_inlist_binary_path, "w") as file:
        file.writelines(updated_binary_lines)

    # Update 'inlist_both'
    template_inlist_both_path = os.path.join(template_folder, "inlist_both")
    if not os.path.exists(template_inlist_both_path):
        raise FileNotFoundError(f"'{template_inlist_both_path}' does not exist in the template folder.")

    with open(template_inlist_both_path, "r") as file:
        both_lines = file.readlines()

    updated_both_lines = []
    for line in both_lines:
        if "mixing_length_alpha =" in line:
            updated_both_lines.append(f"mixing_length_alpha = {mixing_length_alpha} ! Mixing length parameter\n")
        else:
            updated_both_lines.append(line)

    new_inlist_both_path = os.path.join(new_folder, "inlist_both")
    with open(new_inlist_both_path, "w") as file:
        file.writelines(updated_both_lines)

    # Update 'inlist_extra'
    template_inlist_extra_path = os.path.join(template_folder, "inlist_extra")
    if not os.path.exists(template_inlist_extra_path):
        raise FileNotFoundError(f"'{template_inlist_extra_path}' does not exist in the template folder.")

    with open(template_inlist_extra_path, "r") as file:
        extra_lines = file.readlines()

    updated_extra_lines = []
    for line in extra_lines:
        if "new_Z =" in line:
            updated_extra_lines.append(f"new_Z = {Z}d0\n")
        elif "Zbase =" in line:
            updated_extra_lines.append(f"Zbase = {Z}d0\n")
        else:
            updated_extra_lines.append(line)

    new_inlist_extra_path = os.path.join(new_folder, "inlist_extra")
    with open(new_inlist_extra_path, "w") as file:
        file.writelines(updated_extra_lines)

    # Copy the rest of the template folder contents to the new folder
    for item in os.listdir(template_folder):
        item_path = os.path.join(template_folder, item)
        if os.path.isfile(item_path) and item not in ["inlist_binary", "inlist_both", "inlist_extra"]:
            shutil.copy(item_path, new_folder)
        elif os.path.isdir(item_path):
            shutil.copytree(item_path, os.path.join(new_folder, item), dirs_exist_ok=True)

    print(f"New folder '{new_folder}' created with updated 'inlist_binary', 'inlist_both', and 'inlist_extra'.")


# Example usage
template_folder = "new_binary_template"
m1 = 45  # Donor mass in Msun
m2 = 25  # Accretor mass in Msun
period = 5  # Initial period in days
Z = 0.0146  # Metallicity value
mixing_length_alpha = 6.0  # Mixing length alpha parameter
do_tidal_sync = True  # Enable tidal synchronization
evolve_both_stars = True  # Enable evolving both stars

update_inlists(template_folder, m1, m2, period, Z, mixing_length_alpha, do_tidal_sync, evolve_both_stars)

