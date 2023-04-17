""" main.py


"""

import pandas as pd

import utils


def fuzzy_colnames(df):
    """ Renames the columns in `df` according to the following criteria (in
    this order):

    For each column label:

        1. Reverse the string (e.g., column "ABC" becomes "CBA").

        2. If the column label includes the (upper case) letter "B", we have
        two cases:

            a. If the (lower case) letter "b" is NOT in the column name,
            reverse the case of any occurrence of "B" (so each upper case "B"
            will become lower case "b").

            b. If the column name also includes the (lower case) letter "b", do
            nothing.

            For example:

            - "CBA" becomes "CbA"
            - "ZbB" does not change (because name includes a lower case "b')
            - "BBa" becomes "bba"
            - "ZZZ" does not change


    Parameters
    ----------
    df : data frame
        Any data frame with strings column labels.

        You can assume that the data frame `df` will only include strings as
        column labels. There is no need to check for that.


    Returns
    -------
    data frame:
        A data frame with column labels renamed according to the criteria
        above. The order of the columns does not matter.


    Example
    -------

    If the data frame `df` is:

             ABC  Xxb  zy  Bxb
        idx
        0      1    0  10   20
        1      0    0  11   21
        2      1    0  12   22

    This function will return the following data frame:

             CbA  bxX  yz  bxB
        idx
        0      1    0  10   20
        1      0    0  11   21
        2      1    0  12   22

    Note: The order of the columns does not matter

    """
    # <COMPLETE THIS PART>
    for column in df.columns:
        col = column
        col = col[::-1]
        if "B" in col:
            if "b" not in col:
                str_list = list(col)
                for i in range(len(str_list)):
                    if str_list[i] == "B":
                        str_list[i] = "b"
                col = ''.join(str(i) for i in str_list)
        df.rename(columns={column: col}, inplace=True)
    return df
# ----------------------------------------------------------------------------
#   Please do not modify this function
# ----------------------------------------------------------------------------
def _mk_test_df():
    """ Creates a testing data frame

             ABC  Xxb  zy  Bxb
        idx
        0      1    0  10   20
        1      0    0  11   21
        2      1    0  12   22

    Notes
    -----

    For this example df, a valid output for `fuzzy_colnames(df)` is


             CbA  bxX  yz  bxB
        idx
        0      1    0  10   20
        1      0    0  11   21
        2      1    0  12   22

    """
    cnts = """
    idx , ABC, Xxb, zy, Bxb
    0   , 1  , 0  , 10, 20
    1   , 0  , 0  , 11, 21
    2   , 1  , 0  , 12, 22
    """
    fcsv = utils.fake_csv_file(cnts)
    df = pd.read_csv(fcsv, index_col='idx')
    return df



if __name__ == "__main__":
    df = _mk_test_df()
    utils.pprint(df, df_info=False)

    res = fuzzy_colnames(df)
    utils.pprint(res, df_info=False)









