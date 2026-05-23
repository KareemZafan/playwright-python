import pytest



## Precondition
@pytest.fixture(scope="module", autouse=True)
def setup_db_connection():
    print("\nSetting up DB connection")


## Postcondition
@pytest.fixture(scope="module", autouse=True)
def close_db_connection():
    yield
    print("\n Closing DB connection")


## @pytest.mark.xfail(reason="Failing test to demonstrate xfail")
def test_insert_into_DB():
    
    ## Arrange
    ## Act
    print("\nInserting data into DB")

    ## Assert
    print("\nAsserting data is inserted into DB")



def test_update_in_DB():
    ## Arrange 
    ## Act
    print("\nUpdating data in DB")

    ## Assert
    print("\nAsserting data is updated in DB")


def test_delete_from_DB():
    ## Arrange 
    ## Act
    print("\nDeleting data from DB")

    ## Assert
    print("\nAsserting data is deleted from DB")


def test_retreive_from_DB():
    ## Arrange 
    ## Act
    print("\nRetrieving data from DB")

    ## Assert
    print("\nAsserting data is retrieved from DB")

