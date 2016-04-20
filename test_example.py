"""
====================
test_module_example
====================

:Module Description:   A random test module used to learn inspect. 
			The inspect module will pull data from this example.

:Test Reviewer:        jbrown
:Requirement Coverage: Full

"""

import os
import pytest
import sys
from logger import Logger

pytestmark = [pytest.mark.req("00001","00002"),
		pytest.mark.author("eevans"),
		pytest.mark.t_area("AREA1,AREA2,AREA3"),
		pytest.mark.mat3]

# Set Global variable
global variable

def setup_module():
    """
    Setup for all tests in this module

    Module Setup Steps:
    #. Step 1
    #. Step 2
    """
    variable = "abcd"

    pass

def setup_function():
    """
    Setup for every test case in this module

    Function Setup Steps:

    #. Step 1.
    #. Step 2.
    """
    variable2 = '1234'

    pass

def teardown_module():
    """
    Teardown after all tests in this module

    Module Teardown Steps:

    #. Remove something
    """
    variable = "Delete"

    pass


def teardown_function():
    """
    Teardown to be run after every test case 

    Function Teardown Steps:

    #. Step 1
    #. Step 2

    """

    try:
	os.path.isfile(LOGFILE) 
    except OSError:
	pass



@pytest.mark.mat5
@pytest.mark.t_type("Normal")
def test_functionality_1():
    """
    :Test Description: Test description goes here

    **Setup:**

        #. Execute the steps from :func:`setup_module`
        #. Execute the steps from :func:`setup_function`
        

    **Teststeps:**

        #. Run Test Steps.

    **Teardown:**

        #. Execute the steps from :func:`teardown_function`
        #. Execute the steps from :func:`teardown_module`

    """

    # automation code below
    onething = 'specific'
    another = 'unknown'
    assert onething == another, "Everything is different"



@pytest.mark.author("bmarley")
@pytest.mark.t_type("Robustness")
def test_functionality_2():
    """
    

    **Setup:**

        #. Execute the steps from :func:`setup_module`
        #. Execute the steps from :func:`setup_function`


    **Teststeps:**

        #. Run Test Steps.

    **Teardown:**

        #. Execute the steps from :func:`teardown_function`        
        #. Execute the steps from :func:`teardown_module`


    """

    if 1 == 2:
        pytest.fail(msg="The world is not as it seems")
    else:
        #This is a code comment
        print("Phew!")


@pytest.mark.mat5
@pytest.mark.t_type("Robustness")
def test_functionality_3():
    """
    :Test Description:    test description goes here

    **Setup:**

        #. Execute the steps from :func:`setup_module`
        #. Execute the steps from :func:`setup_function`

    **Teststeps:**

	#. Some other steps

    **Teardown:**

        #. Execute the steps from :func:`teardown_function`
        #. Execute the steps from :func:`teardown_module`

    """
    the_answer = 42
    assert the_answer == 42, "All is wrong in the universe"

@pytest.fixture(scope='function', params=['a1', 'a2', 'a3'])
def utilize_somevar(request):
    print "This is a fixture that uses " + request.param

    def destroy_somevar():
	print "This will act as teardown for utilize_somevar that used " + request.param

    request.addfinalizer(destroy_somevar)
    return request.param

def test_parametrize(utilize_somevar):
    print "This is test1 using parameter " + utilize_somevar

class test_class1():
    """
    For some reason we needed a class
    """

    def __init__(self):
	"""Initialize the instance of self"""
	self.var = 42

    @pytest.mark.mat0
    def test_var(self):
	""" :Description: Test that it fails. """
	system_input = 43
	assert system_input == self.var, "The wrong answer to the ultimate question"

    @someotherdecorator.abc
    def test_2(self):
	""" :Description: Test that it passes. """
	system_input = 42
	assert system_input == self.var, "The wrong answer to the ultimate question"
	




