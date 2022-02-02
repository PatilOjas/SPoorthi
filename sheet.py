import gspread
from decouple import config


class SheetEditor:
	def __init__(self,sheetName, sheet) -> None:
		self.sa = gspread.service_account_from_dict(eval(config('GOOGLE_SHEET_CREDENTIALS')))
		self.sh = self.sa.open(sheetName)
		self.wks = self.sh.worksheet(sheet)
