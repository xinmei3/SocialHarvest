from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText
from email import encoders
import os


mail_host = "smtp.qq.com"
mail_user = ""  # 替换为用户
mail_pass = "ginbizweplqoijbh"
sender = ""  # 替换为你的发送邮件的邮箱
receiver = "18340835294@163.com"  # 替换为接收邮件的邮箱


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
                part.add_header("Content-Disposition", f'attachment; filename="{filename}"')
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
        'C:\\Users\\张耀文\\Documents\\requesets_lib\\user_info\\tiktok_like_list.txt',
        'C:\\Users\\张耀文\\Documents\\requesets_lib\\user_info\\tiktok_video_list.txt',
    ])