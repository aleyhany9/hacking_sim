import time
from rich import print
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from game import clear_screen
from level12 import level12
from utils import post_level_menu

console = Console()

def level11():
    console.print("\n[bold magenta]== LEVEL 11: PACKET ANALYSIS ==[/bold magenta]")
    time.sleep(0.5)
    console.print("[cyan]Type 'analyze packet capture' to begin.[/cyan]")

    while True:
        cmd = Prompt.ask("[yellow]>>[/yellow]").strip().lower()
        if cmd == "analyze packet capture":
            console.print("\n[bold cyan]Opening packet dump...[/bold cyan]")
            time.sleep(1)

            packet_dump = """
[Packet 17]
Source IP: 10.0.2.15
Destination IP: 192.168.1.5
Protocol: TCP
Payload: GET /login.php HTTP/1.1

[Packet 18]
Source IP: 10.0.2.15
Destination IP: 192.168.1.5
Protocol: TCP
Payload: username=admin&password=shadow123

[Packet 19]
Source IP: 192.168.1.5
Destination IP: 10.0.2.15
Protocol: HTTP 200 OK
Payload: Login success. SessionID=ASD13213
"""
            console.print(Panel(packet_dump.strip(), title="[bold red]CAPTURED TRAFFIC[/bold red]", subtitle="Analyze the data"))
            time.sleep(1)
            console.print("\n[green]Question:[/green] What was the password used to log in?")

            answer = Prompt.ask("Password>").strip()
            if answer == "shadow123":
                console.print("[bold green]Correct! Packet analysis successful.[/bold green]")
                time.sleep(3)
                clear_screen()
                time.sleep(0.5)
                console.print(Panel.fit("[bold magenta]Level 11 Complete![/bold magenta]", border_style="cyan"))
                time.sleep(0.5)
                post_level_menu(restart_callback=level11, next_level_callback=lambda: (clear_screen(), level12()))
                break
            else:
                console.print("[red]Incorrect. Try again.[/red]")
        else:
            console.print("[red]Unknown command. Type 'analyze packet capture'[/red]")