import kaggle
from langchain_core.tools import tool
from typing import Optional, List


@tool
def list_competitions(
    group: str = None,
    category: str = None,
    sort_by: str = 'latestDeadline',
    page: int = 1,
    search: str = None
):
    """Useful to retrieve competitions available in Kaggle"""
    args = {k: v for k, v in locals().items() if v is not None and v != ""}
    result = kaggle.api.competitions_list_cli(**args)
    return result

@tool
def download_competition_files(
    competition: str = None,
    competition_opt: str = None,
    file_name: str = None,
    path: str = None,
    force: bool = False,
    quiet: bool = False
):
    """Useful to download competition files available in Kaggle"""
    args = {k: v for k, v in locals().items() if v is not None and v != ""}
    result =  kaggle.api.competition_download_cli(**args)
    return result

@tool
def submit_competition(
    file_name: str = None,
    message: str = None,
    competition: str = None,
    competition_opt: str = None,
):
    """Useful to retrieve competitions available in Kaggle"""
    args = {k: v for k, v in locals().items() if v is not None and v != ""}
    result =  kaggle.api.competition_submit(**args)
    return result

@tool
def list_competition_submissions(
    competition: str = None,
    competition_opt: str = None, 
    csv_display: bool = False,
    quiet: bool = False
):
    """Useful to retrieve competition submission user made in Kaggle"""
    args = {k: v for k, v in locals().items() if v is not None and v != ""}
    result =  kaggle.api.competition_submissions_cli(**args)
    return result

@tool 
def get_competition_leaderboard(
    competition: str = None,
    competition_opt: str = None,
    path: str = None,
    view: bool = True,
    download: bool = False,
    csv_display: bool = False,
    quiet: bool = False
):
    """Useful to retrieve competition leaderboard user made in Kaggle"""
    args = {k: v for k, v in locals().items() if v is not None and v != ""}
    result =  kaggle.api.competition_leaderboard_cli(**args)
    return result