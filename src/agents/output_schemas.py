from langchain_core.pydantic_v1 import BaseModel, Field
from typing import Optional

# COMPETITION
class ListCompetitionsOutput(BaseModel):
    group: str = Field(default="general", description="Search for competitions in a specific group.Valid options are 'general', 'entered', and 'inClass'")
    category: str = Field(default=None, description="Search for competitions of a specific category.Valid options are 'all', 'featured', 'research', 'recruitment', 'gettingStarted', 'masters', and 'playground'")
    sort_by: str = Field(default="latestDeadline", description="How to sort the result.Default is 'latestDeadline'. Valid options are 'grouped', 'prize', 'earliestDeadline', 'latestDeadline', 'numberOfTeams', and 'recentlyCreated'")
    page: int = Field(default=1, description="The page number to return")
    search: str = Field(default=None, description="Search term(s) to use")

class DownloadCompetitionFilesOutput(BaseModel):
    competition: str = Field(default=None, description="The name of the competition")
    competition_opt: str = Field(default=None, description="Alternative competition option provided by cli")
    file_name: str = Field(deafult=None, description="The configuration file name, all files are donwloaded if not provided")
    path: str = Field(default=None, description="Path to download the file to")
    force: bool = Field(default=None, description="Force the download if the file already exists")
    quiet: bool = Field(default=None, description="Suppress verbose output") 

class SubmitCompetitionOutput(BaseModel):
    file_name: str = Field(default=None, description="The competition metadata file")
    message: str = Field(default=None, description="The submission description")
    competition: str = Field(default=None, description="The name of the competition")
    competition_opt: str = Field(default=None, description="Alternative competition option provided by cli")

class ListCompetitionSubmissionsOutput(BaseModel):
    competition: str = Field(default=None, description="The name of the competition.")
    competition_opt: str = Field(default=None, description="Alternative competition option provided by cli")
    csv_display: bool = Field(default=True, description="Option to print comma separated values") 
    quiet: bool = Field(default=None, description="Suppress verbose output") 

class GetCompetitionLeaderboardOutput(BaseModel):
    competition: str = Field(default=None, description="The name of the competition")
    competition_opt: str = Field(default=None, description="Alternative competition option provided by cli")
    path: str = Field(default=None, description="Path to download the file to")
    view: bool = Field(default=True, description="Show the results in terminal")
    download: bool = Field(default=True, description="Download the entire leaderboard")
    csv_display: bool = Field(default=False, description="Option to print comma separated values") 
    quiet: bool = Field(default=None, description="Suppress verbose output") 

# DATASET
class ListDatasetOutput(BaseModel):
    search_term: Optional[str] = Field(default="", description="A search term to use")
    page_size: int = Field(default=20, description="Number of datasets to return per page")
    sort_by: str = Field(default='hottest', description="How to sort the result. Valid options are 'hottest', 'votes', 'updated', and 'active'")
    file_type: str = Field(default='all', description="Search for datasets with a specific file type. Valid options are 'all', 'csv', 'sqlite', 'json', and 'bigQuery'")
    license_name: str = Field(default='all', description="Search for datasets with a specific license. Valid options are 'all', 'cc', 'gpl', 'odb', and 'other'")
    tag_ids: Optional[list] = Field(default=None, description="Search for datasets that have specific tags. Tag list should be comma separated")
    user: Optional[str] = Field(default=None, description="Username to filter the search to")
    mine: bool = Field(default=False, description='Boolean, if True, group is changed to "my" to return personal datasets')
    page: int = Field(default=1, description="The page to return (default is 1)")
    max_size: Optional[int] = Field(default=None, description="The maximum size of the dataset to return (bytes)")
    min_size: Optional[int] = Field(default=None, description="The minimum size of the dataset to return (bytes)")

class ListDatasetFilesOutput(BaseModel):
    dataset: str = Field(default=None, description="Name of the dataset.The string identified of the dataset should be in format [owner]/[dataset-name]"),
    dataset_opt: str = Field(default=None, description="Alternative option to providing a dataset")
    csv_display: bool = Field(default=False, description="Option to print comma separated values") 

class DownloadDatasetOutput(BaseModel):
    dataset: str = Field(default=None, description="Name of the dataset.The string identified of the dataset should be in format [owner]/[dataset-name]")
    dataset_opt: str = Field(default=None, description="Alternative option to providing a dataset")
    file_name: str = Field(default=None, dexcription="The dataset configuration file")
    path: str = Field(default=None, dexcription="The path to download the dataset to")
    force: bool = Field(default=False, dexcription="Force the download if the file already exists")
    quiet: bool = Field(default=False, dexcription="Suppress verbose output")
    unzip: bool = Field(default=False, dexcription="If True, unzip files upon download") 

output_schemas_dict = {
    'list_competitions': ListCompetitionsOutput,
    'download_competition_file': DownloadCompetitionFilesOutput,
    'submit_sompetition': SubmitCompetitionOutput,
    'list_competition_submission': ListCompetitionSubmissionsOutput,
    'get_competition_leaderboard': GetCompetitionLeaderboardOutput,
    'list_datasets': ListDatasetOutput,
    'list_dataset_files': ListDatasetFilesOutput,
    'download_dataset': DownloadDatasetOutput
}