import requests
from database import SessionLocal, Contact  # Import database functions
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email_validator import validate_email, EmailNotValidError

API_KEY = "9615285bb174110dbc77743385b83ab68fcc6e0c"

def find_email(name, company):
    """Search for an email using Hunter.io"""
    url = f"https://api.hunter.io/v2/email-finder?domain={company}&first_name={name.split()[0]}&last_name={name.split()[-1]}&api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if "data" in data and "email" in data["data"]:
        return data["data"]["email"]
    return None

def save_contact(name, company):
    """Finds and saves the contact info in the database"""
    session = SessionLocal()
    email = find_email(name, company)
    
    # Check if the email already exists
    existing_contact = session.query(Contact).filter(Contact.email == email).first()
    if existing_contact:
        print(f"✅ {email} already exists in the database.")
    else:
        # If no contact exists, save the new contact
        contact = Contact(name=name, company=company, email=email)
        session.add(contact)
        session.commit()
        print(f"✅ Found and saved: {name} - {email}")
    
    session.close()
    
    if email:
        send_email(email, name)  # Send email after checking if email exists
    else:
        print(f"❌ No email found for {name}.")


def send_email(to_email, name):
    """Send email using Gmail SMTP"""
    from_email = "sathvikbellary12@gmail.com"
    app_password = "jybz beyx ugst txtv"  # Use App password or regular Gmail password
    
    subject = "Interested in SDE Role"
    # Use the actual recipient email in the tracking URL
    tracking_url = f"https://94fe-162-242-90-17.ngrok-free.app/track_open/{to_email}"  # The URL of your tracking server
    print(f"Tracking URL: {tracking_url}")
    body = f"""
    Hi {name},

    I hope this email finds you well! I'm currently exploring new career opportunities and wanted to express my interest in any SDE roles at your company. If you have any open positions, I would love to be considered.

    Best regards,
    Sathvik

    <img src="{tracking_url}" width="1" height="1" style="display:none;"/>
    """  # Add a tiny invisible image for tracking

    # Prepare the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))  # Set content type as 'html' to support the image tag

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(from_email, app_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.close()
        print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f"Error sending email: {e}")

        

if __name__ == "__main__":
    name = input("Enter the person's full name: ")
    company = input("Enter the company domain (e.g., google.com): ")
    save_contact(name, company)
