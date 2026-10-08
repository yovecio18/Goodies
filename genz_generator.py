import random
import sys
import time
import argparse
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.align import Align
from rich import print as rprint

console = Console()

# =====================================================================
# MASSIVE 2025/2026 GEN Z & GEN ALPHA BRAINROT LEXICON
# =====================================================================
LEXICON = {
    "subjects": [
        "Bro", "Blud", "Shmlawg", "Unc", "Local NPC", "My opp", "The sigma",
        "Baby Gronk", "Kai Cenat", "Livvy Dunne", "John Pork", "Diddyblud",
        "The Rizzler", "The Glazer", "Aura-less blud", "Shadow wizard",
        "Goofy ahh NPC", "Mewing champion", "Gassy shlawg", "Looksmaxxer",
        "Skibidi toilet", "CaseOh", "The final boss", "Low-cortisol blud"
    ],
    "nouns": [
        "skibidi", "gyatt", "fanum tax", "sigma", "rizz", "mewing streak",
        "aura", "crashout", "bop", "motion", "opp", "glazer", "NPC",
        "yapaholic", "looksmaxxing", "goon cave", "phantom tax",
        "Ohio gas station", "Grimace Shake", "sub-zero aura", "drip",
        "canon event", "brainrot", "low-cortisol vibe", "edge streak",
        "chronocore", "goated energy", "alpha mentality"
    ],
    "verbs": [
        "rizz up", "mog", "looksmax", "mew", "glaze", "crash out",
        "lock in", "yap", "cook", "tax", "hit the griddy", "loss-farm",
        "lore-dump", "clasp hands", "tweak out", "aura-farm"
    ],
    "verbs_past": [
        "mew-mogged", "rizz-farmed", "lore-dumped", "sigma-cooked",
        "fanum-taxed", "crash-out-mogged", "aura-farmed", "got cooked",
        "ate and left no crumbs", "hit the griddy on", "glazed"
    ],
    "adjectives": [
        "cooked", "clapped", "unhinged", "sussy", "bussin", "lowkey",
        "highkey", "mid", "based", "brainrotted", "skibidi-certified",
        "demure", "chronocore", "goated", "acoustic", "chopped", "delulu",
        "zesty", "geeking"
    ],
    "modifiers": [
        "no cap", "fr fr", "deadass", "big yikes", "on god", "literally",
        "real talk", "blud think he slick"
    ],
    "outcomes": [
        "losing 50,000 aura instantly",
        "getting banished to Ohio",
        "achieving maximum motion",
        "getting mogged by a local NPC",
        "triggering a full crashout mode"
    ]
}

WORD_OF_THE_DAY_DB = [
    ("Skibidi", "Context-dependent universal word indicating chaos, absurdism, or unpredictable energy.", "Bro play was total skibidi."),
    ("Aura", "The intangible social currency/status points. Earned by cool moves, lost by embarrassing blunders.", "Bro lost 10,000 aura instantly."),
    ("Mog", "To completely physically or socially outshine someone so badly that they look inferior.", "He walked in and mogged the entire room."),
    ("Fanum Tax", "The mandatory food stolen from a friend's plate without consent.", "Hand over two fries, Fanum tax."),
    ("Crashout", "To completely lose all self-control and go wild over a minor issue.", "He failed the quiz and decided to crash out."),
    ("Rizz", "Charming social skill or effortless magnetic charisma.", "He has unspoken rizz."),
    ("Mewing", "The practice of resting the tongue on the mouth roof to sculpt a sharper jawline.", "Can't talk right now, I'm mewing."),
    ("Glazing", "Excessively over-praising or bootlicking someone to an embarrassing level.", "Stop glazing him, he's not gonna let you hit."),
    ("Unc", "An older individual clearly out of touch with modern youth culture.", "Unc tried to use slang and got cooked."),
    ("Looksmaxxing", "The hyper-optimization of physical features through grooming, posture, and effort.", "Bro is locked in on looksmaxxing."),
    ("Delulu", "Short for delusional; maintaining irrationally high expectations.", "She thinks he likes her, totally delulu."),
    ("Demure", "Mindful, modest, reserved, and considerate in posture and presentation.", "Very mindful, very demure.")
]

# =====================================================================
# GENERATION ENGINE
# =====================================================================

def generate_logic():
    """Generates a short, grammatically structured logical slang sentence."""
    templates = [
        lambda: f"{random.choice(LEXICON['subjects'])} {random.choice(LEXICON['verbs_past'])} {random.choice(LEXICON['subjects'])}, {random.choice(LEXICON['modifiers'])}.",
        lambda: f"When {random.choice(LEXICON['subjects'])} starts {random.choice(LEXICON['verbs'])}, it usually results in {random.choice(LEXICON['outcomes'])}.",
        lambda: f"That {random.choice(LEXICON['adjectives'])} {random.choice(LEXICON['nouns'])} is giving real {random.choice(LEXICON['adjectives'])} energy.",
        lambda: f"Maintaining a solid {random.choice(LEXICON['nouns'])} requires high {random.choice(LEXICON['nouns'])} and zero useless {random.choice(LEXICON['nouns'])}.",
        lambda: f"{random.choice(LEXICON['subjects'])} is literally {random.choice(LEXICON['adjectives'])} after {random.choice(LEXICON['outcomes'])}."
    ]
    sentence = random.choice(templates)()
    return sentence[0].upper() + sentence[1:]

