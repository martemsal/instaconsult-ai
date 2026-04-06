import json
import os
import sys
import uuid

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'database', 'companies.json')

def load_db():
    if not os.path.exists(DB_PATH):
        return []
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_db(db):
    with open(DB_PATH, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=4, ensure_ascii=False)

def add_company(name, niche, plan="Free"):
    db = load_db()
    new_company = {
        "id": str(uuid.uuid4()),
        "name": name,
        "niche": niche,
        "plan": plan,
        "status": "Active",
        "analysis_pending": False
    }
    db.append(new_company)
    save_db(db)
    print(f"Company {name} added successfully with ID {new_company['id']}")

def request_analysis(company_id):
    db = load_db()
    for company in db:
        if company['id'] == company_id:
            company['analysis_pending'] = True
            save_db(db)
            print(f"Analysis requested for {company['name']} ({company_id})")
            return True
    print(f"Company {company_id} not found.")
    return False

def list_companies():
    db = load_db()
    print(json.dumps(db, indent=4, ensure_ascii=False))

def delete_company(company_id):
    db = load_db()
    new_db = [c for c in db if c['id'] != company_id]
    if len(new_db) < len(db):
        save_db(new_db)
        print(f"Company {company_id} deleted.")
    else:
        print(f"Company {company_id} not found.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python manage_companies.py [add/list/delete] [args...]")
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == "add":
        add_company(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else "Free")
    elif cmd == "list":
        list_companies()
    elif cmd == "delete":
        delete_company(sys.argv[2])
