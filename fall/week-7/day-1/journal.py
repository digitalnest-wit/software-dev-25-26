from datetime import datetime

journal_filename = "myfile.txt"

def display_journal():
    entries = read_journal_entries()
    
    if len(entries) == 0:
        print("Journal is empty. Enter some text, then press [Enter].")
        return
    
    print("Saved Entries:")
    for i, line in enumerate(entries):
        print(f"  {i + 1}: {line.strip("\n")}")

def read_journal_entry() -> str:
    entry = input("> Entry: ")
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M")
    
    # Add a new line at the end of the entry to separate it from other
    # entries in the journal.
    return f"{timestamp} :: {entry}\n"

def read_journal_entries() -> list[str]:
    with open(journal_filename, mode="r") as file:
        return file.readlines()
    
def write_journal_entry(entry: str):
    with open(journal_filename, mode="a") as file:
        file.writelines([entry])

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
