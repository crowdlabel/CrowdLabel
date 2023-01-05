from flask import Flask
import flask_mail
import threading
from datetime import datetime
import utils.config

# 异步发送邮件
class EmailSender:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['MAIL_SERVER'] = utils.config.config['email']['server']
        self.app.config['MAIL_PORT'] = utils.config.config['email']['port']
        self.app.config['MAIL_USERNAME'] = utils.config.config['email']['username']
        self.app.config['MAIL_PASSWORD'] = utils.config.config['email']['password']
        self.app.config['MAIL_USE_SSL'] = False
        self.app.config['MAIL_USE_TLS'] = True
        self.mail_obj = flask_mail.Mail(self.app)
    def send_async_email(self,app, msg):
        with app.app_context():
            self.mail_obj.send(msg)

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
        thr = threading.Thread(target =self.send_async_email, args = [app,msgObject])#创建线程
        thr.start()

if __name__ == '__main__':
    sender = EmailSender()
    sender.send_email(
        'test subject',
        str(datetime.now()),
        'noreply@crowdlabel.org',
        ['me@georgetian.com']
    )