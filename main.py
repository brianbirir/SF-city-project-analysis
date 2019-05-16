import pandas as pd
import numpy as np

FILE_SOURCE = "src/City Council Planning Comm Notes.xlsx"


def dataset_reader():
    """Loads the data set from a file source

    Returns:
        dataFrame: The pandas data structure of the file records
    """
    # convert Excel file to data frame
    records = pd.read_excel(FILE_SOURCE)
    return records


def get_description_column():
    """Extracts the description column from the data source

    Returns:
        dataFrame: The pandas data structure with the description column
    """
    df = dataset_reader()
    return df[['description']]


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
    """Preprocess of text data before analysis

    Returns:
        string: Preprocessed text
    """
    data = remove_punctuation(data)
    preprocessed_data = to_lowercase(data)
    return preprocessed_data


def tokenizer():
    """Convert preprocessed text into terms

    Returns:
        dataFrame: Additional column with list of terms
    """
    df_preprocessed = get_description_column().apply(lambda x: preprocess(x))
    # remove white spaces and split string into a list
    df_preprocessed['terms'] = df_preprocessed['description'].str.strip().str.split()
    return df_preprocessed


if __name__ == "__main__":
    pass
