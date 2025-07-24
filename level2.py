import time 
import random
import os 
import base64
import json


from rich import print
from rich.prompt import Prompt
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
from level3 import level3
from game import clear_screen

console = Console()

def level2():
    console.print("\n[bold magenta]== LEVEL 2 STARTING ==[/bold magenta]")
    console.print("[bold cyan]== INITIATING NETWORK SCAN ==[/bold cyan]")
    target_ip = Prompt.ask("[green]Enter target IP[/green]", default="192.169.1.5")

    console.print(f"[yellow]Scanning ports on {target_ip}...[/yellow]")
    for i in range(0, 101, 20):
        bar = "|" * (i // 5)
        console.print(f"[blue][{bar:<20}][/blue] {i}%")
        time.sleep(1)
    time.sleep(2)    
    clear_screen()

    table = Table(title="Scan Results")

    table.add_column("Port", style="cyan", justify="center")
    table.add_column("Service", style="magenta", justify="center")
    table.add_column("Status", style="green", justify="center")

    fake_ports = [
        ("22", "SSH", "Open"),
        ("80", "HTTP", "Open"),
        ("443", "HTTPS", "Closed"),
        ("3306", "MYSQL", "Open")
    ]

    for port, service, status in fake_ports:
        table.add_row(port, service, status)

    console.print(table)  

    while True:
        choice = Prompt.ask("[bold green]Connect to a port (e.g., '22' or 'ssh') or type 'back'[/bold green]").strip().lower()
        if choice in ("22", "ssh"):
            console.print("[bold green]Connection to SSH...[/bold green]")
            time.sleep(1)
            console.print("[cyan]SSH banner: Ubuntu 20.04 OpenSSH 7.9p1[/cyan]")
            console.print("[bold yellow]Login required...[/bold yellow]")
            break
        elif choice == "back":
            console.print("[bold red]Returning to menu...[/bold red]")
            break
        else:
            console.print("[red]Connection refused or port closed.[/red]")

    console.print("\n[bold cyan]Establishing secure channel...[/bold cyan]")
    for i in range(0, 101, 20):
        bar = "|" * (i // 5)
        console.print(f"[blue][{bar:<20}][/blue] {i}%")
        time.sleep(0.3)
    console.print("[green]\nConnection stable. Proceeding...[/green]") 
    console.print(Panel.fit("[bold magenta]Level 2 Complete![/bold magenta]", border_style="green"))
    time.sleep(3)
    clear_screen()   
    time.sleep(1)
    level3()   