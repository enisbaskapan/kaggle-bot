from agents.llm import ConfigureLLM
from tools.competitions import list_competitions, download_competition_files, submit_competition, list_competition_submissions, get_competition_leaderboard
from tools.datasets import list_datasets, list_dataset_files,  download_dataset
from agents.agent import Agent

class Nodes(Agent, ConfigureLLM):

    def __init__(self):

        super().__init__()

        self.tool_dict = {
            'list_competitions': list_competitions,
            'download_competition_files': download_competition_files,
            'submit_competition': submit_competition,
            'list_competition_submissions': list_competition_submissions,
            'get_competition_leaderboard': get_competition_leaderboard,
            'list_datasets' : list_datasets,
            'list_dataset_files': list_dataset_files,
            'download_dataset': download_dataset
        }

        self.llm, self.llm_with_tools = self.create_llm()

    def args_extractor(self, state):
        """Extract relevant arguments from user query"""
        print("\n🔎 Extracting Arguments 🔎\n")
        query = state['query']

        function = self.llm_with_tools.invoke(query).tool_calls[0]['name']
        args_extractor_agent = self.create_args_extractor_agent(self.llm, function)   
        print('🤖 Agent Created 🤖\n')
        args = args_extractor_agent.invoke({"query": query})
        print('✅ Arguments Extracted ✅\n')

        return {"args": args, "function": function}
    
    def tool_executor(self, state):
        """Execute tools with arguments"""
        print("🔧 Executing Tools 🔧\n")

        function = state['function']
        args = state['args']
        
        result = self.tool_dict[function].invoke(args)
        import pprint
        pprint.pprint(result)
        
    
    