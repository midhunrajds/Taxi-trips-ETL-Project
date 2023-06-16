# Import the necessary packages for the code block
from mage_ai.data_preparation.repo_manager import get_repo_path  # Package for obtaining the repository path
from mage_ai.io.bigquery import BigQuery  # Package for interacting with BigQuery
from mage_ai.io.config import ConfigFileLoader  # Package for loading configuration files
from pandas import DataFrame  # Package for working with data in tabular form
from os import path  # Package for working with file paths

# Check if 'data_exporter' is not already defined in the global scope
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter  # Package for data exporter decorators

# Decorator to mark the following function as a data exporter
@data_exporter
def export_data_to_big_query(data, **kwargs) -> None:
    """
    Template for exporting data to a BigQuery warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#bigquery

    """
    # Obtain the path to the repository and construct the configuration file path
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'  # Specify the configuration profile to use

    # Iterate over the data items to be exported
    for key, value in data.items():
        # Construct the table ID using a specific naming convention
        table_id = 'my-etl-project-389917.uber_dataset.{}'.format(key)

        # Configure the BigQuery instance and export the data
        BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
            DataFrame(value),  # Convert the data to a DataFrame
            table_id,
            if_exists='replace',  # Specify the resolution policy if the table name already exists
        )
