# Реализовать консольное приложение заметки, с сохранением, чтением,

# добавлением, редактированием и удалением заметок. Заметка должна

# содержать идентификатор, заголовок, тело заметки и дату/время создания или

# последнего изменения заметки. Сохранение заметок необходимо сделать в

# формате json или csv формат


import json

import os

from datetime import datetime


class Note:

    def __init__(self, id, title, body, creation_time):

        self.id = id

        self.title = title

        self.body = body

        self.creation_time = creation_time

        self.last_modified_time = creation_time

    def to_dict(self):
        return{
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "creation_time": str(self.creation_time),
            "last_modified_time": str(self.last_modified_time)       
            }
        # returnjls_extract_var
    

@classmethod

def from_dict(clcs, d):

    return cls(

        id= d["id"],

        title= d["title"],

        body= d["body"],

        creation_time= datetime.fromisoformat(d["creation_time"])
    )


def __repr__(self):

    return f"<Note {self.title} ({self.id})>"

def load_notes():

    if os.path.exists("notes.json"):

        with open("notes.json", "r") as f:

            data = json.load(f)
    else:

        data = {"notes": []}

    return data


def save_notes(data):

    with open("notes.json", "w") as f:

        json.dump(data, f, indent=4)

def create_note():

    title = input("Enter note title: ")

    body = input("Enter note body: ")

    timestamp = datetime.now()

    id = len(data["notes"]) + 1

    note = Note(id, title, body, timestamp)

    data["notes"].append(note.to_dict())

    save_notes(data)

    print(f"Note '{title}' created.")


def read_note():

    identifier = input("Enter note id or title: ")

    for note_dict in data["notes"]:

        if str(note_dict["id"]) == identifier or note_dict["title"] == identifier:

            note = Note.from_dict(note_dict)

            print(note.title)

            print(note.body)

            print(note.creation_time)

            print(note.last_modified_time)

            return

    print(f"Note'{identifier}' not founfd.")


def update_note():

    identifier = input("Enter note id or title: ")

    for note_dict in data["notes"]:

        title = input(f"Enter new title ({note_dict['title']}):")

        body = input(f"Enter new body ({note_dict['body']}): ")

        note_dict["title"] = title or note_dict["title"]

        note_dict["body"] = body or note_dict["body"]

        note_dict["last_modified_time"] = str(datetime.now())

        save_notes(data)

        print(f"Note '{note_dict['title']}' updated")

        return

    print(f"Note '{identifier}' not found.")

def delete_note():

    identifier = input("Enter note id or title: ")

    for note_dict in data["notes"]:

        if str(note_dict["id"]) == identifier or note_dict["title"] == identifier:

            data["notes"].remove(note_dict)

            save_notes(data)

            print(f"Note '{note_dict['title']}' deleted. ")

            return

        print(f"Note '{identifier}' not found. ")

def list_notes():

    for note_dict in data["notes"]:

        note = Note.from_dict(note_dict)

        print(note.title)

        print(note.body)

        print(note.creation_time)

        print(note.last_modified_time)

        print()

def main():

    global data 
    data = load_notes()


    while True:

        action = input("Enter 'n' to create a new note, 'r' to read a note, 'u' to update a note, 'd' to delete a note, 'l' to list all notes, 'q' to quit: ")
        if action == "n":
            create_note()
        elif action == "r":
            read_note()

        elif action == "u":

            update_note()
        elif action == "d":
            delete_note()
        elif action == "l":
            list_notes()

        elif action == "q":

            break

        else:

            print("invalid action. ")

if __name__ == "__main__":
    main()





