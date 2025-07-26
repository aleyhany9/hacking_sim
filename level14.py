import time
from rich import print
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()

def level14():
    console.print("\n[bold magenta]== LEVEL 14: FINAL DECRYPTION ==[/bold magenta]")
    time.sleep(1)
    console.print("[cyan]You've found the final encrypted file: [bold]final_file.enc[/bold][/cyan]")
    console.print("[cyan]Use your decryption skills to unlock the truth...[/cyan]\n")

    while True:
        command = Prompt.ask("[green]>>[/green]").strip().lower()
        if command == "decrypt final_file.enc":
            console.print("[bold cyan]Decrypting...[/bold cyan]")
            for i in range(0, 101, 25):
                bar = "|" * (i // 5)
                console.print(f"[blue][{bar:<20}][/blue] {i}%")
                time.sleep(0.6)
            console.print("\n[bold yellow]Enter master passphrase to complete decryption:[/bold yellow]")
            password = Prompt.ask("[red]Passphrase[/red]").strip() 
            if password == "omegaoverride":
                console.print("\n[bold green]Decryption successful![/bold green]")
                console.print(Panel.fit("[cyan]MISSION COMPLETE[/cyan]\n[bold magenta]You've completed the HACKING simulation![/bold magenta]", border_style="green"))
                break
            else:
                console.print("[red]Wrong passphrase. Try again.[/red]")
        else:
            console.print("[red]Unknown command. Try: decrypt final_file.enc[/red]")