import sys
from pathlib import Path
from colorama import Fore, Style, init

# Ініціалізація colorama
init(autoreset=True)

def visualize_directory_structure(directory: Path, indent: str = ""):
    try:
        # Сортуємо файли та папки
        entries = sorted(directory.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
        for entry in entries:
            if entry.is_dir():
                print(f"{indent}{Fore.BLUE}{entry.name}/")
                visualize_directory_structure(entry, indent + "  ")
            else:
                print(f"{indent}{Fore.GREEN}{entry.name}")
    except PermissionError:
        print(f"{Fore.RED}Доступ до директорії {directory} заборонено!")

def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Використання: python hw03.py C:\\Users\\user\\goit-algo-hw-04")
        sys.exit(1)
    
    path = Path(sys.argv[1])
    if not path.exists():
        print(f"{Fore.RED}Шлях {path} не існує.")
        sys.exit(1)
    if not path.is_dir():
        print(f"{Fore.RED}{path} не є директорією.")
        sys.exit(1)
    
    print(f"{Fore.YELLOW}Структура директорії {path}:\n")
    visualize_directory_structure(path)

if __name__ == "__main__":
    main()
