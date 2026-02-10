## LangChain and Model Context Protocol (MCP) Example
This project demonstrates how to create a LangChain agent that utilizes custom tools exposed via the Model Context Protocol (MCP). The example includes a simple tool server for string manipulation and a main script that runs an agent to interact with these tools.

### Prerequisites
Before you begin, ensure you have the following installed on your system:

* Python 3.12

* Conda (Miniconda or Anaconda)

* A Google API Key for the Gemini model. This key must be set as an environment variable named `GOOGLE_API_KEY`.

### Setup
* Create and Activate the Conda Environment:

    The `environment.yml` file specifies all the necessary dependencies. 
    
    Navigate to the project directory and run the following command to create the environment:
    ```
    conda env create -f environment.yml
    ```

* Activate the Environment:
    After the environment is created, activate it with this command:
    ```
    conda activate mcp-env
    ```
* Set Your Google API Key:

    Make sure your GOOGLE_API_KEY is set in your environment.

    On Linux/macOS:
    ```
    export GOOGLE_API_KEY="your-api-key"
    ```
    On Windows (Command Prompt):
    ```
    set GOOGLE_API_KEY="your-api-key"
    ```

### Running the Example
Once the environment is set up and activated, you can run the main agent script. The `run_agent.py` script will automatically start the tool server in the background and use the tools.
```
python run_agent.py
```

### Code Explanation
`string_tools_server.py`:

This script serves as the tool provider. It uses the FastMCP class to create a server that exposes specific Python functions as callable tools.

* `FastMCP("StringTools")`: Initializes a new MCP server.

* `@mcp.tool()`: This decorator registers a Python function as a tool that the agent can discover and use.

* The reverse_string and count_words functions are simple, self-contained tools that an AI agent can call.

* `mcp.run(transport="stdio")`: Starts the server using the standard I/O transport, which allows it to communicate with the client script.

`run_agent.py`
This is the main script that orchestrates the agent's behavior.

* `MultiServerMCPClient`: This class is the core component for connecting to the MCP tool server. It is configured to use the stdio transport to communicate with string_tools_server.py.

* `tools = await client.get_tools()`: Retrieves the list of available tools from the connected server.

* `ChatGoogleGenerativeAI(model="gemini-1.5-flash")`: Initializes the language model that will power the agent's reasoning.

* `create_react_agent(model, tools)`: This function from langgraph creates a "ReAct" style agent. This type of agent can reason, decide which tool to use, and generate a final response based on the tool's output.

* `agent.ainvoke(...)`: Sends a prompt to the agent and waits for a response. The agent will determine if it needs to use a tool to fulfill the request. In the provided examples, it uses the reverse_string and count_words tools.

### Expected Output
When you run python `run_agent.py`, the console output will look like this:

```
Processing request of type ListToolsRequest
Processing request of type CallToolRequest
Processing request of type ListToolsRequest
Reverse response: The reversed string is 'dlrow olleh'.
Processing request of type CallToolRequest
Processing request of type ListToolsRequest
Word-count response: There are 5 words.
```
