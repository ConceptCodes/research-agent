# Research Agent

A research assistant powered by LangGraph and LangChain. This assistant is designed to provide accurate, concise, and well-researched information by interpreting user queries, gathering reliable information and summarizing findings.

![Preview](https://i.imgur.com/kwOzJCz.png)

## Tools

- Wikipedia
- DuckDuckGo Search
- Wolfram Alpha
- Google Scholar
- Google Trends
- Google Finance
- PubMed
- Merriam-Webster Dictionary
- Stack Exchange


## Installation

1. Clone the repository:
    ```sh
    git clone https://conceptcodes.github.com/research-agent.git
    ```
    cd research-agent
    ```

2. Copy the `.env.example` file to `.env` and fill in your API keys.
    ```sh
    cp .env.example .env
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the main script:
    ```sh
    python agent.py
    ```

2. Interact with the research assistant by typing your queries. Type `exit` to quit.

## Project Structure
- [agent.py](http://_vscodecontentref_/0): Entry point of the application. Sets up the CLI and handles user input.
- [llm.py](http://_vscodecontentref_/1): Configures the language model to be used.
- [prompt.py](http://_vscodecontentref_/2): Contains the system message template for the assistant.
- [tools.py](http://_vscodecontentref_/3): Defines various tools for searching and querying information.
- [utils.py](http://_vscodecontentref_/4): Utility functions for displaying steps and handling errors.

## License

This project is licensed under the MIT License. See the LICENSE file for details.