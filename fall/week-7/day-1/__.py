from datetime import datetime

journal_filename = "journal.txt"

def display_journal():
    """Displays the contents of the journal onto the output screen."""
    entries = read_journal_entries()
    
    for entry in entries:
        print(entry, end="")

def read_journal_entry() -> str:
    """Reads an entry from the keyboard and returns it.

    Returns:
        str: The entry read, with a timestamp.
    """
    entry = input("Entry: ")
    
    now = datetime.now()
    ts = now.strftime("%Y-%m-%d %H:%M")
    
    return f"{ts} {entry}"

def read_journal_entries() -> list[str]:
    """Reads all entries from the journal file and returns them.

    Returns:
        list[str]: The journal entries.
    """
    with open(journal_filename, mode="r") as f:
        return f.readlines()
    
def write_journal_entry(entry: str):
    """Writes an entry to the journal file.

    Args:
        entry (str): The entry to write to the file.
    """
    with open(journal_filename, mode="a") as f:
        f.write(entry + "\n")

# Main Program:

while True:
    menu = """Options:
        1. Display journal
        2. Write a new entry
        3. Quit
    """

    print(menu)
    
    selection = input("Make a selection: ").strip()
    if selection == "1":
        display_journal()
    elif selection == "2":
        entry = read_journal_entry()
        write_journal_entry(entry)
    elif selection == "3":
        print("Goodbye.")
        break
