import gspread

from google.auth import default


id_sheet = "1fmnXoXn0HGqwiQEwZke6mBSNHw1eaJ1wjtcPob9SU8s"


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets.readonly",
    "https://www.googleapis.com/auth/drive.readonly",
]

credentials, project = default(scopes=SCOPES)

gc = gspread.authorize(credentials)

spreadsheet = gc.open_by_key(id_sheet)

print(f"Planilha: {spreadsheet.title}")

for worksheet in spreadsheet.worksheets():
    print(f"Aba: {worksheet.title}")