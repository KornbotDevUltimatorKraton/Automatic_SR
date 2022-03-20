import subprocess 
import os 
import time 
#temp_raw = subprocess.check_output("vcgencmd measure_temp",shell=True)
#temp_dec = temp_raw.decode() 
while True:
     temp_raw = subprocess.check_output("vcgencmd measure_temp",shell=True)
     temp_dec = temp_raw.decode()
     print(temp_dec)
     time.sleep(0.01)
