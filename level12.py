import time
import os
from rich import print
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from utils import post_level_menu
from save_system import save_progress

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

console = Console()

def level12():
    console.print("\n[bold magenta]== LEVEL 12: BACKDOOR IMPLANTATION ==[/bold magenta]")
    time.sleep(0.5)
    console.print("[cyan]To maintain access, implant a backdoor on the target system.[/cyan]")
    console.print("[yellow]Type the command: [bold]implant_backdoor --target /bin/secure[/bold][/yellow]")

    while True:
        cmd = Prompt.ask("[green]>>[/green]").strip().lower()
        if cmd == "implant_backdoor --target /bin/secure":
            console.print("\n[bold cyan]Uploading backdoor payload...[/bold cyan]")
            for i in range(0, 101, 20):
                bar = "|" * (i // 10)
                console.print(f"[blue][{bar:<10}][/blue] {i}%")
                time.sleep(0.5)

            console.print("\n[bold green]Backdoor successfully implanted.[/bold green]")    
            time.sleep(0.5)
            console.print("[cyan]Persistence enabled via cronjob entry.[/cyan]")
            save_progress(12)
            time.sleep(3)
            clear_screen()
            time.sleep(0.5)
            console.print(Panel.fit("  [bold green]Remote access secured.[/bold green]\n[bold cyan]Level 12 complete.[/bold cyan]", border_style="magenta"))
            time.sleep(0.5)

            
            def next_level():
                from level13 import level13
                clear_screen()
                level13()

            post_level_menu(restart_callback=level12, next_level_callback=next_level)
            break
        else:
            console.print("[red]Invalid command. Try again.[/red]")