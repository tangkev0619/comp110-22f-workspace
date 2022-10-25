"""Dictionary related utility functions."""

__author__ = "730578568"

from csv import DictReader

DATA_DIRECTORY = "../../data"
DATA_FILE_PATH = f"{DATA_DIRECTORY}/nc_durham_2015_march_21_to_26.csv"


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done. 
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result 


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result 


def head(cb_table: dict[str, list[str]], number_of_rows: int) -> dict[str, list[str]]:
    """This function produce a new column-based table with only the first N rows of data for each column."""
    return_table: dict[str, list[str]] = {}
    for i in cb_table:
        list_to_store: list[str] = []
        num_rows: int = number_of_rows
        if number_of_rows >= len(cb_table[i]):
            num_rows = len(cb_table[i])
        for x in range(num_rows):
            list_to_store.append(cb_table[i][x])
        return_table[i] = list_to_store
    return return_table


def select(column_based_table: dict[str, list[str]], names_of_columns: list[str]) -> dict[str, list[str]]:
    """This function produce a new column-based table with only a specific subset of the original columns."""
    rtn_table: dict[str, list[str]] = {}
    for i in column_based_table:
        if i in names_of_columns:
            rtn_table[i] = (column_based_table[i])
    return rtn_table


def concat(cbt1: dict[str, list[str]], cbt2: dict[str, list[str]]) -> dict[str, list[str]]:
    """This function produce a new column-based table with two column-based tables combined."""
    cbt3: dict[str, list[str]] = {}
    for i in cbt1:
        cbt3[i] = (cbt1[i])
    for i in cbt2:
        if i in cbt3:
            cbt3[i] += (cbt2[i])
        else: 
            cbt3[i] = (cbt2[i])
    return cbt3


def count(list1: list[str]) -> dict[str, int]:
    """This function counts the different itens in a list[str] and return it as dict(str, int)."""
    rtn_table: dict[str, int] = {}
    for i in list1:
        if i in rtn_table:
            rtn_table[i] += 1
        else:
            rtn_table[i] = 1
    return rtn_table