from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from agents.output_schemas import output_schemas_dict
from agents.templates import args_extractor_template

class Agent:

    def create_args_extractor_agent(self, llm, command):
        
        output_schema = output_schemas_dict[command]
        parser = JsonOutputParser(pydantic_object=output_schema)

        args_extractor_prompt = PromptTemplate(template=args_extractor_template, input_variables=['query'], partial_variables={"format_instructions": parser.get_format_instructions()})

        agent = args_extractor_prompt | llm | parser

        return agent