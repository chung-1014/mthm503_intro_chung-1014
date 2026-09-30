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
    home_team, away_team, home_score, away_score = match
    if home_score > away_score:
        return home_team    
    
    elif away_score > home_score:
        return away_team
    
    elif home_score == away_score:
        return "Draw"


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
    total = 0
    for score in scores:
        total += score

    return total / len(scores)

    
    


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
    highest = scores[0]
    for score in scores:
        if score > highest:
            highest = score

    return highest


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
    team_wins = team["wins"]
    team_losses = team["losses"]
    total_games = team_wins + team_losses
    team_win_percentage = (team_wins / total_games) * 100
    return team_win_percentage


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
    if match["home_score"] > match["away_score"]:
        return True
    else:
        return False

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
    total_points = 0
    for match in matches:
        total_points += match["points_for"]
    return total_points


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
    wins = 0
    for match in matches:
        if match["points_for"] > match["points_against"]:
            wins += 1
    return wins
