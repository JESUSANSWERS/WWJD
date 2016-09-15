from gmailModule import Gmail
import subprocess
import time

def sendMessage(a):
    a = str(a)
    subprocess.call("python gmailText.py -u goog.trans.bot -p l0ll02013 -t 8642436724@txt.att.net -b '" + a + "'", shell=True)

while True:
    g = Gmail()
    g.login("goog.trans.bot", "l0ll02013")

    unreadEmails = g.inbox().mail(unread = True)
    if len(unreadEmails) > 0:
        print "there is an email"
        for email in unreadEmails: 
            email.fetch()
            email.read()
            emailSubject = email.subject
            print emailSubject
            emailSubject = emailSubject.split(": ")[1]
            print emailSubject
            if emailSubject == "bible":
                bibleRequest = str(email.body.split("\n")[0]).strip()
                proverb = subprocess.check_output("python bible.py '" + bibleRequest + "'", shell=True)
                proverb = str(proverb.split("\n")[0])
                sendMessage(proverb)
    else:
        print "no answers from your phone"

    time.sleep(2)
    g.logout()
