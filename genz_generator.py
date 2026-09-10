import random
import argparse
import sys

# Expanded 2025/2026 Gen Z & Gen Alpha Brainrot Vocabulary
NOUNS = [
    "sigma", "alpha", "beta", "blud", "shlawg", "fanum tax", "gyatt", 
    "rizz", "rizzler", "skibidi", "Ohio", "grindset", "dawg", "aura", 
    "diddyblud", "main NPC", "canon event", "brainrot", "drip"
]

ADJECTIVES = [
    "bussin", "delulu", "cringe", "cooked", "goofy ahh", "sussy", 
    "zesty", "ultra-based", "clapped", "demure", "chronocore", "goated", "acoustic"
]

VERBS = [
    "mogged", "ate", "cooked", "edged", "hit the griddy", "ghosted", 
    "clapped back", "finessed", "flexed"
]

MODIFIERS = [
    "no cap", "fr fr", "deadass", "big yikes", "uwu", "on god", "literally"
]

def generate_logic():
    """Generates a short, grammatically logical sentence using heavy slang."""
    templates = [
        f"Bro {random.choice(VERBS)} and left no crumbs, {random.choice(MODIFIERS)}.",
        f"That {random.choice(NOUNS)} is looking real {random.choice(ADJECTIVES)} today.",
        f"You can't have negative {random.choice(NOUNS)} in {random.choice(['Ohio', 'this economy'])}, {random.choice(MODIFIERS)}.",
        f"The {random.choice(ADJECTIVES)} {random.choice(NOUNS)} just {random.choice(VERBS)} my {random.choice(NOUNS)}.",
        f"Staying {random.choice(ADJECTIVES)} is a massive {random.choice(NOUNS)}."
    ]
    return random.choice(templates)

def generate_unhinged():
    """Generates 3-4 word purely chaotic and stupid brainrot."""
    pool = NOUNS + ADJECTIVES + VERBS
    # Pick 3 or 4 random words
    words = random.sample(pool, random.choice([3, 4]))
    return " ".join(words)

