from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os, ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import traceback
from loguru import logger
from models import Session, Contact
from datetime import datetime

app = Flask(__name__)


# Create a default SSL context
context = ssl.create_default_context()

# Load environment variables from config.env
load_dotenv('config.env')

@app.route('/')
def home():
    return render_template('index.html')

# Set up Loguru
#log_path = os.path.join("/home/Web/My_flask_app", 'flask_app_log.txt')
logger.add('flask_app_log.txt', level="DEBUG", format="{time} - {level} - {message}")

logger.info("Logging setup complete. Test log entry.")

@app.route('/contact', methods=['POST'])
def handle_contact_form():
    logger.debug("handle_contact_form called")
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')


    # Save the contact form data to the database
    session = Session()
    try:
        new_contact = Contact(
            name=name,
            email=email,
            subject=subject,
            message=message,
            timestamp=datetime.now()
        )
        session.add(new_contact)
        session.commit()
        logger.info("Contact form data saved to database.")
        return jsonify({'success': True, 'message': 'Data saved successfully'}), 200
    except Exception as e:
        session.rollback()
        logger.error(f"Database error: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500
    finally:
        session.close()

    try:
        smtp_server = os.getenv('SENDINBLUE_SMTP_SERVER')
        smtp_server = smtp_server.strip()
        smtp_port = 587
        smtp_user = os.getenv('SENDINBLUE_USERNAME')
        smtp_password = os.getenv('SENDINBLUE_PASSWORD')
        recipient_email = os.getenv('RECIPIENT_EMAIL')

        logger.info(f"SMTP Server: {smtp_server}")
        logger.info(f"SMTP Port: {smtp_port}")
        logger.info(f"SMTP User: {smtp_user}")
        logger.info(f"Recipient Email: {recipient_email}")

        msg = MIMEMultipart()
        msg['From'] = 'foad@drfoadnajafi.tech'
        msg['To'] = recipient_email
        msg['Subject'] = f"New contact form submission: {subject}"

        body = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"
        msg.attach(MIMEText(body, 'plain'))

        logger.info("Connecting to SMTP server...")
        server = smtplib.SMTP(smtp_server, smtp_port,timeout=10)
        server.ehlo()
        logger.info("Starting TLS...")
        logger.debug(f"SMTP Server before starttls: {smtp_server}")
        server.starttls(context=context)
        logger.info("Logging in...")
        server.login(smtp_user, smtp_password)
        logger.info("Sending email...")
        server.sendmail('foad@drfoadnajafi.tech', recipient_email, msg.as_string())
        logger.info("Quitting server...")
        server.quit()

        logger.info("Email sent successfully!")
        return jsonify({'success': True, 'message': 'Email sent successfully'}), 200
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
