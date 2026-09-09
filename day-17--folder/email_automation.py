
import os
import pandas as pd
import logging
import smtplib
from email.message import EmailMessage

# Configure logging
logging.basicConfig(
    filename="email_automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    # Sample business data
    data = {
        "student": ["KANCHAN", "ROBERT", "AGILE"],
        "CT MARKS": [10, 25, 15],
        "CREDITS": [50000, 12500, 22500]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Generate Excel report
    df.to_excel("business_report.xlsx", index=False)

    logging.info("Business report generated successfully.")
    print("Business report generated successfully.")

    # Get email credentials from environment variables
    sender = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("RECIPIENT_EMAIL")

    # Check credentials
    if not sender or not password or not receiver:
        raise ValueError("Email environment variables are not configured.")

    # Create email
    msg = EmailMessage()
    msg["Subject"] = "Business Report"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content("Please find the attached business report.")

    # Attach Excel report
    with open("business_report.xlsx", "rb") as file:
        report = file.read()

    msg.add_attachment(
        report,
        maintype="application",
        subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename="business_report.xlsx"
    )

    # Connect to SMTP server and send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)

    logging.info("Email sent successfully.")
    print("Email sent successfully.")

except Exception as e:
    logging.error(f"Error occurred: {e}")
    print(f"Operation failed: {e}")

