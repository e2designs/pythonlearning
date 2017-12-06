#!/usr/bin/env python

import imp
import inspect
import argparse


def main(filename):
    """
    Uses inspect to return a list of function names and their description
    """
    classlist = {}
    methodlist = {}
    functionlist = {}
    print 'Filename:{0}'.format(filename)
    module = inspect.getmodulename(filename)
    print 'Module:{0}'.format(module)

    importedmodule = imp.load_source(module, filename)
    for name, data in inspect.getmembers(importedmodule):
        if inspect.isclass(data):
            classlist[name] = data.__doc__
        elif inspect.ismethod(data):
            methodlist[name] = data.__doc__
        elif inspect.isfunction(data):
            functionlist[name] = data.__doc__

    print "Functions: "
    for key in functionlist.keys():
        print '{0}'.format(key)

    print "Function / document"
    for key, value in functionlist.items():
        print '{0} {1}'.format(key, value)


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(description="Returns functions and" + \
                " descriptions for a Module")
    PARSER.add_argument('filename', nargs="+", help="Module filename with path")
    ARGS = PARSER.parse_args()
    MODULE = ARGS.filename
    for name in MODULE:
        main(name)
