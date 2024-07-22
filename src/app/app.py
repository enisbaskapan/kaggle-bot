from agents.llm import ConfigureLLM
from graph.graph import WorkFlow

app = WorkFlow().app

print('\nWelcome to 🔵 KaggleBot 🔵\n')

if __name__ == "__main__":

    verbose = False

    while True:
        query = input("Please enter your command (type 'exit' to exit): ")
        if query.lower() == "exit":
            break
        
        inputs = {"query": query}

        try:
            for event in app.stream(
                inputs
                ):
                if verbose:
                    print("\n", event)
                else:
                    print("\n")
        except Exception as e:
            print('Error understanding the query\n')
