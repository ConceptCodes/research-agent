import sys
import random
from colorama import init
from halo import Halo
import warnings
from pyfiglet import figlet_format
from termcolor import cprint
from bs4 import GuessedAtParserWarning

from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

from lib.llm import llm
from lib.prompt import system_message
from lib.tools import tools
from lib.utils import display_step, get_error

init(strip=not sys.stdout.isatty())
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=GuessedAtParserWarning)

checkpointer = MemorySaver()

langgraph_agent_executor = create_react_agent(
    model=llm,
    tools=tools,
    checkpointer=checkpointer,
    state_modifier=system_message,
)


def get_random_thread_id():
    return random.randint(1, 1000000)


def setup_cli():
    cprint(
        figlet_format("Research Agent", font="starwars", width=100, justify="center"),
        attrs=["bold"],
    )
    print("A research assistant powered by LangGraph and LangChain.")
    print("Type 'exit' to quit.\n")


if __name__ == "__main__":
    setup_cli()
    thread_id = get_random_thread_id()

    while True:
        user_input = input("\n> ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        try:
            spinner = Halo(text="Thinking...", spinner="dots")
            for step in langgraph_agent_executor.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config={"configurable": {"thread_id": thread_id}},
            ):
                spinner.start()
                display_step(step, spinner)
        except KeyboardInterrupt:
            print("Process interrupted. Exiting...")
            break
        except Exception as e:
            get_error(e)
