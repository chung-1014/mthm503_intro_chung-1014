import pandas as pd   # noqa: F401


def select_column(df, column):
    """
    Given a DataFrame 'df' and the name of a column 'column',
    return that column as a pandas Series.

    Parameters
    ----------
    df : pandas.DataFrame
        The input DataFrame.
    column : str
        The name of the column to select.

    Returns
    -------
    pandas.Series
        The selected column.
    """
    return df[column]


def column_mean(df, column):
    """
    Given a DataFrame 'df' and the name of a numeric column 'column',
    return the mean of that column.

    Parameters
    ----------
    df : pandas.DataFrame
        The input DataFrame.
    column : str
        The name of the numeric column.

    Returns
    -------
    float
        The mean value of the specified column.
    """
    return df[column].mean()



def filter_rows(df, column, threshold):
    """
    Given a DataFrame 'df', the name of a numeric column 'column',
    and a threshold value 'threshold', return only the rows where
    the column value is greater than the threshold.

    Parameters
    ----------
    df : pandas.DataFrame
        The input DataFrame.
    column : str
        The column used for filtering.
    threshold : float
        The threshold value.

    Returns
    -------
    pandas.DataFrame
        Rows for which df[column] > threshold.
    """
    return df[df[column] > threshold]


def sort_by_column(df, column, ascending=True):
    """
    Given a DataFrame 'df' and a column name 'column',
    return the DataFrame sorted by that column.

    Parameters
    ----------
    df : pandas.DataFrame
        The input DataFrame.
    column : str
        The column used for sorting.
    ascending : bool, default=True
        If True, sort in ascending order.
        If False, sort in descending order.

    Returns
    -------
    pandas.DataFrame
        The sorted DataFrame.
    """
    return df[column].sort_value()


def unique_values(df, column):
    """
    Given a DataFrame 'df' and the name of a column 'column',
    return the unique values in that column.

    Parameters
    ----------
    df : pandas.DataFrame
        The input DataFrame.
    column : str
        The column whose unique values are required.

    Returns
    -------
    numpy.ndarray
        Array of unique values.
    """
    pass


def frequencies_by_group(df, cat_col):
    """
    Given a DataFrame 'df' and the name of a categorical column
    'cat_col', return the frequency count of each category.

    Parameters
    ----------
    df : pandas.DataFrame
        The input DataFrame.
    cat_col : str
        The categorical column.

    Returns
    -------
    pandas.Series
        Frequency counts indexed by category.
    """
    pass


def mean_by_group(df, value_col, group_col):
    """
    Given a DataFrame 'df', a numeric column 'value_col',
    and a grouping column 'group_col', calculate the mean
    of the numeric column for each group.

    Parameters
    ----------
    df : pandas.DataFrame
        The input DataFrame.
    value_col : str
        The numeric column to summarise.
    group_col : str
        The column defining the groups.

    Returns
    -------
    pandas.Series
        Group means indexed by group.
    """
    pass


def add_ratio_column(df, numerator, denominator, new_col):
    """
    Given a DataFrame 'df', calculate the ratio of the
    'numerator' column to the 'denominator' column and
    return a new DataFrame containing an additional column.

    The original DataFrame must not be modified.

    Parameters
    ----------
    df : pandas.DataFrame
        The input DataFrame.
    numerator : str
        Column containing numerator values.
    denominator : str
        Column containing denominator values.
    new_col : str
        Name of the new ratio column.

    Returns
    -------
    pandas.DataFrame
        A new DataFrame including the ratio column.
    """
    pass


def drop_missing(df):
    """
    Given a DataFrame 'df', remove rows containing one
    or more missing values.

    Parameters
    ----------
    df : pandas.DataFrame
        The input DataFrame.

    Returns
    -------
    pandas.DataFrame
        DataFrame with missing-value rows removed.
    """
    pass


def fill_missing(df, value):
    """
    Given a DataFrame 'df' and a replacement value 'value',
    return a DataFrame where all missing values have been
    replaced with that value.

    Parameters
    ----------
    df : pandas.DataFrame
        The input DataFrame.
    value :
        Replacement value for missing entries.

    Returns
    -------
    pandas.DataFrame
        DataFrame with missing values filled.
    """
    pass
