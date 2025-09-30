from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText
from email import encoders
import os
from requesets_lib.common.user_info_manager import UserInfo


email_info = UserInfo.user_info_loader()
mail_host = email_info["email"]["mail_host"]
mail_user = email_info["email"]["mail_user"]
mail_pass = email_info["email"]["mail_pass"]
sender    = email_info["email"]["sender"]
receiver  = email_info["email"]["receiver"]


def send_email(subject, content, attachment_paths=None):
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver
    msg.attach(MIMEText(content, "plain", "utf-8"))

    if attachment_paths:
        if isinstance(attachment_paths, str):
            attachment_paths = [attachment_paths]
        for attachment in attachment_paths:
            filename = os.path.basename(attachment)
            with open(attachment, "rb") as f:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f'attachment; filename="{Header(filename, "utf-8").encode()}"'
                )
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename*=UTF-8''{Header(filename, 'utf-8').encode()}"
                )
                msg.attach(part)

    try:
        with smtplib.SMTP_SSL(mail_host, 465) as server:
            server.login(mail_user, mail_pass)
            server.sendmail(sender, [receiver], msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    subject = "Test Email"
    content = "This is a test email sent from Python."
    send_email(subject, content, [
        "/path/to/attachment1.txt",
        "/path/to/attachment2.jpg"
    ])