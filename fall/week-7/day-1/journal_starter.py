from datetime import datetime

journal_filename = ""

def display_journal():
    """Displays the contents of the journal onto the output screen."""
    pass

def read_journal_entry() -> str:
    """Reads an entry from the keyboard and returns it.

    Returns:
        str: The entry read, with a timestamp.
    """
    raise NotImplementedError

def read_journal_entries() -> list[str]:
    """Reads all entries from the journal file and returns them.

    Returns:
        list[str]: The journal entries.
    """
    raise NotImplementedError
    
def write_journal_entry(entry: str):
    """Writes an entry to the journal file.

    Args:
        entry (str): The entry to write to the file.
    """
    raise NotImplementedError

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
