import time
import random
from rich import print
from rich.prompt import Prompt
from rich.console import Console
from rich.panel import Panel
from level4 import level4
from game import clear_screen

console = Console()

def level3():
    console.print("\n[bold magenta]== LEVEL 3 STARTING ==[/bold magenta]")
    time.sleep(0.5)
    console.print("[bold cyan]== BRUTE-FORCING SSH LOGIN ==[/bold cyan]")
    time.sleep(0.5)
    console.print("[bold cyan]Type 'start brute force' to initiate SSH attack[/bold cyan]")
    time.sleep(0.5)

    while True:
        cmd = Prompt.ask("[yellow]>>[/yellow]").strip().lower()
        if cmd == "start brute force":
            
            target_ip = "192.169.1.5"
            console.print(f"[cyan]Target: {target_ip}[/cyan]")
            time.sleep(0.5)

            attempts = [
                ("root", "admin123"),
                ("admin", "toor"),
                ("guest", "guest"),
                ("root", "hunter2")
            ] 

            console.print("[yellow]Attempting login...[/yellow]")
            time.sleep(1)

            for username, password in attempts[:-1]:
                console.print(f"> Trying username: {username}, password: {password} [red]FAILED[/red]")
                time.sleep(0.8)

            success_user, success_pass = attempts[-1]
            console.print(f"> Trying username: {success_user}, password: {success_pass} [bold green]ACCESS GRANTED[/bold green]")
            time.sleep(1)

            console.print("[green]Welcome to the system, Agent_47.[/green]")
            console.print("[cyan]Type 'whoami', 'ls', or 'exit' to interact.[/cyan]")
            console.print("[yellow]Type 'exit' to disconnect and proceed to the next level.[/yellow]")


            while True:
                cmd = Prompt.ask("ssh@target").strip().lower()
                if cmd == "whoami":
                    console.print("[yellow]Agent_47[/yellow]")
                elif cmd == "ls":
                    console.print("documents/  secrets.txt  logs/")
                elif cmd == "exit":
                    console.print(Panel.fit("[bold magenta]Level 3 Complete![/bold magenta]", border_style="green"))
                    console.print("[red]Exiting SSH session...[/red]")
                    time.sleep(3)
                    clear_screen()         
                    level4()               
                    break

                    
                else:
                    console.print("[red]Command not found[/red]")
            break
        else:
            console.print("[red]Unknown command. Type 'start brute force'[/red]")

