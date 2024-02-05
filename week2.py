# Data loader.
import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-10.csv.gz'
    url1 = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-11.csv.gz'
    url2 = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-12.csv.gz'

    taxi_dtypes = {
                    'VendorID': pd.Int64Dtype(),
                    'passenger_count': pd.Int64Dtype(),
                    'trip_distance': float,
                    'RatecodeID':pd.Int64Dtype(),
                    'store_and_fwd_flag':str,
                    'PULocationID':pd.Int64Dtype(),
                    'DOLocationID':pd.Int64Dtype(),
                    'payment_type': pd.Int64Dtype(),
                    'fare_amount': float,
                    'extra':float,
                    'mta_tax':float,
                    'tip_amount':float,
                    'tolls_amount':float,
                    'improvement_surcharge':float,
                    'total_amount':float,
                    'congestion_surcharge':float
                }

    #parse_dates = ['tpep_pickup_datetime', 'tpep_dropoff_datetime']

    df = pd.read_csv(
        url, sep=',', compression='gzip', dtype=taxi_dtypes, #parse_dates=parse_dates
        )

    df1 = pd.read_csv(
        url1, sep=',', compression='gzip', dtype=taxi_dtypes, #parse_dates=parse_dates
        )

    df2 = pd.read_csv(
    url2, sep=',', compression='gzip', dtype=taxi_dtypes, #parse_dates=parse_dates
    )

    df3 = pd.concat([df, df1, df2])

    return df3



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'


# Transformer
import datetime


if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    #print(f'Preprocessing: rows with zero passengers: {data["passenger_count"].isin([0]).sum()}')
    data = data[data['passenger_count'] > 0]
    data = data[data['trip_distance'] > 0]

    #data["lpep_pickup_date"] = data["lpep_pickup_datetime"].map(
    #    lambda x: str(datetime.datetime.strptime(x, "%Y-%m-%d"))
    #    if x == x and x is not None
    #    else x
    #)

    return data

@test
def test_output(output, *args):
    assert output["passenger_count"].isin([0]).sum() == 0, 'There are rides with zero passengers'



 # Python exporter
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.postgres import Postgres
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_postgres(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a PostgreSQL database.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#postgresql
    """
    schema_name = 'mage'  # Specify the name of the schema to export data to
    table_name = 'green_taxi'  # Specify the name of the table to export data to
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'dev'

    with Postgres.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        loader.export(
            df,
            schema_name,
            table_name,
            index=False,  # Specifies whether to include index in exported table
            if_exists='replace',  # Specify resolution policy if table name already exists
        )


# SQL exporter
select distinct vendorid from mage.green_taxi
