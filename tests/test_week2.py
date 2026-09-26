from src.week2 import (
    winner, average_score, highest_score, team_win_percentage,
    home_team_won, total_points_for, count_wins)


def test_home_team_wins():
    match = ("Exeter", "Bath", 25, 18)
    assert winner(match) == "Exeter"


def test_away_team_wins():
    match = ("Exeter", "Bath", 18, 25)

    assert winner(match) == "Bath"


def test_draw():
    match = ("Exeter", "Bath", 20, 20)

    assert winner(match) == "Draw"


def test_average_score():
    assert average_score([20, 30, 40]) == 30.0


def test_highest_score():
    assert highest_score([20, 30, 40]) == 40


def test_team_win_percentage():
    team = {
        "name": "Exeter",
        "wins": 12,
        "losses": 3,
    }

    assert team_win_percentage(team) == 80.0


def test_home_team_won():
    match = {
        "home_team": "Exeter",
        "away_team": "Bath",
        "home_score": 24,
        "away_score": 18,
    }

    assert home_team_won(match) is True


def test_total_points_for():
    matches = [
        {"points_for": 24},
        {"points_for": 18},
    ]

    assert total_points_for(matches) == 42


def test_count_wins():
    matches = [
        {
            "points_for": 24,
            "points_against": 18,
        },
        {
            "points_for": 15,
            "points_against": 22,
        },
        {
            "points_for": 20,
            "points_against": 10,
        },
    ]

    assert count_wins(matches) == 2
