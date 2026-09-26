from src.week1 import (
    try_points, conversion_points, penalty_points, drop_goal_points,
    total_score, is_valid_conversion_count, result_message,)


def test_try_points():
    assert try_points(3) == 15


def test_conversion_points():
    assert conversion_points(2) == 4


def test_penalty_points():
    assert penalty_points(3) == 9


def test_drop_goal_points():
    assert drop_goal_points(2) == 6


def test_total_score():
    assert total_score(2, 2, 1, 0) == 17


def test_valid_conversion_count():
    assert is_valid_conversion_count(3, 2) is True


def test_invalid_conversion_count():
    assert is_valid_conversion_count(3, 4) is False


def test_result_message():
    assert (
        result_message("Exeter", 24)
        == "Exeter scored 24 points."
    )
