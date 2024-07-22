from typing_extensions import TypedDict
from typing import List

class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        query : user input
        args : arguments to pass for function calling (LLM generation)
        function : function to call (LLM generation)
    """
    query : dict
    args : dict
    function : dict