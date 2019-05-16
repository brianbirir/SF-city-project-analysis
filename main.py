import pandas as pd

FILE_SOURCE = 'src/City Council Planning Comm Notes.xlsx'


def dataset_reader():
    """Loads the data set from a file source

    Returns:
        dataFrame: The pandas data structure of the file records
    """
    # convert Excel file to data frame
    records = pd.read_excel(FILE_SOURCE)
    return records
