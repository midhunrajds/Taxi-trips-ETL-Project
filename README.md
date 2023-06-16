# Taxi-trips - ETL Project
# Uber Data Analytics Project

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)  ![SQL](https://img.shields.io/badge/SQL-MySQL-orange.svg)  ![Mage.ai](https://img.shields.io/badge/Mage.ai-Data%20Pipeline%20Tool-green.svg) ![Google Cloud Platform](https://img.shields.io/badge/Google%20Cloud%20Platform-GCP-blue.svg) ![VM Machines](https://img.shields.io/badge/VM%20Machines-GCP%20Compute%20Engine-yellow.svg)  ![SSH](https://img.shields.io/badge/SSH-Remote%20Access-red.svg)  ![BigQuery](https://img.shields.io/badge/BigQuery-Google%20Cloud%20BigQuery-orange.svg) ![Google Cloud Storage](https://img.shields.io/badge/Google%20Cloud%20Storage-GCS-blue.svg) ![Tableau](https://img.shields.io/badge/Tableau-Data%20Visualization-yellow.svg) ![Lucid Chart](https://img.shields.io/badge/Lucid%20Chart-Diagramming%20Tool-lightgrey.svg)


This project analyzes Uber data using various tools and technologies, including GCP Storage, Python, Compute Instance, Mage Data Pipeline Tool, BigQuery, and Tableau. The goal is to gain insights from the TLC Trip Record Data, which includes yellow and green taxi trip records, capturing pick-up and drop-off details, trip distances, fares, payment types, and more.

## Dataset

The dataset used in this project is the TLC Trip Record Data, which can be found on the [NYC TLC Trip Record Data website](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page). The data dictionary for the trip records can be accessed [here](https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf).

Dataset Location: [Uber Dataset](https://github.com/darshilparmar/uber-etl-pipeline-data-engineering-project/blob/main/data/uber_data.csv)

## Project Overview

The project involves the following steps:

1. Set up GCP Storage: Create a storage bucket in Google Cloud Platform (GCP) to store the Uber dataset and intermediate files.

2. Data Ingestion: Download the Uber dataset and upload it to the GCP Storage bucket.

3. Data Transformation with Python: Use Python to read the Uber dataset, clean the data, and perform necessary transformations and calculations.

4. Data Pipeline with Mage Data Pipeline Tool: Set up the Mage Data Pipeline Tool on a Compute Instance in GCP to orchestrate the data processing steps and store the transformed data in BigQuery.

5. Data Loading into BigQuery: Create a BigQuery dataset to store the transformed Uber data and configure the data pipeline to load the data into BigQuery tables.

6. Data Analysis with Tableau: Use Tableau, a data visualization tool, to connect to the BigQuery dataset and create reports and visualizations for analyzing the Uber data.

## Project Structure

The project follows the following structure:


## Getting Started

To set up the project and reproduce the analysis, please follow the instructions below:

1. [Step-by-step instructions on setting up GCP Storage, Compute Instance, Mage Data Pipeline Tool, and Tableau]
2. [Instructions on running the data pipeline and loading data into BigQuery]
3. [Instructions on accessing and analyzing the data using Tableau]

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

