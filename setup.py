

import os
from sys import platform

# set PYTHONPATH
# by appending to .bash_profile?

# get location of package
project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


# Unix:
if platform == "linux" or platform == "darwin":

    # save copy of .bash_profile
    os.system('cp ~/.bash_profile ~/.bash_profile.ideagraph')

    # setup bash jawn
    bash_line = "\nexport PYTHONPATH=\${PYTHONPATH}:" + project_dir + "\n\n"
    
    # append to .bash_profile
    os.system("printf \"" + bash_line + "\" >> ~/.bash_profile")

    # create launcher script
    cmd = '"#!/bin/bash\n\npython -m ideagraph \$@\n"'
    exec_loc = "/usr/local/bin/ideagraph" if platform == "darwin" else "~/.local/bin/ideagraph"
    os.system("printf " + cmd + " > " + exec_loc)
    os.system("chmod +x " + exec_loc)
    

# Windows:
elif platform == "win32":
    pass
    
