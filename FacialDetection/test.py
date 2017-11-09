# https://stackoverflow.com/questions/30664263/return-value-from-one-python-script-to-another
# how to read an output from one python script called by another another

import sys
import subprocess

s2_out = subprocess.check_output([sys.executable, "script2.py", "34"])
print s2_out
