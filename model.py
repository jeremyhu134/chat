import json

def load_db():
    with open("flashcards_db.json") as f:
        return json.load(f)

db = load_db()

accounts = [
  {
    "username": "Satvik",
    "password": "password"
  }
]