import time
from rich import print
from rich.prompt import Prompt
from rich.console import Console
from level6 import level6

console = Console()

def level5():
    console.print("\n[bold magenta]== LEVEL 5: HASH CHALLENGE ==[/bold magenta]\n")
    time.sleep(0.5)

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
        console.print("[cyan]Level 5 Complete! Get ready for the next mession..[/cyan]\n")
        time.sleep(1)
        level6()
    else:
        console.print("[bold red]Wrong password. Try again later.[/bold red]")