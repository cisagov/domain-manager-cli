"""Domain Manager main script."""
# Third-Party Libraries
from colorama import Fore


def main():
    """Main function."""
    header = """\
     _____                        _         __  __                                   
    |  __ \                      (_)       |  \/  |                                  
    | |  | | ___  _ __ ___   __ _ _ _ __   | \  / | __ _ _ __   __ _  __ _  ___ _ __ 
    | |  | |/ _ \| '_ ` _ \ / _` | | '_ \  | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
    | |__| | (_) | | | | | | (_| | | | | | | |  | | (_| | | | | (_| | (_| |  __/ |   
    |_____/ \___/|_| |_| |_|\__,_|_|_| |_| |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
                                                                      __/ |          
                                                                     |___/           
                    Launch websites and categorize your Domains!
    """

    print(Fore.CYAN + header)


if __name__ == "__main__":
    main()
