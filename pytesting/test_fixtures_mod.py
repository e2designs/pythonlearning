import pytest

def setup_module():
    pass


@pytest.fixture(scope="module")
def setup_fixture(username):
    myuser = username
    print myuser


def test_test1(setup_fixture):
    print 'running test1'

def test_test2(setup_fixture):
    print 'running test2'
