# -*- coding: utf-8 -*-

# Import package
import smtplib

class Send_Mail:
    def __init__(self, fromAdd, toAdd):
        self.fromMy = fromAdd
        self.to = toAdd

    def write_mail(self, subject, content):
        sub = subject
        message_text = content
        msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % ( self.fromMy, self.to, sub, message_text )
        return msg

    def send_mail(self, subject, content):
        msg = self.write_mail(subject, content)
        username = str('send_log@yahoo.com')
        password = str('LTlt6421')
        try :
            server = smtplib.SMTP("smtp.mail.yahoo.com",587)
            server.starttls()
            server.login(username, password)
            server.sendmail(self.fromMy, self.to, msg)
            server.quit()
            print 'ok the email has sent '
        except :
            print 'can\'t send the Email'


