import time
import os
from rich import print
from rich.prompt import Prompt
from rich.panel import Panel
from rich.console import Console
from level8 import level8
from utils import post_level_menu
from save_system import save_progress

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def level7():
    console.print("\n[bold magenta]== LEVEL 7: PRIVILEGE ESCALATION ==[/bold magenta]")
    time.sleep(1)
    console.print("[cyan]You have limited shell access. Try to escalate privileges to root.[/cyan]")
    time.sleep(1)

    console.print("\n[yellow]Try running 'sudo -l' to check for allowed sudo commands.[/yellow]")
    while True:
        cmd = Prompt.ask("user@target").strip().lower()
        if cmd == "sudo -l":
            console.print("\n[green]Matching Defaults entries for user on target:[/green]")
            time.sleep(1)
            console.print("[green]User may run the following commands on target:[/green]")
            time.sleep(1)
            console.print("[bold cyan](ALL) NOPASSWD: /opt/rootme[/bold cyan]")
            time.sleep(1)
            break
        else:
            console.print("[red]UnKmowm command, Try 'sudo -l' [/red]")

    console.print("\n[cyan]Looks like you can run /opt/rootme as root![/cyan]")
    console.print("[yellow]Try executing it...[/yellow]")

    while True:
            cmd = Prompt.ask("user@target").strip().lower()
            if cmd in ["./opt/rootme", "sudo /opt/rootme"]:
                console.print("\n[bold green]Privilege escalated to root![/bold green]")
                console.print("[cyan]You now have full control over the system.[/cyan]")
                save_progress(7)
                time.sleep(3)
                clear_screen()
                time.sleep(0.5)
                console.print(Panel.fit("[bold magenta]Level 7 Complete![/bold magenta]", border_style="green"))
                time.sleep(0.5)
                post_level_menu(restart_callback=level7, next_level_callback=lambda: (clear_screen(), level8()))
                break
            else:
                console.print("[red]Access denied or command not recognized. Try again.[/red]")