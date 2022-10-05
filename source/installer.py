import os, shutil

username = os.getlogin()
current_dir = os.getcwd()
copy_dir = f'C:\\Users\{username}\\AppData\\Local\\TJoC_SM\\Saved\\SaveGames'
file_dir = f'{current_dir}\\SaveGames'

if os.path.exists(copy_dir) == True:
    shutil.rmtree(copy_dir)

shutil.copytree(file_dir, copy_dir)

# Validating the files
print("Validating...\n")
listdir = os.listdir(f'C:\\Users\\{username}\\AppData\\Local\\TJoC_SM\\Saved\\SaveGames')
true_listdir = os.listdir(file_dir)
if os.path.exists(f'C:\\Users\\{username}\\AppData\\Local\\TJoC_SM\\Saved\\SaveGames'):
    for file in true_listdir:
        if file in listdir:
            print(f"Validated {file}.")
        else:
            print(f'Failed to validate {file}, retrying.')
            shutil.copy(f'{file_dir}\{file}', copy_dir)
            if not file in listdir:
                print(f'Couldnt validate {file}, please copy the file manually.')
            

input("\nPress ENTER to exit.")