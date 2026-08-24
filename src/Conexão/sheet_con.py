import gspread
from google.auth import default


ID_SHEET = "1lxkwmxp5FfOMmOXmw6CbhQzhDGlKR5CZ1geSAKjxq_E"

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets.readonly",
    "https://www.googleapis.com/auth/drive.readonly",
]

def connect_sheet():
    credentials, project = default(scopes=SCOPES)

    gc = gspread.authorize(credentials)

    spreadsheet = gc.open_by_key(ID_SHEET)
    return spreadsheet

