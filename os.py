import os
import sys


sys.stderr.write('stderr test\n')
sys.stderr.flush()
sys.stdout.write('stdout test\n')
print('sys.argv==>:', sys.argv)
