from database import SessionLocal, Contact

def list_contacts():
    session = SessionLocal()
    contacts = session.query(Contact).all()
    session.close()

    if not contacts:
        print("No contacts found.")
    else:
        for contact in contacts:
            print(f"Name: {contact.name}, Company: {contact.company}, Email: {contact.email}")

if __name__ == "__main__":
    list_contacts()
