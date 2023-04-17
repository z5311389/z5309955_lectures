""" main.py

"""

import pandas as pd

import utils


def last_by_type_v0(df):
    """ Returns a data frame with the last "row" of DF for each unique
    value of the column "type".

    The last row is defined as the row with the largest index value
    (if DatetimeIndex, the row with the most recent index value).

    Parameters
    ----------
    data frame:
        ANY data frame with at least two columns. One of the columns must
        be called "type". The dtype of the column "type" can be anything.
        The dtype of the other columns must be a numeric type. This data frame
        must not include any NaN.

        You can assume that the `df` data frame will meet the description
        above. There is no need to check for that. For instance, there is not
        need to check that the `df` data frame includes at least two columns,
        or that one of them is called "type", or that it does not include any
        NaN.

    Returns
    -------
    data frame
        Columns: Same columns as df (INCLUDING "type").
                 The order of the columns does not matter

        Index: Unique values of the column "type"

    Example
    -------
    If the data frame is

            type  A  B  C
        idx
        0      x  1  0  1
        1      x  0  0  1
        2      y  1  0  1

    This function will return the following data frame:

              A  B  C type
        type
        x     0  0  1    x
        y     1  0  1    y

    Note: The order of the columns does not matter

    """
    # <COMPLETE THIS PART>

    type_value = ''
    i = 0
    for row in df:



# ----------------------------------------------------------------------------
#   Please do not modify this function
# ----------------------------------------------------------------------------
def _mk_test_df():
    """ Creates a testing data frame


    Notes
    -----

    Given this example data frame a valid output for
    last_by_type_v0(df) is

                     A         B         C  type
        type
        1     3.252369  6.498818  0.802957     1
        2     6.470209  9.675518  8.548817     2

    """
    cnts = """
    date      , type,        A,        B,        C
    2020-01-05,    1, 3.319464, 8.629389, 3.133565
    2020-01-07,    2, 6.421113, 2.182970, 7.779123
    2020-01-07,    1, 1.954982, 2.868030, 4.212673
    2020-01-04,    1, 7.810074, 0.798035, 1.118955
    2020-01-05,    2, 5.606010, 7.690301, 0.688441
    2020-01-06,    2, 6.754960, 7.971680, 0.152985
    2020-01-09,    1, 3.252369, 6.498818, 0.802957
    2020-01-08,    1, 0.130774, 6.271210, 9.657531
    2020-01-09,    2, 6.470209, 9.675518, 8.548817
    2020-01-07,    1, 0.691137, 7.830912, 7.055062
    """
    fcsv = utils.fake_csv_file(cnts)
    df = pd.read_csv(fcsv, parse_dates=['date'], index_col='date')
    return df


if __name__ == "__main__":
    df = _mk_test_df()
    utils.pprint(df, df_info=False)

    res = last_by_type_v0(df)
    utils.pprint(res, df_info=False)













