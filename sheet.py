import gspread

class SheetEditor:
	def __init__(self,sheetName, sheet) -> None:
		self.sa = gspread.service_account(filename="spoorthi-336812-2c50e4c92911.json")
		self.sh = self.sa.open(sheetName)
		self.wks = self.sh.worksheet(sheet)

# print(wks.update('A2:B2', [['SPoorthi', 'Tech Head']]))

# sheetName = "Site Feature Testing"
# sheet = "Sheet1"