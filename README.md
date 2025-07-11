# Notetaker CLI (Python + PostgreSQL)

A simple CLI app to create, list, update, and delete notes using PostgreSQL.

## Features
- Create, view, update, delete notes
- CLI via argparse
- PostgreSQL integration using psycopg2

## Command
```
python notetaker.py create --title "Hello" --content "World"
python notetaker.py list
python notetaker.py update --id 1 --title "Updated"
python notetaker.py delete --id 1
```
# Setup
- Create .env file with DB credentials
- Run the script with Python
- Requires psycopg2 and python-dotenv


