from utils.emailsender import EmailSender

sender = EmailSender()

import random

def generate_verification_code():
    # generates a 6 digit verification code
    return str(random.randint(0, 999999)).rjust(6, '0')


def send_verification_email(email, verification_code):
    sender.send_email(
        'CrowdLabel 邮箱验证码',
        verification_code,
        'noreply@crowdlabel.org',
        [email]
    )

if __name__ == '__main__':
    send_verification_email('chenjz20@mails.tsinghua.edu.cn', '666666')