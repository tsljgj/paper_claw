import json
import logging
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path


def load_recipients_config() -> dict:
    """Load recipients from config/recipients.json if exists, fallback to env."""
    config_path = Path(__file__).resolve().parents[1] / "config" / "recipients.json"
    if config_path.exists():
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                config = json.load(f)
                # Filter enabled recipients
                enabled = [r for r in config.get("recipients", []) if r.get("enabled", True)]
                if enabled:
                    return {
                        "recipients": enabled,
                        "settings": config.get("settings", {})
                    }
        except Exception as e:
            logging.warning("Failed to load recipients.json: %s", e)
    return None


def email_enabled() -> bool:
    required = ["SMTP_HOST", "SMTP_PORT", "SMTP_USER", "SMTP_PASS"]
    return all(os.getenv(item) for item in required)


def send_html_email(subject: str, html_body: str) -> None:
    if not email_enabled():
        logging.info("SMTP secrets not fully configured; skipping email.")
        return

    host = os.environ["SMTP_HOST"]
    port = int(os.environ["SMTP_PORT"])
    user = os.environ["SMTP_USER"]
    password = os.environ["SMTP_PASS"]
    
    # Try to load from config file first
    config = load_recipients_config()
    if config:
        recipients = [r["email"] for r in config["recipients"]]
        logging.info("Using recipients from config/recipients.json")
    else:
        # Fallback to env var
        recipients = [item.strip() for item in os.environ.get("EMAIL_TO", "").split(",") if item.strip()]
    
    if not recipients:
        logging.warning("No recipients configured; skipping email.")
        return

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = user
    message["To"] = ", ".join(recipients)
    message.attach(MIMEText(html_body, "html", "utf-8"))

    logging.info("Sending digest email to %s recipient(s): %s", len(recipients), ", ".join(recipients))
    with smtplib.SMTP_SSL(host, port, timeout=30) as server:
        server.login(user, password)
        server.sendmail(user, recipients, message.as_string())
    logging.info("Email sent successfully.")
