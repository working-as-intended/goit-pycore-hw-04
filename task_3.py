import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)


def show_directory(folder, level=0):
    for item in sorted(folder.iterdir()):
        indent = "    " * level

        if item.is_dir():
            print(f"{indent}{Fore.CYAN}{item.name}/")
            show_directory(item, level + 1)
        else:
            print(f"{indent}{Fore.GREEN}{item.name}")


if len(sys.argv) != 2:
    print("Вкажіть шлях до директорії.")
else:
    path = Path(sys.argv[1])

    if not path.exists():
        print("Вказаний шлях не існує.")
    elif not path.is_dir():
        print("Вказаний шлях не є директорією.")
    else:
        try:
            print(f"{Fore.CYAN}{path.name}/")
            show_directory(path, 1)
        except OSError as error:
            print(f"Помилка під час читання директорії: {error}")
