# import smtplib
from email.mime.multipart import MIMEMultipart
from src.config_6 import SMTPSettings
from src.email_6 import EmailMessage


def main() -> MIMEMultipart:
    patient_email = input('Введите почту пациента: ')

    smtp_settings = SMTPSettings()

    email_message = EmailMessage(
        from_email=smtp_settings.email,
        to_email=patient_email,
        subject='Receipt',
        body='Test'
    )

    mime_message = email_message.create_mime_message()

    # настройка сервера

    # with smtplib.SMTP(smtp_settings.server, smtp_settings.port) as server:
    #     server.starttls()
    #     server.login(smtp_settings.email, smtp_settings.email_password)
    #     server.sendmail(smtp_settings.email, patient_email, mime_message.as_string())
    #     print('Проверь почту!')

    return mime_message


if __name__ == "__main__":
    main()
