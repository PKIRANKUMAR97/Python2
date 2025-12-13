### approach 1 :

import sys
sys.path.append("C:/Users/reach/PycharmProjects/Python2/Day9/pack1")
#
# import module1
# import module2
#
# module1.display()
# module2.show()

### approach 2:

from module1 import *
from module2 import *

from Day9.pack1.module1 import display

display()
show()