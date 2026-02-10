## Multi-Terminal Agent-to-Agent (A2A) Protocol Demo
This project demonstrates a realistic **Agent-to-Agent (A2A) protocol**, where independent agents communicate using structured A2A cards. Each agent runs in its own terminal, processes tasks asynchronously, and responds with structured messages. The example includes two simple agents — one that reverses strings and one that counts words — and an orchestrator that sends tasks to them.

### Prerequisites
Before you begin, ensure you have the following installed on your system:

* Python 3.12
* Conda (Miniconda or Anaconda)
* `aiohttp` library for asynchronous HTTP communication

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
    conda activate a2a-env
    ```

* Install `aiohttp` (if not already installed via environment.yml):

    ```
    pip install aiohttp
    ```

### Running the Example
This demo requires three terminals: one for each agent and one for the orchestrator.

* Terminal 1 — Run Agent Alpha (word-count agent):
    ```
    python agent_alpha.py
    ```

* Terminal 2 — Run Agent Beta (string-reverse agent):
    ```
    python agent_beta.py
    ```

* Terminal 3 — Run the orchestrator:
    ```
    python run_a2a.py
    ```

The orchestrator sends tasks to each agent and prints their responses.

### Code Explanation
`agent_alpha.py`:

This script runs Agent Alpha, which counts the number of words in the provided text.

* Uses `aiohttp` to start an async HTTP server on port 8001.
* `handle_card(request)`: Receives A2A cards, checks for `count_words` action, and returns a structured response card with the word count.

`agent_beta.py`:

This script runs Agent Beta, which reverses a given string.

* Uses `aiohttp` to start an async HTTP server on port 8002.
* `handle_card(request)`: Receives A2A cards, checks for `reverse_string` action, and returns a structured response card with the reversed string.

`run_a2a.py`:

This is the orchestrator script that coordinates tasks between the agents.

* `send_card(agent_url, card)`: Sends a structured A2A card to the specified agent via HTTP POST.
* Sends a `reverse_string` task to Agent Beta and prints the response.
* Sends a `count_words` task to Agent Alpha and prints the response.

### Expected Output
When you run the orchestrator (`run_a2a.py`), the console output will look like this:
```
Beta Response: {'type': 'response', 'action': 'reverse_string', 'payload': {'result': 'dlrow olleh'}}
Alpha Response: {'type': 'response', 'action': 'count_words', 'payload': {'count': 4}}
```
