# Import necessary libraries
import io  # Required for handling input/output operations
import pandas as pd  # Required for data manipulation and analysis
import requests  # Required for making HTTP requests

# Check if 'data_loader' and 'test' functions are already defined in the global scope
if 'data_loader' not in globals():
    # If not defined, import 'data_loader' function from Mage.ai library
    from mage_ai.data_preparation.decorators import data_loader

if 'test' not in globals():
    # If not defined, import 'test' function from Mage.ai library
    from mage_ai.data_preparation.decorators import test

# Decorate the 'load_data_from_api' function with 'data_loader' decorator
@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    # Specify the URL to fetch the data from
    url = 'https://storage.googleapis.com/etl-uber-project-june2023/uber_data.csv'
    
    # Make an HTTP GET request to the URL and store the response
    response = requests.get(url)

    # Read the response text into a Pandas DataFrame
    return pd.read_csv(io.StringIO(response.text), sep=',')

# Decorate the 'test_output' function with 'test' decorator
@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    # Assert that the output is not None
    assert output is not None, 'The output is undefined'
