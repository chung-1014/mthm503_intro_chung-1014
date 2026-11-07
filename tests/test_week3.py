import numpy as np
import pandas as pd
import pandas.testing as pdt

from src.week3 import (
    select_column,
    column_mean,
    filter_rows,
    sort_by_column,
    unique_values,
    frequencies_by_group,
    mean_by_group,
    add_ratio_column,
    drop_missing,
    fill_missing,
)


def test_select_column():
    df = pd.DataFrame({"a": [1, 2, 3],
                       "b": [4, 5, 6]})
    expected = pd.Series([1, 2, 3], name="a",)
    result = select_column(df, "a")
    pdt.assert_series_equal(result, expected)


def test_column_mean():
    df = pd.DataFrame({"score": [10, 20, 30, 40]})
    assert column_mean(df, "score") == 25.0


def test_filter_rows():
    df = pd.DataFrame({"name": ["A", "B", "C", "D"],
                       "score": [10, 20, 30, 40]})
    expected = pd.DataFrame({"name": ["C", "D"],
                             "score": [30, 40]}, index=[2, 3])
    result = filter_rows(df, "score", 25)
    pdt.assert_frame_equal(result, expected)


def test_sort_by_column_ascending():
    df = pd.DataFrame({"name": ["C", "A", "B"],
                       "score": [30, 10, 20]})
    expected = pd.DataFrame({"name": ["A", "B", "C"],
                             "score": [10, 20, 30]}, index=[1, 2, 0],)
    result = sort_by_column(df, "score")
    pdt.assert_frame_equal(result, expected)


def test_sort_by_column_descending():
    df = pd.DataFrame({"name": ["C", "A", "B"],
                       "score": [30, 10, 20]})
    expected = pd.DataFrame({"name": ["C", "B", "A"],
                             "score": [30, 20, 10]}, index=[0, 2, 1])
    result = sort_by_column(df, "score", ascending=False)
    pdt.assert_frame_equal(result, expected)


def test_unique_values():
    df = pd.DataFrame({"species": ["Adelie", "Gentoo", "Adelie", "Chinstrap",]})
    expected = np.array(["Adelie", "Gentoo", "Chinstrap"])
    result = unique_values(df, "species")
    np.testing.assert_array_equal(result, expected)


def test_frequencies_by_group():
    df = pd.DataFrame({"species": ["Adelie", "Gentoo", "Adelie", "Adelie",]})
    expected = pd.Series([3, 1], index=pd.Index(["Adelie", "Gentoo"],
                                                name="species"),
                         name="count")
    result = frequencies_by_group(df, "species")
    pdt.assert_series_equal(result, expected)


def test_mean_by_group():
    df = pd.DataFrame({"species": ["Adelie", "Adelie", "Gentoo", "Gentoo",],
                       "bill_length": [38, 42, 48, 52,]})
    expected = pd.Series([40.0, 50.0], index=pd.Index(["Adelie", "Gentoo"], name="species"),
                         name="bill_length",)
    result = mean_by_group(df, value_col="bill_length", group_col="species",)
    pdt.assert_series_equal(result, expected)


def test_add_ratio_column():
    df = pd.DataFrame({"x": [10, 20], "y": [2, 4]})
    expected = pd.DataFrame({"x": [10, 20], "y": [2, 4],
                             "ratio": [5.0, 5.0]})
    result = add_ratio_column(df, numerator="x", denominator="y", new_col="ratio",)
    pdt.assert_frame_equal(result, expected)


def test_add_ratio_column_does_not_modify_original():
    df = pd.DataFrame({"x": [10, 20], "y": [2, 4]})
    add_ratio_column(df, numerator="x", denominator="y", new_col="ratio",)
    assert "ratio" not in df.columns


def test_drop_missing():
    df = pd.DataFrame({"a": [1, np.nan, 3], "b": [4, 5, np.nan]})
    expected = pd.DataFrame({"a": [1.0], "b": [4.0]}, index=[0])
    result = drop_missing(df)
    pdt.assert_frame_equal(result, expected)


def test_fill_missing():
    df = pd.DataFrame({"a": [1, np.nan, 3], "b": [4, 5, np.nan]})
    expected = pd.DataFrame({"a": [1.0, 0.0, 3.0], "b": [4.0, 5.0, 0.0]})
    result = fill_missing(df, 0)
    pdt.assert_frame_equal(result, expected)
