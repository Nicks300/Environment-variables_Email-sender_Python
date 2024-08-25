from src.config_6 import SMTPSettings, Configuration
from src.email_7 import EmailMessage, EmailSender
from src.doctor_5 import Doctor



def main():
    configuration = Configuration()
    doc = Doctor(configuration)

    mode = input("Нужно ли будет сохранить рецепт в файле? ")
    if mode != "":
        path = input("Введите имя файла, куда будет сохранен рецепт: ")
        doc.write_recipe(path)

    patient_email = input('Введите почту пациента: ')

    smtp_settings = SMTPSettings()

    email_message = EmailMessage(
        from_email=smtp_settings.email,
        to_email=patient_email,
        subject='Receipt',
        body='Test'
    )

    email_to_send = EmailSender(smtp_settings)
    email_to_send.send_email(email_message)


if __name__ == "__main__":
    main()
