from os import listdir, getcwd
from os.path import isdir,join
from shutil import move,copy
import subprocess

CONFIGS_TARGET = join(r"C:\Users\menas\AppData\Roaming\caspion")
CASPION_EXE = join(r"C:\Users\menas\AppData\Local\Programs\caspion\caspion.exe")
CONFIGS_PATH = join(getcwd(), 'configs')
CONFIG_FILE_NAME = "config.encrypt"


def choose_config():
    config_folders = [d for d in listdir(CONFIGS_PATH) if isdir(join(CONFIGS_PATH, d))]
    
    print("Choose configuration:")
    for index, config in enumerate(config_folders):
        print(index+1, " - ", config)
    
    while(True):
        try:
            config_i = int(input("Enter Number: ")) -1
            if config_i not in range(len(config_folders)): raise ValueError
            break
        except ValueError:
            print("Wrong input")

    print("Running caspion '" + config_folders[config_i] + "' with configuration...")
    copy( join(CONFIGS_PATH, config_folders[config_i], CONFIG_FILE_NAME) , join(CONFIGS_TARGET, CONFIG_FILE_NAME) )
    subprocess.run(CASPION_EXE, capture_output=True)
    move( join(CONFIGS_TARGET, CONFIG_FILE_NAME) , join(CONFIGS_PATH, config_folders[config_i], CONFIG_FILE_NAME) )

if __name__ ==  str("__main__"):
    while(True):
        try:
            choose_config()
        except Exception as e: 
            if __debug__:
                print(e)
            restart = input("Fatal Error! restart [Y/n]? ")
            if restart == 'n': break
           

    