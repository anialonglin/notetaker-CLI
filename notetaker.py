# CLI interface
import argparse
from db import create_note, list_notes, update_note, delete_note

parser = argparse.ArgumentParser(description="Notetaker CLI - manage notes in PostgreSQL")
subparsers = parser.add_subparsers(dest="command", required=True)

# Create command
create_parser = subparsers.add_parser("create", help="Create a new note")
create_parser.add_argument("--title", required=True, help="Title of the note")
create_parser.add_argument("--content", required=True, help="Content of the note")

# List command
list_parser = subparsers.add_parser("list", help="List all notes")

# Update command
update_parser = subparsers.add_parser("update", help="Update a note")
update_parser.add_argument("--id", type=int, required=True, help="ID of the note to update")
update_parser.add_argument("--title", help="New title")
update_parser.add_argument("--content", help="New content")

# Delete command
delete_parser = subparsers.add_parser("delete", help="Delete a note")
delete_parser.add_argument("--id", type=int, required=True, help="ID of the note to delete")

args = parser.parse_args()

# Command handler
if args.command == "create":
    create_note(args.title, args.content)
elif args.command == "list":
    list_notes()
elif args.command == "update":
    update_note(args.id, args.title, args.content)
elif args.command == "delete":
    delete_note(args.id)
