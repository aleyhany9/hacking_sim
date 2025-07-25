import time
from rich import print
from rich.prompt import Prompt
from rich.console import Console
from rich.panel import Panel
from level10 import level10
from game import clear_screen

console = Console()

def level9():
    console.print("\n[bold magenta]== LEVEL 9: PASSWORD CRACKING ==[/bold magenta]")
    time.sleep(2)

    console.print("[cyan]We've found a hashed password on the system.[/cyan]")
    time.sleep(1)
    hash = "2ab96390c7dbe3439de74d0c9b0b1767"
    console.print(f"[yellow]MD5 Hash:[/yellow] [bold]{hash}[/bold]\n")
    time.sleep(1)

    console.print("[green]Use the cracking too to break the hash.[/green]")
    console.print("[bold]Example:[/bold] crack_hash -w wordlist.txt -h 2ab96390c7dbe3439de74d0c9b0b1767\n")
    
    while True:
        cmd = Prompt.ask("[bold yellow]>>[/bold yellow]").strip().lower()
        if cmd == f"crack_hash -w wordlist.txt -h {hash}":
            console.print("\n[bold cyan]Launching dictionary attack...[/bold cyan]")
            break
        else:
            console.print("[red]Invalid command. Try again.[/red]")

    time.sleep(1)

    wordlist = ["123456", "password", "admin", "letmein", "hunter2", "root", "qwerty"]
    target_password = "hunter2"

    for word in wordlist:
        console.print(f"Trying: [blue]{word}[/blue]...", end="")
        time.sleep(0.8)
        if word == target_password:
            console.print(" [bold green]MATCH FOUND![/bold green]")
            time.sleep(0.5)
            break
        else:
            console.print(" [red]FAILED[/red]")

    console.print(f"\n[bold green]Password cracked:[/bold green] [bold yellow]{target_password}[/bold yellow]")
    time.sleep(0.7)

    console.print("[cyan]Access granted. Admin credentials unlocked.[/cyan]")      
    time.sleep(0.5)

    console.print(Panel.fit("[bold magenta]Level 9 Complete![/bold magenta]", border_style="cyan"))
    time.sleep(3)
    clear_screen()
    time.sleep(1)
    level10()
    