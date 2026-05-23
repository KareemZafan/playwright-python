from src import calculator as calc
import pytest

test_data = [(2, 3, 5), (-1, 1, 0), (0, 0, 0), (-5, -3, -8), (1.5, 2.5, 4.0), (-1.5, -2.5, -4.0)]
@pytest.mark.parametrize("input1, input2, sum", test_data)
def test_add(input1, input2, sum):
    assert calc.add(input1,input2) == sum


sub_test_data = [(5, 2, 3), (1, -1, 2), (0, 0, 0), (-5, -3, -2), (2.5, 1.5, 1.0), (-2.5, -1.5, -1.0), (1000,150,850)]
@pytest.mark.parametrize("input1, input2, difference", sub_test_data)
@pytest.mark.AprilRelease
def test_subtract(input1, input2, difference):
    assert calc.subtract(input1, input2) == difference


mul_test_data = [(2, 3, 6), (-1, 1, -1), (0, 5, 0), (-5, -3, 15), (2.5, 1.5, 3.75), (-2.5, -1.5, 3.75), (150,1000,150000)]
@pytest.mark.parametrize("inp1,inp2,product",mul_test_data)
@pytest.mark.AprilRelease
def test_multiply(inp1,inp2,product):
    assert calc.multiply(inp1,inp2) == product

#@pytest.mark.skip(reason="Not implemented yet")
def test_divide():
    assert calc.divide(6, 3) == 2
    assert calc.divide(-1, 1) == -1
    assert calc.divide(0, 5) == 0
    assert calc.divide(-5, -3) == 5/3
    assert calc.divide(2.5, 1.5) == 5/3
    assert calc.divide(-2.5, -1.5) == 5/3
    assert calc.divide(150,1000) == 0.15
    assert calc.divide(5, 0) == None
    ##with pytest.raises(ValueError):
      ##  calc.divide(5, 0)   

@pytest.mark.RegressionTest
@pytest.mark.SanityTest
def test_power():
    assert calc.power(2, 3) == 8
    assert calc.power(-1, 2) == 1
    assert calc.power(0, 5) == 0
    assert calc.power(-5, -3) == -1/125
    assert calc.power(2.5, 1.5) == 2.5 ** 1.5
    assert calc.power(-2.5, -1) == -0.4
    assert calc.power(10,10) == 10 ** 10

@pytest.mark.RegressionTest
def test_sqrt():
    assert calc.sqrt(4) == 5
    assert calc.sqrt(0) == 0
    assert calc.sqrt(2.25) == 1.5
    
    with pytest.raises(ValueError):
        calc.sqrt(-1)
    with pytest.raises(ValueError):
        calc.sqrt(-2.25)

day = 28 

@pytest.mark.skipif(day < 28, reason="Notification message is only sent between 28th and 30th of the month.")
def test_notification_message():
    print("This is a notification message for testing purposes.")
    assert True  # Dummy assertion to ensure the test passes
    ### code to send the notification message

    ## Assertion of received notification message can be added here if applicable