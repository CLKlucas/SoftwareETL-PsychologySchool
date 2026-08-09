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

worksheet = spreadsheet.worksheet("records")

print(f"\nAba selecionada: {worksheet.title}")

dados = worksheet.get_all_values()

print(f"Quantidade de registros: {len(dados)}")

print("\nPrimeiros 5 registros:")

for registro in dados[:5]:
    print(registro)