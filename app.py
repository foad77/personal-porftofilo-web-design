from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import traceback

app = Flask(__name__)

# Load environment variables from config.env
load_dotenv('config.env')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def handle_contact_form():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')

    try:
        smtp_server = os.getenv('SENDINBLUE_SMTP_SERVER')
        smtp_port = int(os.getenv('SENDINBLUE_SMTP_PORT'))
        smtp_user = os.getenv('SENDINBLUE_USERNAME')
        smtp_password = os.getenv('SENDINBLUE_PASSWORD')
        recipient_email = os.getenv('RECIPIENT_EMAIL')

        print(f"SMTP Server: {smtp_server}")
        print(f"SMTP Port: {smtp_port}")
        print(f"SMTP User: {smtp_user}")
        print(f"Recipient Email: {recipient_email}")
        msg = MIMEMultipart()
        msg['From'] = 'foad@drfoadnajafi.tech'
        msg['To'] = recipient_email
        msg['Subject'] = f"New contact form submission: {subject}"

        body = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"
        msg.attach(MIMEText(body, 'plain'))

        print("Connecting to SMTP server...")
        server = smtplib.SMTP(smtp_server, smtp_port)
        print("Starting TLS...")
        server.starttls()
        print("Logging in...")
        server.login(smtp_user, smtp_password)
        print("Sending email...")
        server.sendmail('foad@drfoadnajafi.tech', recipient_email, msg.as_string())
        print("Quitting server...")
        server.quit()

        print("Email sent successfully!")
        return jsonify({'success': True, 'message': 'Email sent successfully'}), 200
    except Exception as e:
        print(f"Error: {str(e)}")
        print(traceback.format_exc())
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)