def generate_unhinged():
    """Generates pure chaotic brainrot strictly locked to 3 or 4 words."""
    all_words = LEXICON["subjects"] + LEXICON["nouns"] + LEXICON["adjectives"] + LEXICON["verbs_past"]
    count = random.choice([3, 4])
    selected = random.sample(all_words, count)
    return " ".join(selected).upper() + "!"

# =====================================================================
# UI RENDERING (THEMED RICH INTERFACE)
# =====================================================================

def print_header(mode_label, style_color="bright_magenta"):
    """Prints the brainrot styled terminal banner."""
    header_text = Text("BRAINROT TERMINAL\n", style="bold bright_yellow")
    subtitle_text = Text(f"[{mode_label}]", style=f"bold {style_color}")
    panel = Panel(Align.center(header_text + subtitle_text), border_style=style_color, width=54)
    console.print(panel)

def display_result(sentence, mode_title, border_color):
    """Displays generated brainrot in a custom Rich panel."""
    body = Text()
    body.append("SLOP DROP: ", style="bold bright_yellow")
    body.append(f"\"{sentence}\"\n", style="bold italic bright_green")
    body.append("STATUS: ", style="bold bright_yellow")
    body.append("100% Brainrotted (Fr Fr)", style="bold bright_cyan")

    panel = Panel(body, title=f"[bold {border_color}] {mode_title} [/bold {border_color}]", border_style=border_color, width=54)
    console.print(panel)

def word_of_the_day():
    """Outputs Word of the Day UI card and terminates app immediately."""
    console.clear()
    term, definition, example = random.choice(WORD_OF_THE_DAY_DB)
    
    body = Text()
    body.append("DAILY BRAINROT ACQUIRED\n\n", style="bold bright_green")
    body.append("TERM: ", style="bold bright_yellow")
    body.append(f"{term.upper()}\n", style="bold bright_cyan")
    
    body.append("DEFINITION: ", style="bold bright_yellow")
    body.append(f"{definition}\n", style="white")
    
    body.append("EXAMPLE: ", style="bold bright_yellow")
    body.append(f"\"{example}\"", style="bold italic bright_green")

    panel = Panel(body, title="[bold bright_green] WORD OF THE DAY [/bold bright_green]", border_style="bright_green", width=54)
    console.print(panel)
    rprint("\n[bold bright_magenta]Daily dose acquired! Go touch grass blud! [/bold bright_magenta]\n")
    sys.exit(0)

# =====================================================================
# MAIN EXECUTION & CLI
# =====================================================================

def main():
    parser = argparse.ArgumentParser(description="Gen Z / Gen Alpha Brainrot Terminal Generator")
    parser.add_argument(
        "--mode",
        choices=["logic", "unhinged", "word_of_the_day"],
        help="Select brainrot generation mode via command line flag."
    )

    args = parser.parse_args()

    # CLI Flag Execution
    if args.mode:
        if args.mode == "logic":
            print_header("LOGICAL MODE (+100 AURA)", "bright_cyan")
            display_result(generate_logic(), "LOGICAL SLANG", "bright_cyan")
        elif args.mode == "unhinged":
            print_header("UNHINGED SLOP (3-4 WORDS MAX)", "bright_magenta")
            display_result(generate_unhinged(), "PURE UNHINGED SLOP", "bright_yellow")
        elif args.mode == "word_of_the_day":
            word_of_the_day()
        return

    # Interactive Brainrot Menu UI
    current_mode = "logic"
    
    while True:
        console.clear()
        mode_label = "LOGICAL MODE" if current_mode == "logic" else "UNHINGED MODE (3-4 WORDS)"
        mode_color = "bright_cyan" if current_mode == "logic" else "bright_magenta"
        
        print_header(mode_label, mode_color)
        
        rprint("[bold bright_yellow]SELECT YOUR VIBE:[/bold bright_yellow]")
        rprint(" [1] Generate Brainrot")
        rprint(f" [2] Switch Mode (Active: [bold {mode_color}]{current_mode.upper()}[/bold {mode_color}])")
        rprint(" [3] Word of the Day & Touch Grass")
        rprint(" [4] Exit Terminal")
        
        choice = Prompt.ask("\n[bold bright_magenta]Choice[/bold bright_magenta]", choices=["1", "2", "3", "4"], default="1")
        
        if choice == "1":
            time.sleep(0.05)
            console.clear()
            print_header(mode_label, mode_color)
            if current_mode == "logic":
                display_result(generate_logic(), "LOGICAL SLANG SENTENCE", "bright_cyan")
            else:
                display_result(generate_unhinged(), "UNHINGED 3-4 WORD BURST", "bright_yellow")
            Prompt.ask("\n[bold cyan]Press [ENTER] to cook again[/bold cyan]")
            
        elif choice == "2":
            current_mode = "unhinged" if current_mode == "logic" else "logic"
            rprint(f"\n[bold bright_yellow]Switching brainrot frequencies to {current_mode.upper()}...[/bold bright_yellow]")
            time.sleep(0.2)
            
        elif choice == "3":
            word_of_the_day()
            
        elif choice == "4":
            rprint("\n[bold bright_magenta]Terminal closed! Go touch grass blud! [/bold bright_magenta]\n")
            break

if __name__ == "__main__":
    main()
