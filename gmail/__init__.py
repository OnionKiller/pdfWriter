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
import sys
sys.path.append(r"D:\Dürer\infoMCS\pdfWriter\gmail")
from send import Authorize
from send import sendMailTocandidate as sendMail