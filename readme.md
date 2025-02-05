# Research Agent

A research assistant powered by LangGraph and LangChain. This assistant is designed to provide accurate, concise, and well-researched information by interpreting user queries, gathering reliable information and summarizing findings.

![Preview](https://i.imgur.com/kwOzJCz.png)

## Tools

| Tool                        | Description                                      | API Key Required |
|-----------------------------|--------------------------------------------------|------------------|
| Wikipedia                   | Free online encyclopedia                         |                  |
| DuckDuckGo Search           | Privacy-focused search engine                    |                  |
| Wolfram Alpha               | Computational knowledge engine                   | ✅               |
| Google Scholar              | Search engine for scholarly articles             | ✅               |
| Google Trends               | Analyzes the popularity of search queries        | ✅               |
| Google Finance              | Financial news and data                          | ✅               |
| PubMed                      | Database of biomedical literature                |                  |
| Merriam-Webster Dictionary  | Online dictionary and thesaurus                  | ✅               |
| Stack Exchange              | Network of Q&A communities                       |                  |


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/conceptcodes/research-agent.git
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
- [agent.py](/agent.py): Entry point of the application. Sets up the CLI and handles user input.
- [llm.py](/lib/llm.py): Configures the language model to be used.
- [prompt.py](/lib/prompt.py): Contains the system message template for the assistant.
- [tools.py](/lib/tools.py): Defines various tools for searching and querying information.
- [utils.py](/lib/utils.py): Utility functions for displaying steps and handling errors.

## Roadmap
- [ ] Add more tools for specialized searches.
- [ ] Implement a feedback mechanism to improve the assistant's responses.
- [ ] Enhance the summarization capabilities of the assistant.
- [ ] Add support for more languages. (ES, FR, DE, JA, KO, HI, RU)

## License

This project is licensed under the MIT License. See the LICENSE file for details.