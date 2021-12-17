from imapclient import IMAPClient, SEEN
#sudo pip install imapclient for above

SEEN_FLAG = 'SEEN'
UNSEEN_FLAG = 'UNSEEN'

class GmailWrapper:
    def __init__(self):
        #   force the user to pass along username and password to log in as 
        
        #self.host = host
        self.host = 'imap.gmail.com'

        #self.userName = userName
        self.userName = 'samandoskarscatfeeder@gmail.com'

        #self.password = password
        self.password = 'esbd vuwi ycrp wlxe'

        self.login()
        
    def send_email(self, receiver,email_message,temp=0.0):
        # creates SMTP session
        print("Test")
        s = smtplib.SMTP('smtp.gmail.com', 465)
        print("init")

        # start TLS for security
        s.starttls()
        print("Logged in tls")

        # Authentication
        s.login(self.userName, self.password)
        print("Logged in smtp")
                  
        
        # sending the mail
        s.sendmail(self.userName, receiver, email_message)
        print("Email sent")

        # terminating the session
        s.quit()


    def login(self):
        print('Logging in as ' + self.userName)
        server = IMAPClient(self.host, use_uid=True, ssl=True)
        server.login(self.userName, self.password)
        self.server = server

    #   The IMAPClient search returns a list of Id's that match the given criteria.
    #   An Id in this case identifies a specific email
    def getIdsBySubject(self, subject, unreadOnly=True, folder='INBOX'):
        #   search within the specified folder, e.g. Inbox
        self.setFolder(folder)  

        #   build the search criteria (e.g. unread emails with the given subject)
        self.searchCriteria = [UNSEEN_FLAG, 'SUBJECT', subject]

        if(unreadOnly == False):
            #   force the search to include "read" emails too
            self.searchCriteria.append(SEEN_FLAG)

        #   conduct the search and return the resulting Ids
        return self.server.search(self.searchCriteria)

    def markAsRead(self, mailIds, folder='INBOX'):
        self.setFolder(folder)
        self.server.set_flags(mailIds, [SEEN])

    def setFolder(self, folder):
        self.server.select_folder(folder)
        
    def email_back(self, message, temp, uid=None):
        self.setFolder('INBOX')
        messages = self.server.search(['UNSEEN'])
        print(messages)
        bytes_msg = self.server.fetch(messages[0], ["RFC822"])
        msg = email.message_from_bytes(bytes_msg[messages[0]][b"RFC822"])
        sender = msg['From'].split('<')
        email_name = sender[1].replace('>', '')
        print(email_name)
        self.server.logout()
        
        self.send_email(email_name, message, temp)

if __name__ == '__main__':
    g = GmailWrapper()
    
    # g.email_back()
    #g.send_email('samandoskarscatfeeder@gmail.com')
    
    """
    print("logged in and in ifname main")
    g = GmailWrapper()
    print("logged in")
    # Continuously sarch for feed cat email
    while True:
        
        # Look for any emails with the subject "feed cats"
        ids = g.getIdsBySubject('feed cats')
        if ids:
            print("Fed the cat scat")
            g.markAsRead(ids)
            # Feed the cats
            break
    """
    