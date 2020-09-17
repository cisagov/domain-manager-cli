"""Run commands."""
# Standard Python Libraries
import sys

# Third-Party Libraries
from colorama import Fore
from utils.switch import Switch


def run():
    """Run application."""
    while True:
        show_commands()
        action = input(Fore.WHITE + "What action would you like to take? ")

        with Switch(action) as s:
            s.case(["x", "bye", "exit", "exit()"], exit_app)
            s.default(unknown_command)


def show_commands():
    """Show available commands."""
    print(
        Fore.LIGHTYELLOW_EX
        + """
View available [D]omains
View available S3 [W]ebsites
e[X]it

    """
    )


def exit_app():
    """Exit application."""
    print()
    print(Fore.RED + "Bye")
    return sys.exit()


def unknown_command():
    """Unknown command response."""
    print("Sorry we didn't understand that command.")
