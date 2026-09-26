def winner(match):
    """
    Determine the winner of a match.
    The match is represented as a tuple containing:
    (
        home_team,
        away_team,
        home_score,
        away_score
    )
    Return the name of the winning team.
    If the scores are equal, return 'Draw'.
    Parameters
    ----------
    match : tuple
    Returns
    -------
    str
    Examples
    --------
    >>> winner(('Exeter', 'Bath', 24, 18))
    'Exeter'
    >>> winner(('Exeter', 'Bath', 21, 21))
    'Draw'
    HINT: Consider using tuple unpacking
    """
    pass


def average_score(scores):
    """
    Calculate the mean score from a list of scores.
    Parameters
    ----------
    scores : list[int]
    Returns
    -------
    float
    Examples
    --------
    >>> average_score([20, 30, 40])
    30.0
    HINT: do this without using a pre-written average or mean function
    """
    pass


def highest_score(scores):
    """
    Find the highest value in a list of scores.
    Parameters
    ----------
    scores : list[int]
    Returns
    -------
    int
    Examples
    --------
    >>> highest_score([10, 25, 17])
    25
    HINT: Do this without using a pre-built max function
    """
    pass


def team_win_percentage(team):
    """
    Calculate a team's win percentage.
    The team dictionary contains:
    {
        "name": str,
        "wins": int,
        "losses": int
    }
    Win percentage is:
        wins / (wins + losses) * 100
    Parameters
    ----------
    team : dict
    Returns
    -------
    float
    Examples
    --------
    >>> win_percentage(
    ...     {"name": "Exeter", "wins": 12, "losses": 3}
    ... )
    80.0
    """
    pass


def home_team_won(match):
    """
    Determine whether the home team won.
    The match dictionary contains:
    {
        "home_team": str,
        "away_team": str,
        "home_score": int,
        "away_score": int
    }
    Parameters
    ----------
    match : dict
    Returns
    -------
    bool
    Examples
    --------
    >>> home_team_won(
    ...     {
    ...         "home_team": "Exeter",
    ...         "away_team": "Bath",
    ...         "home_score": 24,
    ...         "away_score": 18,
    ...     }
    ... )
    True
    """
    pass


def total_points_for(matches):
    """
    Calculate the total points scored across a season.
    The season is represented as a list of dictionaries.
    Parameters
    ----------
    matches : list[dict]
    Returns
    -------
    int
    Examples
    --------
    >>> total_points_for(
    ...     [
    ...         {"points_for": 24},
    ...         {"points_for": 18},
    ...     ]
    ... )
    42
    """
    pass


def count_wins(matches):
    """
    Count the number of matches won.
    A match is considered a win when
    points_for > points_against.
    Parameters
    ----------
    matches : list[dict]
    Returns
    -------
    int
    Examples
    --------
    >>> count_wins(
    ...     [
    ...         {
    ...             "points_for": 24,
    ...             "points_against": 18
    ...         },
    ...         {
    ...             "points_for": 10,
    ...             "points_against": 12
    ...         },
    ...     ]
    ... )
    1
    """
    pass
