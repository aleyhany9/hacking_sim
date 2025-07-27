def level1():
    from random import choice, sample
    from rich import print
    from rich.console import Console
    from rich.prompt import Prompt
    from rich.panel import Panel
    import time
    from level2 import level2
    from game import clear_screen
    from utils import post_level_menu

    console = Console()

    word_list = [
        "control", "hacking", "network", "access", "system",
        "virus", "malware","secure", "capture", "breach",
        "packets", "command", "target", "firewall"
    ]

    possible_words = [w.upper() for w in sample(word_list, 8)]
    correct_password = choice(possible_words)

    print("[bold cyan]\n==ACCESSING PASSWORD DATABASE... ==[/bold cyan]")
    time.sleep(1)
    print("[yellow]Possible passwords:[/yellow]\n")

    for word in possible_words:
       print(f">{word}") 

    attempts = 4

    while attempts > 0:
        guess = Prompt.ask("\n[green]Enter password guess[/green]").strip().upper()

        if guess not in possible_words:
            print("[red]Invalid word. Try one from the list above.[/red]")
            continue
    
        match_count = sum(1 for a, b in zip(guess, correct_password)if a == b)

        if guess == correct_password:
            print("[bold green]\nACCESS GRANTED[/bold green]")
            time.sleep(3)
            clear_screen()
            console.print(Panel.fit("[bold magenta]Level 1 Complete![/bold magenta]", border_style="green"))
            time.sleep(0.5)
            post_level_menu(restart_callback=level1, next_level_callback=lambda: (clear_screen(), level2()))
            break
        else:
            attempts -= 1
            print(f"[yellow]{match_count}/7 letters correct[/yellow]")
            print(f"[red]{attempts} attempts left[/red]")

        if attempts == 0:
            print(f"[bold red]\nACCESS DENIED[/bold red]")
            print(f"[cyan]The correct password was: [bold]{correct_password}[/bold][/cyan]")
