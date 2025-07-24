import time
from rich import print
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from level7 import level7
from game import clear_screen

console = Console()

def level6():
    console.print("\n[bold magenta]== LEVEL 6: VULNERABILITY SCAN ==[/bold magenta]")
    time.sleep(0.5)
    console.print("[cyan]Type 'start scanning' to begin scanning the target system...[/cyan]")

    while True:
        cmd = Prompt.ask("[yellow]>>[/yellow]").strip().lower()
        if cmd == "start scanning":
            console.print("\n[bold cyan]Scanning target for vulnerabilities...[/bold cyan]")
            for i in range(0, 101, 25):
                bar = "|" * (i // 5)
                console.print(f"[blue][{bar:<20}][/blue] {i}%")
                time.sleep(1)

            console.print("\n[bold green]Scan complete. Vulnerabilities found:[/bold green]")
            vulns = [
                ("CVE-2021-3156", "sudo heap overflow"),
                ("CVE-2020-1472", "ZeroLogon"),
                ("CVE-2019-0708", "BlueKeep"),
                ("CVE-2023-23397", "Outlook Privilege Escalation")
            ]
            for v in vulns:
                console.print(f"[red]> {v}[/red]")
            break
        else:
            console.print("[red]Unkown command. Type 'start scanning'[/red]")  
    
    console.print("\n[cyan]Select a CVE to exploit (e.g., CVE-2023-23397)[/cyan]")
    while True:
        choice = Prompt.ask("exploit>").strip().upper()
        if choice == "CVE-2023-23397":
            time.sleep(0.5)
            console.print("\n[bold green]Exploiting...[/bold green]")
            time.sleep(1.5)
            console.print("[bold cyan]Exploit succesful! Admin shell access granted.[/bold cyan]")
            console.print(Panel.fit("[bold magenta]Level 6 Complete![/bold magenta]", border_style="green"))
            time.sleep(3)
            clear_screen() 
            time.sleep(1)
            level7()
            break
        elif any(choice == cve for cve, _ in vulns):
            console.print("[red]Exploit failed. No effect on target.[/red]")
        else:
            console.print("[red]Invalid CVE ID. Try again.[/red]")