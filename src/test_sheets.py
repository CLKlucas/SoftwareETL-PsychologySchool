import gspread
from google.auth import default

ID_SHEET = "1fmnXoXn0HGqwiQEwZke6mBSNHw1eaJ1wjtcPob9SU8s"

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets.readonly",
    "https://www.googleapis.com/auth/drive.readonly",
]

credentials, project = default(scopes=SCOPES)

gc = gspread.authorize(credentials)

spreadsheet = gc.open_by_key(ID_SHEET)

print(f"Planilha: {spreadsheet.title}")

# Aba records
records = spreadsheet.worksheet("records")

print(f"\nAba: {records.title}")

valor_records = records.get(
    "F4",
    value_render_option="FORMULA"
)

print("records F4:")
print(valor_records)


# Aba daily
daily = spreadsheet.worksheet("daily")

print(f"\nAba: {daily.title}")

valor_daily = daily.get(
    "R4",
    value_render_option="FORMULA"
)

print("daily R4:")
print(valor_daily)