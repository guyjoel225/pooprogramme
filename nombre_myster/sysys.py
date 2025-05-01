import os

import sys

import getopt
"""

try:
    opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help","output="])
    
except getopt.GetoptError as err:
    
    print(err)
    
    sys.exit(2)
    
output = None
Verbose = False

for o, a in opts:
    
    if o == "-v":
        
        Verbose = True
        
    elif o in ("-h", "--help"):
        
        sys.exit(2)
        
    elif o in ("-o", "--outpout"):
        
        output = a
    
    else:
        
        print("Option {}inconnue".format(o))
        
        sys.exit(2)
        
    """
    
    
os.system("printenv")