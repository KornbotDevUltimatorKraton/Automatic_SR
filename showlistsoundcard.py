import os
import subprocess 
os.system("arecord -l")
outputprocess = subprocess.check_output("arecord -l",shell=True)
print(outputprocess.decode())
