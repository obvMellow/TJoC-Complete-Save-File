import os, shutil, time

global ask
ask = ""
print("This proccess will replace your current save file.")
while ask != "y" or ask != "n":
    ask = input("Are you sure you want to continue(y/n): ")
    if ask == "y" or ask == "n":
        break

if ask == "y":
    pass
elif ask == "n":
    print("Exiting...")
    time.sleep(2.0)
    raise Exception("Exitted.")


username = os.getlogin()
current_dir = os.getcwd()
copy_dir = f'C:\\Users\{username}\\AppData\\Local\\TJoC_SM\\Saved\\SaveGames'
file_dir = f'{current_dir}\\SaveGames'

if os.path.exists(copy_dir) == True:
    shutil.rmtree(copy_dir)

print("\nCopying the files...")
shutil.copytree(file_dir, copy_dir)
time.sleep(1.0)

print("\nValidating...\n")
time.sleep(0.1)
listdir = os.listdir(f'C:\\Users\\{username}\\AppData\\Local\\TJoC_SM\\Saved\\SaveGames')
true_listdir = os.listdir(file_dir)
for file in true_listdir:
    result = []
    time.sleep(0.01)
    if file in os.listdir(f'C:\\Users\\{username}\\Appdata\\Local\\TJoC_SM\\Saved\\SaveGames'):
        print(f"Validated {file}.")
        result.append("Success")
    else:
        print(f'Failed to validate {file}, retrying.')
        shutil.copy(f'{file_dir}\{file}', copy_dir)
        if file in os.listdir(f'C:\\Users\\{username}\\Appdata\\Local\\TJoC_SM\\Saved\\SaveGames'):
            print(f"Validated {file}.")
            result.append("Success")
        else:
            print(f'Couldnt validate {file}, please copy the file manually.')
            result.append("Fail")
    
if "Fail" in result:
    print("Some files weren't validated succesfully. Please copy them manually.")
else:
    print("All files were validated succesfully.")

input("\nPress ENTER to exit.")