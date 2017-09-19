from lazysetup import lazysetup, forcelazy
import pytest

@pytest.fixture()
def setup_fixture():
    """
    Setup for the module
    """

    env = lazysetup()
    env.logger.general("\nIn setup fixture")
    env.ddc = "ddc setup"
    env.wls_client
    env.placeholder

    yield env

    print "\nCleaning up env"

@pytest.fixture()
def setup_too():
    """
    Forced attribute execution
    """
    env2 = forcelazy()
    print env2.ff_gui
    env2.ff_gui = 'My Gui'
    print env2.ff_gui

    yield env2

    print "\nCleaning up other env"

def test_something(setup_fixture):
    """
    Test using env lazy setup
    """
    env = setup_fixture
    print "Testing my lazy setup"
    print "Updating placeholder"
    env.placeholder = 'Assigned value'

    print "CLI = {0}".format(env.maint_cli)
    print "GUI = {0}".format(env.ff_gui)
    print "DDC = {0}".format(env.ddc)
    print "WLS Client = {0}".format(env.wls_client)
    print "Adding something in the test"
    env.something = "Something new"

    print "Running test"
    try:
        raise Exception("Whoops")
    except:
        env.logger.critical("Something went wrong")
        env.logger.critical("My env is {}".format(env.__dict__))

def test_else(setup_too):
    """
    Test using env lazy setup
    """
    env2 = setup_too
    print "Testing my lazy setup"

    print "GUI = {0}".format(env2.ff_gui)
    print "Adding something in the test"
    env2.something = "Something new"

    print "Running test"
    try:
        raise Exception("Whoops")
    except:
        env2.logger.critical("Something went wrong")
        env2.logger.critical("My env is {}".format(env2.__dict__))
