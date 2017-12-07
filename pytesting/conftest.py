import pytest

@pytest.fixture(scope='session', params=['defaultuser'])
def username(request):
    user = request.param
    print '\nConftest Fixture:{}\n'.format(user)
    return user
