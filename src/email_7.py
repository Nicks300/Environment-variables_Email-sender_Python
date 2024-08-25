import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from src.config_6 import SMTPSettings


class EmailMessage:
    def __init__(self, from_email: str, to_email: str, subject: str, body: str) -> None:
        self.from_email = from_email
        self.to_email = to_email
        self.subject = subject
        self.body = body

    def create_mime_message(self) -> MIMEMultipart:
        message = MIMEMultipart()
        message['From'] = self.from_email
        message['To'] = self.to_email
        message['Subject'] = self.subject
        message.attach(MIMEText(self.body, 'plain'))
        return message


class EmailSender:
    def __init__(self, smtp_settings: SMTPSettings) -> None:
        self.smtp_settings = smtp_settings

    def send_email(self, message: EmailMessage) -> None:
        self.message = message
        mime_message = message.create_mime_message()
        try:
            with smtplib.SMTP(self.smtp_settings.server, self.smtp_settings.port) as server:
                server.starttls()
                server.login(self.smtp_settings.email, self.smtp_settings.email_password)
                server.sendmail(self.smtp_settings.email, self.message.to_email, mime_message.as_string())
                print('Письмо успешно отправлено')
        except:
            print('Ошибка при отправке письма!')
