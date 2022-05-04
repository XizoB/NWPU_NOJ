import os
print(os.name)
#print(os.environ)
print(os.sep)
print(os.getcwd())
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.abspath(os.path.abspath(__file__)))
print(os.path.dirname(__file__))