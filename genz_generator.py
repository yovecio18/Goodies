import sqlite3
import random
import time
import sys
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.align import Align
from rich import print as rprint

console = Console()

# -------------------------------------------------------------------
# Data Sources
# -------------------------------------------------------------------
BASE_SLANG = [
    ("Skibidi", "Chaotic absurd funny word.", "Bro play was skibidi.", "Gen Alpha"),
    ("Rizz", "Ability to charm people.", "He has unspoken rizz.", "Gen Z / Alpha"),
    ("Fanum Tax", "Stealing food from friends.", "Gimme fries, Fanum tax.", "Gen Alpha"),
    ("Gyatt", "Reaction to fine person.", "Gyatt look at that.", "Gen Z / Alpha"),
    ("Sigma", "Independent lone wolf person.", "Grinding daily, real sigma.", "Gen Z / Alpha"),
    ("Mewing", "Resting tongue defines jaw.", "Can not talk, mewing.", "Gen Z / Alpha"),
    ("Mogging", "Outshining everyone in looks.", "Bro walked in mogging.", "Gen Alpha"),
    ("Looksmaxxing", "Maximizing physical looks.", "He is looksmaxxing now.", "Gen Z / Alpha"),
    ("Aura", "Cool social status points.", "Bro lost ten aura.", "Gen Alpha"),
    ("Cooked", "Doomed or severe trouble.", "Did not study, cooked.", "Gen Z / Alpha"),
    ("Crash Out", "Completely lose your mind.", "He decided to crash.", "Gen Z / Alpha"),
    ("6-7", "Viral hand gesture meme.", "Bro said six seven.", "Gen Alpha"),
    ("Glazing", "Over praising someone annoyingly.", "Stop glazing him blud.", "Gen Z / Alpha"),
    ("Ohio", "Wild chaotic cursed event.", "Only in Ohio bruh.", "Gen Z / Alpha"),
    ("Delulu", "Holding delusional high hopes.", "She is totally delulu.", "Gen Z / Alpha"),
    ("Yap", "Talking endlessly about nothing.", "Bro keeps yapping daily.", "Gen Z / Alpha"),
    ("Locked In", "Absolute intense focus.", "Time to get locked.", "Gen Z / Alpha")
]

LOGICAL_SUBJECTS = ["Bro", "Blud", "Shmlawg", "Unc", "Local NPC", "My opp", "The sigma"]
LOGICAL_ACTIONS = [
    "started mewing today.",
    "is aura farming.",
    "decided to crash.",
    "got cooked instantly.",
    "is yapping loudly.",
    "lost ten aura.",
    "paid Fanum Tax.",
    "went full delulu."
]

UNHINGED_SUBJECTS = ["Skibidi blud", "Baby Gronk", "Unc", "Shmlawg", "Diddyblud", "GigaChad", "Local opp"]
UNHINGED_MID = ["mewed at", "mogged", "fanum-taxed", "lore-dumped", "glazed", "rizzled", "looksmaxxed"]
UNHINGED_END = ["Kai Cenat.", "Ohio.", "Grimace.", "Waffle House.", "6-7 gesture.", "Livvy Dunne."]

UNHINGED_SHORT_PHRASES = [
    "lost -99k aura fast.",
    "got instant cooked, bro.",
    "is totally delulu now.",
    "went full crash out.",
    "got labeled chopped, bruh."
]

# -------------------------------------------------------------------
# Sentence Generators
# -------------------------------------------------------------------
def generate_logical_sentence():
    sub = random.choice(LOGICAL_SUBJECTS)
    act = random.choice(LOGICAL_ACTIONS)
    return f"{sub} {act}"

def generate_unhinged_sentence():
    if random.choice([True, False]):
        sub = random.choice(UNHINGED_SUBJECTS)
        verb = random.choice(UNHINGED_MID)
        target = random.choice(UNHINGED_END)
        sentence = f"{sub} {verb} {target}"
    else:
        sub = random.choice(UNHINGED_SUBJECTS)
        phrase = random.choice(UNHINGED_SHORT_PHRASES)
        sentence = f"{sub} {phrase}"

    words = sentence.split()
    if len(words) > 5:
        sentence = " ".join(words[:5]) + "."
        
    return sentence

def generate_dataset(mode="logical"):
    data = list(BASE_SLANG)
    index = 1
    while len(data) < 1000:
        term_name = f"Brainrot #{index}"
        cohort = random.choice(["Gen Alpha", "Gen Z / Alpha"])
        
        if mode == "logical":
            meaning = "Standard slang usage example."
            example = generate_logical_sentence()
        else:
            meaning = "Maximum absurdity short sequence."
            example = generate_unhinged_sentence()
            
        data.append((term_name, meaning, example, cohort))
        index += 1
    return data

# -------------------------------------------------------------------
# DB Engine
# -------------------------------------------------------------------
def setup_database(mode="logical"):
    conn = sqlite3.connect("brainrot_dual_short.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS brainrot")
    cursor.execute('''
        CREATE TABLE brainrot (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            term TEXT NOT NULL,
            definition TEXT NOT NULL,
            example TEXT NOT NULL,
            cohort TEXT NOT NULL
        )
    ''')
    dataset = generate_dataset(mode)
    cursor.executemany('''
        INSERT INTO brainrot (term, definition, example, cohort)
        VALUES (?, ?, ?, ?)
    ''', dataset)
    conn.commit()
    conn.close()

