"""Run commands."""
# Standard Python Libraries
import sys

# Third-Party Libraries
from colorama import Fore
from scripts.active_sites import delete_live_site, launch_live_site
from scripts.get_data import (
    get_application_list,
    get_domain_list,
    get_live_site_list,
    get_website_content_list,
)
from utils.message_handling import unknown_command
from utils.switch import Switch


def run():
    """Run application."""
    while True:
        show_commands()
        action = input(Fore.WHITE + "What action would you like to take? ")

        with Switch(action) as s:
            s.case("d", get_domain_list)
            s.case("w", get_website_content_list)
            s.case("a", get_application_list)
            s.case("s", get_live_site_list)
            s.case("l", launch_live_site)
            s.case("c", print("site categorized"))
            s.case("e", delete_live_site)
            s.case(["x", "bye", "exit", "exit()"], exit_app)
            s.default(unknown_command)


def show_commands():
    """Show available commands."""
    print(
        Fore.LIGHTYELLOW_EX
        + """
View available [D]omains
View available S3 [W]ebsites
View available [A]pplications
View [S]ites that are currently live
[L]aunch a new site
[C]ategorize an existing site
Delete an [E]xisting site
e[X]it

    """
    )


def exit_app():
    """Exit application."""
    print()
    print(Fore.RED + "Bye")
    return sys.exit()
