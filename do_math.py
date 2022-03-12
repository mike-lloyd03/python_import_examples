from math_fcns.div import div  # imported from subdirectory with a blank __init__.py
from more_fcns import add  # imported from a subdirectory with a __init__.py which imports stuff
from subtract import sub  # imported from same directory with no __init__.py

print(sub(19, 5))
print(div(35, 5))
print(add(10, 1000))
