import pytest

users = ['ModuleUser']
def setup_module():
    pass

@pytest.fixture(scope="module")
def setup_fixture(username):
    user = username
    print "\nIn Setup_fixture with {}.\n".format(user)
    return user

def test_test1(setup_fixture):
    print '\nrunning test1\n'
    print 'Setup fixture returned:{}\n'.format(setup_fixture)

def test_test2(setup_fixture):
    print '\nrunning test2\n'
    print 'Setup fixture returned:{}\n'.format(setup_fixture)
