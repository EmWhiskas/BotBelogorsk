import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# The ID and settings.py of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1D5LT5gGjbzfYrKjTAIg0E7u31i4W1wSnxbydeYe3Gtc'
# SAMPLE_RANGE_NAME = settings.date1
photo = []
mas = []
count = 0
def clear():
  global mas, count,photo
  mas.clear()
  photo.clear()
  count = 0

def main(SAMPLE_RANGE_NAME):
  global mas, count
  """Shows basic usage of the Sheets API.
  Prints values from a sample spreadsheet.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
      sheet.values()
      .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
      .execute()
    )
    values = result.get("values", [])

    if not values:
      print("No data found.")
      mas.append('Вышла ошибочка, попробуй позже')
      return mas

    for row in values:

        count += 1
        if count == 1:
            mas.append('<b>Адрес</b>')
        elif count == 2:
            mas.append('<b>\nМероприятия</b>')

        try:
            answer = (row[0])
            if count != 3:
                mas.append(answer)
            else:
                if row[0] != 'Нет':
                    photo.append(answer)
                else:
                    photo.append('AgACAgIAAxkBAAICKmYeeifllKBPsqIfHTMYhySiGtciAAL42zEb8gH5SCZhcHLmGm6pAQADAgADcwADNAQ')
        except:
            mas.append('---')

    return mas, photo



  except HttpError as err:
    print(err)
