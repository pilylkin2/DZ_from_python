# DZ_from_python
Я пытался, но дальше этого я не продвинулся:

import os

from importlib import import_module

path = 'question_types'

rez = os.listdir(path)
print(rez)
s = []
path = 'question_types.subpkg'
y= '..'
for i in rez:
    j = i[:-3]
    j = y+j
    print(j)   
    s.append(exec('import_module(j,path)'))
    pass

s
