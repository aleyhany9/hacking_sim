from rich import print
from rich.prompt import Prompt

def post_level_menu(restart_callback, next_level_callback):
    print("\n[bold cyan]What do you want to do next?[/bold cyan]")
    print("[yellow]1.[/yellow] Restart Level")
    print("[yellow]2.[/yellow] Continue to Next Level")
    print("[yellow]3.[/yellow] Exit Game")

    while True:
        choice = Prompt.ask("[green]Enter choice (1/2/3)[/green]").strip()
        if choice == "1":
            restart_callback()
            break
        elif choice == "2":
            next_level_callback()
            break
        elif choice == "3":
            print("[red]Exiting game. Goodbye, Agent_47.[/red]")
            exit()
        else:
            print("[red]Invalid choice. Please enter 1, 2, or 3.[/red]")