from flask import Flask
import flask_mail

from datetime import datetime
from utils.config import get_config

# 异步发送邮件
class EmailSender:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['MAIL_SERVER'] = get_config('email.server')
        self.app.config['MAIL_PORT'] = get_config('email.port')
        self.app.config['MAIL_USERNAME'] = get_config('email.username')
        self.app.config['MAIL_PASSWORD'] = get_config('email.password')
        self.app.config['MAIL_USE_SSL'] = False
        self.app.config['MAIL_USE_TLS'] = True
        self.mail_obj = flask_mail.Mail(self.app)

    def send_email(self,
        subject: str,
        body: str,
        sender: str,
        recipients: list):

        sender = sender.replace('%40', '@')
        for i in range(len(recipients)):
            recipients[i] = recipients[i].replace('%40', '@')

        msgObject = flask_mail.Message(
            subject=subject,
            body=body,
            sender=sender,
            recipients=recipients
        )
        app = self.app
        with app.app_context():
            self.mail_obj.send(msgObject)

if __name__ == '__main__':
    sender = EmailSender()
    sender.send_email(
        'test subject',
        str(datetime.now()),
        'noreply@crowdlabel.org',
        ['me@georgetian.com']
    )