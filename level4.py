import time
import os
from rich import print
from rich.prompt import Prompt
from rich.console import Console
from rich.panel import Panel
from level5 import level5
from utils import post_level_menu
from save_system import save_progress

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def level4():
    console.print("\n[bold magenta]== LEVEL 4: FILE EXTRACTION ==[/bold magenta]")
    time.sleep(1)

    console.print("[cyan]Listing available files on remote machine...[/cyan]")
    time.sleep(1)

    files = ["secrets.txt", "data_dump.db", "flag.enc", "readme.md"]
    for f in files:
        console.print(f"[green]> {f}[/green]")
        time.sleep(0.3)

    console.print("\n[yellow]Which file do you want to extract?[/yellow]")
    selected = Prompt.ask("[bold green]Enter filename[/bold green]").strip()

    if selected not in files:
        console.print("[red]File not found or access denied.[/red]")
        return

    console.print(f"\n[bold cyan]Extracting '{selected}'...[/bold cyan]")
    for i in range(0, 101, 25):
        bar = "|" * (i // 10)
        console.print(f"[blue][{bar:<10}][/blue] {i}%")
        time.sleep(0.3)
    console.print(f"\n[bold green]{selected} successfully extracted![/bold green]")
    time.sleep(0.5)

    save_progress(4)
    time.sleep(3)
    clear_screen()
    time.sleep(0.5)
    console.print(Panel.fit("[bold magenta]Level 4 Complete![/bold magenta]", border_style="green")) 
    time.sleep(0.5)
    post_level_menu(restart_callback=level4, next_level_callback=lambda: (clear_screen(), level5()))