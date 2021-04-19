import os

print(__file__)
print(os.path.realpath(__file__))
print(os.path.abspath(__file__))

import os
print(os.listdir(os.getcwd())+"/img")