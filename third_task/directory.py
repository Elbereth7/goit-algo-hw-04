from pathlib import Path
from colorama import Fore, Back, Style

def directory_content(path: Path):

    for element in path.iterdir():
        if element.is_dir():
            description = "This is folder"
            print(Back.MAGENTA + f"{description:^16}" + Back.RESET + Fore.MAGENTA + f" - {element}" + Style.RESET_ALL)
            directory_content(element)
        elif element.is_file():
            description = "This is file"
            print(Back.CYAN + f"{description:^16}" + Back.RESET + Fore.CYAN + f" - {element.name}"+ Style.RESET_ALL)

