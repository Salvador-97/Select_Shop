from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import date

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'key.json'
SPREADSHEET_ID = '10ofAQNzJ0ZRu0N7UDyIv4psddjIA4VDIDhMejiEwJtc'

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes = SCOPES)

service = build('sheets', 'v4', credentials = creds)
sheet = service.spreadsheets()

# SKU = input('SKU: ')
# CONTENEDOR = input('Contenedor: ')
# FECHA = str(date.today())

# values = [[SKU, CONTENEDOR, FECHA]]
# result = sheet.values().append(spreadsheetId = SPREADSHEET_ID, 
#                                range = 'A1',
#                                valueInputOption = 'USER_ENTERED',
#                                body = {'values':values}).execute()

# sheet_id = 0

# deleteValues = {
#     'requests': [
#         {
#             'deleteDimension':{
#                 'range': {
#                     'sheetId': sheet_id,
#                     'dimension': 'ROWS',
#                     'startIndex': 4,
#                     'endIndex': 5
#                 }
#             }
#         },
#         {
#             'deleteDimension':{
#                 'range': {
#                     'sheet_id': sheet_id,
#                     'dimension': 'COLUMNS',
#                     'startIndex': 1,
#                     'endIndex': 1
#                     }   
#                 }   
#             } 
#     ]
# }

# service.spreadsheets().batchUpdate(
#     spreadsheetId = SPREADSHEET_ID,
#     body = deleteValues
# ).execute()