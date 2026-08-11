import gspread
from google.auth import default


ID_SHEET = "1lxkwmxp5FfOMmOXmw6CbhQzhDGlKR5CZ1geSAKjxq_E"

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets.readonly",
    "https://www.googleapis.com/auth/drive.readonly",
]


credentials, project = default(scopes=SCOPES)

gc = gspread.authorize(credentials)

spreadsheet = gc.open_by_key(ID_SHEET)

print(f"Planilha: {spreadsheet.title}")


records = spreadsheet.worksheet("records")

print(f"\nAba: {records.title}")

valor_records = records.get(
    "F5",
    value_render_option="FORMULA"
)

print("records F5:")
print(valor_records)

daily = spreadsheet.worksheet("daily")

print(f"\nAba: {daily.title}")


valor_daily = daily.get(
    "R5",
    value_render_option="FORMULA"
)

print("daily R5:")
print(valor_daily)

print("\nValores dos horários da daily:")

horarios = daily.get(
    "F5:Q5",
    value_render_option="FORMULA"
)

print(horarios)


print("\nPrimeiras linhas da daily:")

dados_daily = daily.get("A3:Q7")

for linha in dados_daily:
    print(linha)