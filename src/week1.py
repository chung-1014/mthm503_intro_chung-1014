def try_points(tries):
    """
    Calculate the number of points scored from tries.
    Each try is worth 5 points.
    Parameters
    ----------
    tries : int
        Number of tries scored.
    Returns
    -------
    int
        Total points scored from tries.
    Examples
    --------
    >>> try_points(3)
    15
    >>> try_points(0)
    0
    """
    pass


def conversion_points(conversions):
    """
    Calculate the number of points scored from conversions.
    Each successful conversion is worth 2 points.
    Parameters
    ----------
    conversions : int
        Number of successful conversions.
    Returns
    -------
    int
        Total points scored from conversions.
    Examples
    --------
    >>> conversion_points(2)
    4
    """
    pass


def penalty_points(penalties):
    """
    Calculate the number of points scored from penalties.
    Each penalty goal is worth 3 points.
    Parameters
    ----------
    penalties : int
        Number of penalty goals.
    Returns
    -------
    int
        Total points scored from penalties.
    Examples
    --------
    >>> penalty_points(4)
    12
    """
    pass


def drop_goal_points(drop_goals):
    """
    Calculate the number of points scored from drop goals.
    Each drop goal is worth 3 points.
    Parameters
    ----------
    drop_goals : int
        Number of drop goals.
    Returns
    -------
    int
        Total points scored from drop goals.
    Examples
    --------
    >>> drop_goal_points(2)
    6
    """
    pass


def total_score(tries, conversions, penalties, drop_goals):
    """
    Calculate the total score for a rugby team.
    The total score is the sum of points from:
    - tries
    - conversions
    - penalties
    - drop goals
    Parameters
    ----------
    tries : int
        Number of tries.
    conversions : int
        Number of conversions.
    penalties : int
        Number of penalty goals.
    drop_goals : int
        Number of drop goals.
    Returns
    -------
    int
        Total points scored.
    Examples
    --------
    >>> total_score(2, 2, 1, 0)
    17
    HINT: use the various functions you have constructed before to develop a solution
    """
    pass


def is_valid_conversion_count(tries, conversions):
    """
    Determine whether a conversion count is valid.
    A conversion can only occur after a try.
    Therefore the number of conversions cannot exceed
    the number of tries.
    Parameters
    ----------
    tries : int
        Number of tries scored.
    conversions : int
        Number of successful conversions.
    Returns
    -------
    bool
        True if conversions <= tries, otherwise False.
    Examples
    --------
    >>> is_valid_conversion_count(3, 2)
    True
    >>> is_valid_conversion_count(3, 4)
    False
    """
    pass


def result_message(team_name, score):
    """
    Create a message describing a team's score.
    Parameters
    ----------
    team_name : str
        The team's name.
    score : int
        The team's score.
    Returns
    -------
    str
        Message of the form:
        '<team_name> scored <score> points.'
    Examples
    --------
    >>> result_message('Exeter', 24)
    'Exeter scored 24 points.'
    HINT: Use a so-called f-string
    """
    pass
