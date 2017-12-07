import pytest

@pytest.fixture(scope='module', params=['defaultuser'])
def username(request):
    print 'Request:{}'.format(request)
    user = request.param
    print '\nConftest Fixture:{}\n'.format(user)
    return user
