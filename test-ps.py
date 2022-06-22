import subprocess, sys

p = subprocess.Popen(["powershell.exe", 
              "G:\\drowsiness\\SMS.ps1"], 
              stdout=sys.stdout)
p.communicate()
