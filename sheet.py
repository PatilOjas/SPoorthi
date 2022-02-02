import gspread

class SheetEditor:
	def __init__(self,sheetName, sheet) -> None:
		self.sa = gspread.service_account(filename=GOOGLE_SHEET_CREDENTIALS)
		self.sh = self.sa.open(sheetName)
		self.wks = self.sh.worksheet(sheet)
