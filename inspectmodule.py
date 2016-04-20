#!/usr/bin/env python

"""
:Description: Adventures in learning inspect.

"""
import imp
import importlib
import inspect
import os
import sys


# Check if file is provided and exists
if len (sys.argv) >=2:
    filename = sys.argv[1]
else:
    filename = "test_example.py"

if os.path.isfile(filename) is False:
    print "File %s does not exist"% filename
    sys.exit(0)

# Check if file is source file and suffix is correct
try:
    (name, suffix, mode, mtype) = inspect.getmoduleinfo(filename)
except TypeError:
    print "Unable to determine module type %s" % filename
else:
    mtype_name = { imp.PY_SOURCE:'source',
		    imp.PY_COMPILED:'compiled',
		    }.get(mtype, mtype)

    mode_description = { 'rb':'(read-binary)',
			'U':'(Universal Newline)',
			}.get(mode, '')

    print "Name\t:%s" % name
    print "Suffix\t:%s" % suffix
    print "Mode\t:%s %s" % (mode, mode_description)
    print "Mtype\t:%s" % mtype_name



# Get Module name
module = inspect.getmodulename(filename)
print "Module %s"% module



