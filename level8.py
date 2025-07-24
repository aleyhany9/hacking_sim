import time
from rich import print
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()

def level8():
    console.print("\n[bold magenta]== LEVEL 8: DATA EXFILTRATION ==[/bold magenta]")
    time.sleep(1)

    console.print("[cyan]You've gained root access. It's time to exfiltrate the target data.[/cyan]")
    time.sleep(1)

    console.print("[yellow]Available sensitive files:[/yellow]")
    time.sleep(0.5)
    files = ["flag.txt", "database.db", "emails.mbox", "passwd.bak"]

    for file in files:
        console.print(f"[green]> {file}[/green]")
        time.sleep(0.3)

    console.print("\n[cyan]Type the correct exfiltration command (e.g., 'exfil flag.txt' or 'scp flag.txt')[/cyan]")

    while True:
        cmd = Prompt.ask("root@target").strip().lower()

        if cmd in ["exfil flag.txt", "scp flag.txt"]: 
            console.print("\n[bold cyan]Exfiltrating 'flag.txt'...[/bold cyan]")
            for i in range(0, 101, 20):  
                bar = "|" * (i // 10)         
                console.print(f"[blue][{bar:<10}][/blue] {i}%")
                time.sleep(0.5)
            time.sleep(1)    
            console.print("\n[bold green]Data exfiltration complete! Mission accomplished.[/bold green]")  
            time.sleep(1)
            console.print(Panel.fit("[bold magenta]Level 8 Complete![/bold magenta]", border_style="cyan"))
            break
        elif cmd.startswith("exfil") or cmd.startswith("scp"):
            console.print("[red]Access denied or wrong file. Try again with 'flag.txt'.[/red]")
        else:
            console.print("[red]Unknown command. Use 'exfil flag.txt' or 'scp flag.txt'[/red]")