def get_random_brainrot():
    conn = sqlite3.connect("brainrot_dual_short.db")
    cursor = conn.cursor()
    cursor.execute("SELECT term, definition, example, cohort FROM brainrot ORDER BY RANDOM() LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    return row

def get_total_count():
    conn = sqlite3.connect("brainrot_dual_short.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM brainrot")
    count = cursor.fetchone()[0]
    conn.close()
    return count

# -------------------------------------------------------------------
# UI Engine
# -------------------------------------------------------------------
def print_header(mode):
    mode_label = "🧠 LOGICAL MODE" if mode == "logical" else "💀 UNHINGED MODE (4-5 WORDS)"
    color = "bright_cyan" if mode == "logical" else "bright_magenta"
    
    header_text = Text(f"🔥 BRAINROT TERMINAL 🔥\n", style="bold magenta")
    subtitle_text = Text(f"[{mode_label}]", style=f"bold {color}")
    panel = Panel(Align.center(header_text + subtitle_text), border_style=color, width=50)
    console.print(panel)

def display_entry(data, mode):
    term, definition, example, cohort = data
    border_col = "bright_cyan" if mode == "logical" else "bright_yellow"
    
    body = Text()
    body.append("🔥 TERM: ", style="bold bright_yellow")
    body.append(f"{term.upper()}\n", style="bold bright_cyan")
    
    body.append("💡 MEANING: ", style="bold bright_yellow")
    body.append(f"{definition}\n", style="white")
    
    body.append("🗣️ EXAMPLE: ", style="bold bright_yellow")
    body.append(f"\"{example}\"\n", style="bold italic bright_green")
    
    body.append("👥 COHORT: ", style="bold bright_yellow")
    body.append(f"{cohort}", style="magenta")

    panel = Panel(body, title="[bold magenta]💀 BRAIN ROT 💀[/bold magenta]", border_style=border_col, width=50)
    console.print(panel)

def display_word_of_the_day_and_exit():
    """Displays Word of the Day and terminates app immediately."""
    console.clear()
    data = random.choice(BASE_SLANG)
    term, definition, example, cohort = data
    
    body = Text()
    body.append("🌟 WORD OF THE DAY 🌟\n\n", style="bold bright_green")
    body.append("🔥 TERM: ", style="bold bright_yellow")
    body.append(f"{term.upper()}\n", style="bold bright_cyan")
    
    body.append("💡 MEANING: ", style="bold bright_yellow")
    body.append(f"{definition}\n", style="white")
    
    body.append("🗣️ EXAMPLE: ", style="bold bright_yellow")
    body.append(f"\"{example}\"\n", style="bold italic bright_green")
    
    body.append("👥 COHORT: ", style="bold bright_yellow")
    body.append(f"{cohort}", style="magenta")

    panel = Panel(body, title="[bold bright_green]⚡ DAILY BRAINROT ⚡[/bold bright_green]", border_style="bright_green", width=50)
    console.print(panel)
    rprint("\n[bold magenta]Daily dose acquired! Go touch grass! 👋💀[/bold magenta]\n")
    sys.exit(0)

def main():
    console.clear()
    
    rprint("[bold magenta]SELECT INITIAL MODE:[/bold magenta]")
    rprint(" [1] 🧠 Logical Mode (Standard slang)")
    rprint(" [2] 💀 Unhinged Mode (Max 4-5 words)")
    rprint(" [3] 🌟 Word of the Day (Quick view & exit)")
    
    init_choice = Prompt.ask("\nChoice", choices=["1", "2", "3"], default="1")
    
    if init_choice == "3":
        display_word_of_the_day_and_exit()
        
    current_mode = "logical" if init_choice == "1" else "unhinged"
    setup_database(current_mode)
    
    while True:
        console.clear()
        print_header(current_mode)
        rprint(f"[bold bright_green]Entries loaded:[/bold bright_green] [bold yellow]{get_total_count()}[/bold yellow]\n")
        
        rprint("[bold magenta]SELECT OPTION:[/bold magenta]")
        rprint(" [1] 🎲 Fetch Random Slang")
        rprint(f" [2] 🔄 Switch Mode (Current: {current_mode.upper()})")
        rprint(" [3] 🌟 Word of the Day & Exit")
        rprint(" [4] ❌ Exit App")
        
        choice = Prompt.ask("\nChoice", choices=["1", "2", "3", "4"], default="1")
        
        if choice == "1":
            time.sleep(0.05)
            data = get_random_brainrot()
            if data:
                display_entry(data, current_mode)
            Prompt.ask("\nPress [enter] to continue")
            
        elif choice == "2":
            current_mode = "unhinged" if current_mode == "logical" else "logical"
            rprint(f"\n[bold yellow]Rebuilding database for {current_mode.upper()} mode...[/bold yellow]")
            setup_database(current_mode)
            time.sleep(0.3)
            
        elif choice == "3":
            display_word_of_the_day_and_exit()
            
        elif choice == "4":
            rprint("\n[bold magenta]Go touch grass! 👋💀[/bold magenta]\n")
            break

if __name__ == "__main__":
    main()
