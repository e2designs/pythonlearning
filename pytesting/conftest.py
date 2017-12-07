import pytest

@pytest.fixture(scope='session')
def username():
    print "My User"
    return "My User"
