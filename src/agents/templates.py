command_extractor_template="""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
    Each command refers to a function.
    Analyze the query and select the command that can best be used to answer the query.\
    Below are the possible commands:
    
    list_competitions
    download_competition_file
    submit_sompetition
    list_competition_submission
    get_competition_leaderboard
    list_datasets
    list_dataset_files
    download_dataset
    
    Output should be just the command.
    
    <|eot_id|><|start_header_id|>user<|end_header_id|>
    query: {query}
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
    """

args_extractor_template ="""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
    Analyze the query and extract the relevant arguments from the query if you detect any.\
    {format_instructions}
    Output the whole schema even if yo dont find the arguments.
    <|eot_id|><|start_header_id|>user<|end_header_id|>
    query: {query}
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
    """