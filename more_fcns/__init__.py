# If I import stuff from other Python files in this directory, I can
# import those same functions directly when importing the module.
# So when I import this module, I don't have to reference the "thisisalongname"
# since what I need from it is being imported here in the __init__ file.
from .thisisalongname import add