def word_of_the_day():
    """Generates a Word of the Day block and exits immediately."""
    definitions = {
        "Skibidi": "Context-dependent filler word for anything chaotic or absurd.",
        "Fanum Tax": "The act of stealing a bite of your friend's food.",
        "Gyatt": "An exclamation of surprise, usually regarding someone's appearance.",
        "Mogging": "To establish dominance over someone by looking significantly better.",
        "Chronocore": "Something extremely trendy but highly temporary.",
        "Demure": "Mindful, considerate, and modest. Very demure.",
        "Delulu": "Short for delusional; remaining intentionally ignorant of reality.",
        "Goofy ahh": "Something remarkably silly or foolish."
    }
    word = random.choice(list(definitions.keys()))
    print(f"🌟 WORD OF THE DAY: {word} 🌟")
    print(f"Definition: {definitions[word]}")
    print(f"Example: {generate_logic()}")
    sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gen Z / Gen Alpha Brainrot Generator")
    parser.add_argument("--mode", choices=Here is a Python script packed with an extensive dictionary of Gen Z and Gen Alpha brainrot terminology, memes, and slang.

It features all **3 modes**:
1. **`logic`**: Generates syntactically sound, grammatically logical observations using brainrot concepts.
2. **`unhinged`**: Outputs a strictly 3 to 4 word burst of chaotic brainrot.
3. **`word_of_the_day`**: Outputs one word with its definition and exits.

```python
import random
import sys

# --- Extensive Brainrot & Gen Z/Alpha Lexicon ---
LEXICON = {
    "nouns": [
        "skibidi", "gyatt", "fanum tax", "sigma", "rizzler", "mewing streak",
        "aura", "crashout", "unc", "bop", "motion", "opp", "glazer", "NPC",
        "shadow wizard money brigade", "yapaholic", "looksmaxxer", "gooner",
        "phantom tax", "Ohio resident", "Baby Gronk", "Kai Cenat", "Livvy Dunne",
        "edgemaxxer", "grimace shake", "sub-zero aura"
    ],
    "verbs": [
        "rizz up", "mog", "looksmax", "mew", "glaze", "crash out",
        "lock in", "yap", "cook", "tax", "loss-farm", "tweak"
    ],
    "adjectives": [
        "cooked", "clapped", "unhinged", "sus", "bussin", "lowkey", "highkey",
        "mid", "based", "brainrotted", "skibidi-certified", "valid", "cooked to a crisp"
    ],
    "outcomes": [
        "losing 50,000 aura instantly",
        "getting banished to Ohio",
        "achieving maximum motion",
        "getting mogged by an NPC",
        "triggering an immediate crashout"
    ]
}

WORD_OF_THE_DAY_DB = {
    "Aura": "The invisible currency of social status. Gained by doing cool things, lost instantly by fumbling.",
    "Mog": "To visually or socially dominate someone so completely that they look inferior by comparison.",
    "Fanum Tax": "The mandatory percentage of food stolen from a friend's plate without prior notice.",
    "Crashout": "To completely lose all self-control and ruin one's life over a trivial inconvenience.",
    "Rizzler": "An individual with an absurdly high capability for smooth social persuasion.",
    "Mewing": "The act of resting your tongue on the roof of your mouth to sculpt your jawline.",
    "Glazing": "Over-hyping or brown-nosing someone to an embarrassing, excessive degree.",
    "Unc": "An older person out of touch with modern slang, usually over the age of 22.",
    "Yapaholic": "Someone incapable of stopping continuous, empty talk.",
    "Motion": "Having money, power, active progress, and zero downtime in life.",
    "Looksmaxxing": "The hyper-optimization of every physical trait through intense grooming and discipline.",
    "Skibidi": "A universal noun/adjective indicating unpredictable, surreal, or modern absurd content."
}

def generate_logic():
    templates = [
        lambda: f"Maintaining a solid {random.choice(LEXICON['nouns'])} requires high-level {random.choice(LEXICON['nouns'])} and zero useless {LEXICON['verbs'][7]}.",
        lambda: f"When a {random.choice(LEXICON['nouns'])} tries to {random.choice(LEXICON['verbs'])} without {random.choice(LEXICON['nouns'])}, it usually results in {random.choice(LEXICON['outcomes'])}.",
        lambda: f"The fundamental difference between a true {random.choice(LEXICON['nouns'])} and an ordinary {random.choice(LEXICON['nouns'])} is their ability to {random.choice(LEXICON['verbs'])} under pressure.",
        lambda: f"Excessive {random.choice(LEXICON['nouns'])} will leave your entire setup looking completely {random.choice(LEXICON['adjectives'])}."
    ]
    return random.choice(templates)()

def generate_unhinged():
    # Strictly 3 or 4 words of pure brainrot
    all_words = (
        LEXICON["nouns"] + 
        LEXICON["verbs"] + 
        LEXICON["adjectives"]
    )
    word_count = random.choice([3, 4])
    selected = random.sample(all_words, word_count)
    return " ".join(selected).upper()

def generate_word_of_the_day():
    word, definition = random.choice(list(WORD_OF_THE_DAY_DB.items()))
    return f"📖 WORD OF THE DAY: {word.upper()}\nDefinition: {definition}"

def run_generator(mode="logic"):
    mode = mode.lower()
    if mode == "logic":
        print(generate_logic())
    elif mode == "unhinged":
        print(generate_unhinged())
    elif mode in ["word_of_the_day", "word", "wotd"]:
        print(generate_word_of_the_day())
        sys.exit(0)
    else:
        print("Unknown mode. Choose from: 'logic', 'unhinged', or 'word_of_the_day'.")

if __name__ == "__main__":
    # Change mode here: "logic", "unhinged", or "word_of_the_day"
    selected_mode = "unhinged"
    
    # Or pass via command-line: python script.py unhinged
    if len(sys.argv) > 1:
        selected_mode = sys.argv[1]
        
    run_generator(selected_mode)
