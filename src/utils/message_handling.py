"""Return messages handler."""
# Third-Party Libraries
from colorama import Fore


def success_msg(text):
    """Success message."""
    print(Fore.LIGHTGREEN_EX + text + Fore.WHITE)


def error_msg(text):
    """Error message."""
    print(Fore.LIGHTRED_EX + text + Fore.WHITE)


def unknown_command():
    """Unknown command response."""
    print("Sorry we didn't understand that command.")
