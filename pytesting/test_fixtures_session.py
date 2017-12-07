import pytest

def setup_module():
    pass


def test_test1(username):
    print '\nrunning test1\n'
    print 'Setup fixture returned:{}\n'.format(username)

def test_test2(username):
    print '\nrunning test2\n'
    print 'Setup fixture returned:{}\n'.format(username)
