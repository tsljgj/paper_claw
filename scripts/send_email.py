import logging
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def email_enabled() -> bool:
    required = ["SMTP_HOST", "SMTP_PORT", "SMTP_USER", "SMTP_PASS", "EMAIL_TO"]
    return all(os.getenv(item) for item in required)


def send_html_email(subject: str, html_body: str) -> None:
    if not email_enabled():
        logging.info("SMTP secrets not fully configured; skipping email.")
        return

    host = os.environ["SMTP_HOST"]
    port = int(os.environ["SMTP_PORT"])
    user = os.environ["SMTP_USER"]
    password = os.environ["SMTP_PASS"]
    recipients = [item.strip() for item in os.environ["EMAIL_TO"].split(",") if item.strip()]

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = user
    message["To"] = ", ".join(recipients)
    message.attach(MIMEText(html_body, "html", "utf-8"))

    logging.info("Sending digest email to %s recipient(s).", len(recipients))
    with smtplib.SMTP_SSL(host, port, timeout=30) as server:
        server.login(user, password)
        server.sendmail(user, recipients, message.as_string())
