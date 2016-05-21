#!/usr/bin/python
import marshal
fd = open('my.pyc', 'rb')
magic = fd.read(4)
date = fd.read(4)
code_object = marshal.load(fd)
fd.close()

print "Magic number is ", int(magic.encode('hex'),16)
print "Compilation date is ", date

import types

def inspect_code_object(co_obj, indent=''):
    print indent, "%s(lineno:%d)" % (co_obj.co_name, co_obj.co_firstlineno)
    for c in co_obj.co_consts:
            if isinstance(c, types.CodeType):
                inspect_code_object(c, indent+ '  ')

inspect_code_object(code_object)
