from rich.console import Console
from rich.prompt import Prompt

import os
from save_system import load_progress

from level1 import level1
from level2 import level2
from level3 import level3
from level4 import level4
from level5 import level5
from level6 import level6
from level7 import level7
from level8 import level8
from level9 import level9
from level10 import level10
from level11 import level11
from level12 import level12
from level13 import level13
from level14 import level14

console = Console()

def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

def level_selection_menu():
    progress = load_progress()
    if not progress:
        console.print("[red]No saved progress found. Complete some levels first.[/red]")
        return
    
    console.print("\n[bold magenta]== LEVEL SELECTION MENU ==[/bold magenta]")
    for i in range(1, progress + 1):
        console.print(f"[cyan]{i}. Level {i}[/cyan]")

    choice = Prompt.ask("Enter level number to play or 'exit' to return").strip().lower()
    if choice == "exit":
        return
    
    try:
        level_num = int(choice)
        if 1 <= level_num <= progress:
            level_map = {
                1: level1,
                2: level2,
                3: level3,
                4: level4,
                5: level5,
                6: level6,
                7: level7,
                8: level8,
                9: level9,
                10: level10,
                11: level11,
                12: level12,
                13: level13,
                14: level14,
            }
            clear_screen()
            level_map[level_num]()
        else:
            console.print("[red]Invalid level number.[/red]")
    except ValueError:
        console.print("[red]Invalid input. Enter a number or 'exit'.[/red]")