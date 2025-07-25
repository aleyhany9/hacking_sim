import time
from rich import print
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()

def level13():
    console.print("\n[bold magenta]== LEVEL 13: LOG CLEANING ==[/bold magenta]")
    time.sleep(0.5)
    console.print("[cyan]To avoid detection, remove traces from system logs.[/cyan]")
    time.sleep(0.5)
    console.print("[yellow]Use the command: [bold]clear_logs --force[/bold][/yellow]")

    while True:
        cmd = Prompt.ask("[green]>>[/green]").strip().lower()
        if cmd == "clear_logs --force":
            console.print("\n[bold cyan]Wiping logs...[/bold cyan]")
            logs = [
                "/var/log/auth.log",
                "/var/log/syslog",
                "/home/user/.bash_history",
                "/var/log/apache2/access.log"
            ]
            for log in logs:
                console.print(f"[red]- {log} [green]CLEARED[/green]")
                time.sleep(0.6)

            console.print("\n[bold green]All logs cleared successfully.[/bold green]")    
            time.sleep(0.5)
            console.print("[cyan]System appears clean. No traces left behind.[/cyan]")
            time.sleep(0.5)
            console.print(Panel.fit("[bold green]Tracks covered.[/bold green]\n[bold cyan]Level 13 complete.[/bold cyan]", border_style="magenta"))
            break
        else:
            console.print("[red]Invalid command. Try again.[/red]")