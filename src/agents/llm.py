import json
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
from tools.competitions import list_competitions, download_competition_files, submit_competition, list_competition_submissions, get_competition_leaderboard
from tools.datasets import list_datasets, list_dataset_files,  download_dataset

class ConfigureLLM:

    def __init__(self):
        self.tools = [list_competitions, download_competition_files, submit_competition, list_competition_submissions, get_competition_leaderboard,
         list_datasets, list_dataset_files,  download_dataset]
        
        with open('./settings/settings.json', 'r') as file:
            self.settings = json.load(file)
        

    def create_llm(self):

        provider = self.settings['provider']
        model= self.settings['model']
        api_key = self.settings['api_key']

        if provider == 'groq':
            if api_key:

                llm = ChatGroq(
                    model= model,
                    api_key = api_key
                )

                llm_with_tools = llm.bind_tools(self.tools)
            
                return (llm, llm_with_tools)
                
            else:
                raise Exception('API key not provided.')
        
        if provider == 'ollama':

            llm = ChatOllama(
                    model= model
                )
            
            return (llm, llm_with_tools)
        


            
            

        
    


