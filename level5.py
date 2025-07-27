import time
import os
from rich import print
from rich.prompt import Prompt
from rich.console import Console
from rich.panel import Panel
from level6 import level6
from utils import post_level_menu
from save_system import save_progress

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def level5():
    console.print("\n[bold magenta]== LEVEL 5: HASH CHALLENGE ==[/bold magenta]\n")
    time.sleep(1)

    console.print("[cyan]You've found an encrypted password. Crack it to proceed.[/cyan]")
    time.sleep(0.5)

    original_password = "shadow"
    hash_value = "3bf1114a986ba87ed28fc1b5884fc2f8"

    console.print(f"[yellow]Hash: [bold]{hash_value}[bold][/yellow]")
    console.print("[green]Use an external tool like CrackStation or Hashcat to crack the hash.[/green]\n")
    time.sleep(1)

    guess = Prompt.ask("[bold cyan]Enter the cracked password[/bold cyan]").strip().lower()

    if guess == original_password:
        console.print("[bold green]Correct! You've cracked the hash.[/bold green]")
        save_progress(5)
        time.sleep(3)
        clear_screen() 
        time.sleep(0.5)
        console.print(Panel.fit("[bold magenta]Level 5 Complete![/bold magenta]", border_style="green"))
        time.sleep(0.5)
        post_level_menu(restart_callback=level5, next_level_callback=lambda: (clear_screen(), level6()))
    else:
        console.print("[bold red]Wrong password. Try again later.[/bold red]")