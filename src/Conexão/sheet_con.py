import gspread
from google.auth import default


ID_SHEET = "1fmnXoXn0HGqwiQEwZke6mBSNHw1eaJ1wjtcPob9SU8s"

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets.readonly",
    "https://www.googleapis.com/auth/drive.readonly",
]

def connect_sheet():
    credentials, project = default(scopes=SCOPES)

    gc = gspread.authorize(credentials)

    spreadsheet = gc.open_by_key(ID_SHEET)
    return spreadsheet

