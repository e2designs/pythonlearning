import pytest

@pytest.fixture(scope='module', params=['defaultuser'])
def username(request):
    user = request.param
    print '\nConftest Fixture:{}\n'.format(user)
    host = 'My host'
    yield user, host
    print 'RUNNING CONFTEST TEARDOWN'
