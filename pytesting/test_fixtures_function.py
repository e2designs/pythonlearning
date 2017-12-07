import pytest

def setup_module():
    pass


@pytest.fixture(scope="function")
def func_username(username):
    user = username
    print "\nIn Setup_fixture with {}.\n".format(user)
    return user

@pytest.mark.parametrize('func_username', ['functionuser1'])
def test_test1(func_username):
    print '\nrunning test1\n'
    print 'Setup fixture returned:{}\n'.format(func_username)

@pytest.mark.parametrize('username', ['functionuser2'])
def test_test2(func_username):
    print '\nrunning test2\n'
    print 'Setup fixture returned:{}\n'.format(func_username)

def test_test3(func_username):
    print '\nrunning test3\n'
    print 'Setup fixture returned:{}\n'.format(func_username)
