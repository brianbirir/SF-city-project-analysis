import os
import sys
import pandas as pd
import numpy as np

# dataset source
FILE_SOURCE = sys.argv[1]

# keywords to search for in dataset
LARGE_SCALE = 'large'
RESIDENTIAL = 'residential'


def read_dataset():
    """Loads the data set from a file source

    Returns:
        dataFrame: The pandas data structure of the file records
    """
    # get file extension to determine method of reading file
    # using pandas
    file_name, file_extension = os.path.splitext(FILE_SOURCE)
    if file_extension == '.xlsx':
        records = pd.read_excel(FILE_SOURCE)
    elif file_extension == '.csv':
        records = pd.read_csv(FILE_SOURCE)
    else:
        records = "Unsupported file format!"
    return records


def get_description_column():
    """Extracts the description column from the data source

    Returns:
        dataFrame: The pandas data structure with the description column
    """
    df = read_dataset()
    # replace empty cells with NaN value
    df[['description']].replace('', np.nan, inplace=True)
    # drop non-values found in description table
    df.dropna(subset=['description'], inplace=True)
    return df[['OBJECTID', 'record_name', 'description']]


def remove_punctuation(text):
    """Removes punctuation from the description column text

    Returns:
        dataFrame: Description column data without punctuation
    """
    symbols = "[^\w\s]"
    return text.str.replace(symbols, "")


def to_lowercase(text):
    """Converts description column text to lower case

    Returns:
        dataFrame: Description column data text in lower case
    """
    return text.str.lower()


def preprocess(data):
    """Pre-process of text data before analysis

    Returns:
        string: Preprocessed text
    """
    data = remove_punctuation(data)
    preprocessed_data = to_lowercase(data)
    return preprocessed_data


def build_data_pipeline():
    """ Build data pipeline

    Returns:
        dataFrame: Processed data
    """
    df_preprocessed = get_description_column().astype(str).apply(lambda x: preprocess(x))
    df_preprocessed['large_scale'] = df_preprocessed.astype(str).sum(axis=1).str.contains(LARGE_SCALE)
    df_preprocessed['residential'] = df_preprocessed.astype(str).sum(axis=1).str.contains(RESIDENTIAL)
    return df_preprocessed


def generate_analysis_results():
    """ Generate analysis results
    Returns:
        file: csv file
    """
    df_processed_data = build_data_pipeline()
    df_processed_data.to_csv('results/processed_data.csv')


if __name__ == "__main__":
    generate_analysis_results()
