import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from datetime import datetime
from colorama import Fore, Style
from dateutil import tz

console = Console(force_terminal=True)


def set_color(text, color):
    return f"{color}{text}{Style.RESET_ALL}"


def display_step(step, spinner):
    """Display a step dynamically based on its type."""
    if isinstance(step, dict):
        if "agent" in step:
            agent_messages = step["agent"].get("messages", [])
            for message in agent_messages:
                if hasattr(message, "content"):
                    if message.content is None:
                        continue
                    content = message.content or "[No content]"
                    metadata = getattr(message, "response_metadata", {})
                    model = metadata.get("model", "Unknown Model")
                    created_at = format_timestamp(
                        metadata.get("created_at", "Unknown Time")
                    )
                    if content != "[No content]":
                        spinner.stop()
                        console.print(
                            Panel(
                                Text(
                                    f"\n{content}\n\n"
                                    f"{set_color('Model:', Fore.BLUE)} {model}\n"
                                    f"{set_color('Timestamp:', Fore.BLUE)} {created_at}",
                                    style="white",
                                ),
                                title="Agent Message",
                                border_style="green",
                            )
                        )
        elif "tools" in step:
            tool_messages = step["tools"].get("messages", [])
            for tool_message in tool_messages:
                tool_name = getattr(tool_message, "name", "Unknown Tool")
                content = getattr(tool_message, "content", "[No content]")
                spinner.stop()
                console.print(
                    Panel(
                        Text(
                            f"{set_color('Tool Used:', Fore.YELLOW)} {tool_name}\n\n"
                            f"{set_color('Output:', Fore.YELLOW)} {content}",
                            style="white",
                        ),
                        title="Tool Output",
                        border_style="yellow",
                    )
                )
                spinner.start()
        else:
            spinner.stop()
            console.print(
                Panel(
                    Text(f"Unknown step structure:\n{step}", style="red"),
                    title="Unknown Step",
                    border_style="red",
                )
            )
            spinner.start()
    else:
        spinner.stop()
        console.print(
            Panel(
                Text(f"Unexpected step type: {step}", style="bold red"),
                title="Error",
                border_style="red",
            )
        )
        spinner.start()


def format_timestamp(timestamp):
    try:

        dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        dt = dt.astimezone(tz.tzlocal())
        return dt.strftime("%B %d, %Y, %I:%M %p %Z")
    except ValueError:
        return timestamp


def get_random_thread_id():
    return random.randint(1, 1000000)


def get_error(e):
    console.print(
        Panel(
            Text(f"An error occurred: {str(e)}", style="bold red"),
            title="Error",
        )
    )
