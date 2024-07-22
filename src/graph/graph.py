from langgraph.graph import END, StateGraph
from .state import GraphState
from .nodes import Nodes
#from .conditional_edges import ConditionalEdges

class WorkFlow():
	
    def __init__(self):
        nodes = Nodes()
        #conditional_edges = ConditionalEdges()
        workflow = StateGraph(GraphState)

        workflow.add_node("args_extractor", nodes.args_extractor)
        workflow.add_node("tool_executor", nodes.tool_executor)


        workflow.set_entry_point("args_extractor")
        workflow.add_edge("args_extractor", "tool_executor")
        workflow.add_edge("tool_executor", END)

        self.app = workflow.compile()