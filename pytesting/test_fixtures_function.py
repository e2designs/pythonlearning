import pytest

def setup_module():
    pass


@pytest.fixture(scope="function")
def func_username(username, request):
    user, host = username
    print "\nIn Setup_fixture with {}.\n".format(user)
    return user, host

@pytest.mark.parametrize('func_username', ['Function1User'])
def test_test1(func_username):
    print '\nrunning test1\n'
    print 'Setup fixture returned:{}\n'.format(func_username)

def test_test2(func_username):
    print '\nrunning test2\n'
    print 'Setup fixture returned:{}\n'.format(func_username)

def test_test3(func_username):
    print '\nrunning test3\n'
    print 'Setup fixture returned:{}\n'.format(func_username)
