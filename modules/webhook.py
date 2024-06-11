import imaplib
import email

class EmailChecker:
    def __init__(self):
        self.username = "webhookreciver@gmail.com"
        self.password = "ideo gbrx esmr iymg"
        self.imap_server = "imap.gmail.com"
        self.imap_port = 993

    def checkemail(self):
        try:
            hold = '{"action": "hold", "close": "00000", "time": "2024"}'
            
            mail = imaplib.IMAP4_SSL(self.imap_server, self.imap_port)
            mail.login(self.username, self.password)

            mail.select("inbox")

            status, email_ids = mail.search(None, "(UNSEEN)")
            if email_ids[0]:
                latest_email_id = email_ids[0].split()[-1]

                status, email_data = mail.fetch(latest_email_id, "(RFC822)")
                raw_email = email_data[0][1]

                msg = email.message_from_bytes(raw_email)

                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        if "text/plain" in content_type:
                            body = part.get_payload(decode=True).decode()
                            break
                else:
                    body = msg.get_payload(decode=True).decode()

                mail.close()
                mail.logout()
            
                return body

        except Exception as e:
            return 'ERROR'
