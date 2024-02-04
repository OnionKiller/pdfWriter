from __future__ import print_function
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import mimetypes
import os

from apiclient import errors

def SendMessage(service, user_id, message):
  """Send an email message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.

  Returns:
    Sent Message.
  """
  try:
    message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
    print ('Message Id: %s' % message['id'])
    return message
  except errors.HttpError as error:
    print ('An error occurred: %s' % error)


def CreateMessage(sender, to, subject, message_text):
  """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

  Returns:
    An object containing a base64url encoded email object.
  """
  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  print(repr(message))
  raw = base64.urlsafe_b64encode(message.as_bytes())
  raw = raw.decode()
  return {'raw': raw}


def CreateMessageWithAttachment(sender, to, subject, message_text, file_dir,filename):
    """Create a message for an email.

    Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.
    file_dir: The directory containing the file to be attached.
    filename: The name of the file to be attached.

    Returns:
    An object containing a base64url encoded email object.
    """
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    msg = MIMEText(message_text)
    message.attach(msg)

    pdf = MIMEBase('application', "pdf")
    message.attach(pdf)

    path = os.path.join(file_dir, filename)
    with open(path, 'rb') as pdf_file:
        pdf.set_payload(pdf_file.read())
        encoders.encode_base64(pdf)
        pdf.add_header('Content-Disposition', 'attachment', filename=filename)

    message.attach(pdf)
    raw = base64.urlsafe_b64encode(message.as_bytes())
    raw = raw.decode()
    return {'raw': raw}

def Authorize():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(r"D:\Dürer\infoMCS\pdfWriter\gmail\token.pickle"):
        with open(r"D:\Dürer\infoMCS\pdfWriter\gmail\token.pickle", 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # If modifying these scopes, delete the file token.pickle.
            SCOPES = ['https://www.googleapis.com/auth/gmail.readonly','https://www.googleapis.com/auth/gmail.send']
            flow = InstalledAppFlow.from_client_secrets_file(
                r"D:\Dürer\infoMCS\pdfWriter\gmail\credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(r"D:\Dürer\infoMCS\pdfWriter\gmail\token.pickle", 'wb') as token:
            pickle.dump(creds, token)
    service = build('gmail', 'v1', credentials=creds)
    return service

def sendMailTocandidate(service,senderEmail,reciverEmail,messageText,attachment):
    message = CreateMessageWithAttachment(senderEmail,reciverEmail,"XIII. Dürer Verseny helyi forduló eredmény",messageText,r"D:\Dürer\infoMCS\pdfWriter",attachment)
    SendMessage(service,senderEmail,message)

if __name__ == "__main__":
    service = Authorize()
    sendMailTocandidate(service,"durerinfo@gmail.com","durerinfo@gmail.com","Gratulálunk! A versenyen elért eredményed az oklevelen majd meglátod:","document-output.pdf")
    sendMailTocandidate(service,"durerinfo@gmail.com","durerinfo@gmail.com","Gratulálunk! A versenyen elért eredményed az oklevelen majd meglátod:","document-output.pdf")
    sendMailTocandidate(service,"durerinfo@gmail.com","durerinfo@gmail.com","Gratulálunk! A versenyen elért eredményed az oklevelen majd meglátod:","document-output.pdf")
    print(service.users().getProfile(userId = "durerinfo@gmail.com").execute())
    #message = CreateMessageWithAttachment("durerinfo@gmail.com","durerinfo@gmail.com","Teszt","Ez egy teszt.",r"C:\Users\tomi\python\pdf","document-output.pdf")
    #SendMessage(service,"durerinfo@gmail.com",message)