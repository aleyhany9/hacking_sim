import time
import base64
import json
import os 
import random

from rich import print
from rich.prompt import Prompt
from rich.panel import Panel
from rich.console import Console
from level1 import level1
from save_system import save_progress, load_progress, clear_save
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
from menus import level_selection_menu

console = Console()

def slow_print_rich(text, delay=0.03):
    clean_text = (
        text.replace("[green]", "")
            .replace("[/green]", "")
            .replace("[cyan]", "")
            .replace("[/cyan]", "")
            .replace("[bold]", "")
            .replace("[/bold]", "")
            .replace("[bold green]", "")
            .replace("[/bold green]", "")
    )

    for char in clean_text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def boot_screen():
    console.print("[bold green]+-------------------------------------+[/bold green]")
    console.print("[bold green]|        HACKNET v1.0 INITIALIZING    |[/bold green]")
    console.print("[bold green]+-------------------------------------+[/bold green]\n")



    stages = [
        "Bypassing firewall...",
        "Spoofing MAC address...",
        "Injecting payload...",
        "ACCESS GRANTED\n"
    ]
    for stage in stages:
        slow_print_rich(f"[green]{stage}[/green]", 0.05)
        time.sleep(0.3)

    console.print("[cyan]Welcome, Agent_47.[/cyan]")
    console.print("Type [yellow]help[/yellow] to see the available commands.\n")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def start_game():
    console.print("[bold cyan]Starting new game...[/bold cyan]")
    time.sleep(1)
    console.print("\n[bold magenta]== LEVEL 1 STARTING ==[/bold magenta]")
    level1()


def main_menu():


    try:
        while True:
            command = Prompt.ask(">>").strip().lower()

            if command == "help":
                console.print("[yellow]Available commands:[/yellow] start, levels, help, exit")
            elif command == "start":
                clear_screen()
                start_game()
            elif command == "exit":
                console.print("[red]Exiting hacking sim...[/red]")
                break
            elif command == "levels":
                level_selection_menu()
            else:
                console.print("[red]Unknown command. Type 'help'[/red]")
    except KeyboardInterrupt:
        console.print("\n[bold red]User exited with ctrl+c.[/bold red]")


if __name__ == "__main__":
    try:
        boot_screen()
        main_menu()
    except KeyboardInterrupt:
        console.print("\n[bold red]User exited during startup.[/bold red]")    

