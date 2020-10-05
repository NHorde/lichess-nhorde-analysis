import os
import sys

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PATH)

print(PATH)