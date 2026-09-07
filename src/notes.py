# This module provides functions to take and show notes.
def takeNote():
    note = input("Please enter your note: ")
    if note.strip() == "":
        print("Empty note not saved.")
    else:
        with open("data/notes.txt", "a") as file:
            file.write(note + "\n")

def showNotes():
    try:
        with open("data/notes.txt", "r") as file:
            notes = file.readlines()
    except FileNotFoundError:
        print("File has not been created yet. Please take a note first.")
        return
    if notes:
        print("Your Notes:")
        for idx, note in enumerate(notes, start=1):
            print(f"{idx}. {note.strip()}")
    else:
        print("No notes found.")