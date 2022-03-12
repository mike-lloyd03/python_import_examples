import sys

sys.path.append("../")

from python_import_test.math_fcns.div import div
from python_import_test.more_fcns import add
from python_import_test.subtract import sub

print(div(15, 5))
print(add(15, 5))
print(sub(15, 5))
