import sys
from app import create_app, db

print("Connecting to database...")
app = create_app()

with app.app_context():
    try:
        print("Dropping old tables...")
        db.drop_all()  # delete old tables
        print("Creating new tables...")
        db.create_all()# new tables with 256
        print("Baza de date a fost (re)creată.")
    except Exception as e:
        print(f"ERROR: Could not recreate tables. Error: {e}", file=sys.stderr)
        sys.exit(1)

print("Init script finished.")