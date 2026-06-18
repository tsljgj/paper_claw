"""
Email sending module with attachment support for full digest.
"""
import json
import logging
import os
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
from pathlib import Path

# Friendly display name shown to the recipient as the sender. Override with the
# EMAIL_FROM_NAME environment variable / GitHub secret if you want a different one.
SENDER_NAME = os.getenv("EMAIL_FROM_NAME", "Zhihao's Paper Assistant")


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


def send_single_email(host: str, port: int, user: str, password: str, 
                      recipient_email: str, recipient_name: str,
                      subject: str, html_body: str, attachment_paths: list[Path] = None) -> bool:
    """
    Send a single personalized HTML email.
    
    Args:
        host: SMTP host
        port: SMTP port  
        user: SMTP user
        password: SMTP password
        recipient_email: Recipient email address
        recipient_name: Recipient name for personalization
        subject: Email subject
        html_body: HTML content (should contain {{ recipient_name }} placeholder)
        attachment_paths: List of paths to file attachments
        
    Returns:
        True if sent successfully, False otherwise
    """
    # Personalize the HTML body - handle both template variable and plain text replacement
    personalized_html = html_body.replace("{{ recipient_name }}", recipient_name)
    # Also try to replace if the variable is used differently in template
    if "recipient_name" in personalized_html and "{{" not in personalized_html:
        personalized_html = personalized_html.replace("recipient_name", recipient_name)
    
    # Create multipart message
    message = MIMEMultipart("mixed")
    message["Subject"] = subject
    # Show a friendly sender name (e.g. "Zhihao's Paper Assistant <addr@gmail.com>")
    # instead of the bare Gmail address.
    message["From"] = formataddr((SENDER_NAME, user))
    message["To"] = recipient_email
    
    # Add HTML part
    html_part = MIMEMultipart("alternative")
    html_part.attach(MIMEText(personalized_html, "html", "utf-8"))
    message.attach(html_part)
    
    # Add attachments if provided. Accept either a single path or a list.
    if attachment_paths:
        if isinstance(attachment_paths, (str, Path)):
            attachment_paths = [attachment_paths]
        for attachment_path in attachment_paths:
            if attachment_path and attachment_path.exists():
                try:
                    with open(attachment_path, "rb") as f:
                        attachment = MIMEApplication(f.read())
                        attachment.add_header(
                            "Content-Disposition",
                            f"attachment; filename=\"{attachment_path.name}\""
                        )
                        message.attach(attachment)
                        logging.info("Attached file: %s", attachment_path.name)
                except Exception as e:
                    logging.warning("Failed to attach file %s: %s", attachment_path, e)
    
    try:
        with smtplib.SMTP_SSL(host, port, timeout=30) as server:
            server.login(user, password)
            server.sendmail(user, [recipient_email], message.as_string())
        logging.info("Email sent successfully to %s (%s)", recipient_name, recipient_email)
        return True
    except Exception as e:
        logging.error("Failed to send email to %s: %s", recipient_email, e)
        return False


def send_html_email(subject: str, html_body: str, attachment_paths: list[Path] = None, 
                   preview_mode: bool = False) -> list[dict]:
    """
    Send HTML email with optional attachments to all configured recipients.
    
    Args:
        subject: Email subject
        html_body: HTML content (can contain {{ recipient_name }} placeholder)
        attachment_paths: List of paths to file attachments
        preview_mode: If True, only return recipient list without sending
        
    Returns:
        List of recipient info dicts with email, name, and status
    """
    if not email_enabled():
        logging.info("SMTP secrets not fully configured; skipping email.")
        return []

    host = os.environ["SMTP_HOST"]
    port = int(os.environ["SMTP_PORT"])
    user = os.environ["SMTP_USER"]
    password = os.environ["SMTP_PASS"]
    
    # Try to load from config file first
    config = load_recipients_config()
    if config:
        recipients = config["recipients"]
        logging.info("Using recipients from config/recipients.json")
    else:
        # Fallback to env var
        emails = [item.strip() for item in os.environ.get("EMAIL_TO", "").split(",") if item.strip()]
        recipients = [{"email": e, "name": e.split("@")[0]} for e in emails]
    
    if not recipients:
        logging.warning("No recipients configured; skipping email.")
        return []
    
    results = []
    
    if preview_mode:
        # Just return recipient list for preview
        for r in recipients:
            results.append({
                "email": r["email"],
                "name": r["name"],
                "status": "preview"
            })
        return results
    
    # Send to each recipient individually for personalization
    logging.info("Sending digest email to %s recipient(s)...", len(recipients))
    
    for r in recipients:
        email = r["email"]
        name = r["name"]
        
        success = send_single_email(
            host, port, user, password,
            email, name,
            subject, html_body, attachment_paths
        )
        
        results.append({
            "email": email,
            "name": name,
            "status": "sent" if success else "failed"
        })
    
    success_count = sum(1 for r in results if r["status"] == "sent")
    logging.info("Email sending complete: %s/%s successful", success_count, len(recipients))
    
    return results
