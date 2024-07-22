import kaggle
from langchain_core.tools import tool
from typing import Optional, List

@tool
def list_datasets(
    search_term: str = "",
    sort_by: str = 'hottest',
    file_type: str = 'all',
    license_name: str = 'all',
    tag_ids: Optional[List[str]] = None,
    user: Optional[str] = None,
    mine: bool = False,
    page: int = 1,
    max_size: Optional[int] = None,
    min_size: Optional[int] = None
):
    """Useful to retrieve datasets available in Kaggle"""
    args = {k: v for k, v in locals().items() if v is not None and v != ""}
    if tag_ids:
        args['tag_ids'] = ','.join(tag_ids)
    if mine:
        args['group'] = 'my'
    result = kaggle.api.dataset_list_cli(**args)
    return result

@tool
def list_dataset_files(
    dataset: str = None,
    dataset_opt: str = None,
    csv_display: bool = False
):
    """Useful to download competitions available in Kaggle"""
    args = {k: v for k, v in locals().items() if v is not None and v != ""}
    result =  kaggle.api.dataset_list_files_cli(**args)
    return result

@tool
def download_dataset(
    dataset: str = None,
    dataset_opt: str = None,
    file_name: str = None,
    path: str = None,
    force: bool = False,
    quiet: bool = False,
    unzip: bool = False
):
    """Useful to download competitions available in Kaggle"""
    args = {k: v for k, v in locals().items() if v is not None and v != ""}
    result =  kaggle.api.competition_download_cli(**args)
    return result