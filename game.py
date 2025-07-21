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
        "Bypasing firewall...",
        "Spoofing MAC address...",
        "Injecting payload...",
        "ACCESS GRANTED\n"
    ]
    for stage in stages:
        slow_print_rich(f"[green]{stage}[/green]", 0.05)
        time.sleep(0.3)

    console.print("[cyan]Welcome, Agent_47.[/cyan]")
    console.print("Type [yellow]help[/yellow] to see the available commands.\n")


def start_game():
    console.print("[bold cyan]Starting new game...[/bold cyan]")
    time.sleep(0.3)
    console.print("\n[bold magenta]== LEVEL 1 STARTING ==[/bold magenta]")
    level1()


def main_menu():
    try:
        while True:
            command = Prompt.ask(">>").strip().lower()


            if command == "help":
                console.print("[yellow]Available commands:[/yellow] start, help, exit")
            elif command == "start":
                start_game()
            elif command == "exit":
                console.print("[red]Exiting hacking sim...[/red]")
                break
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