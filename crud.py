class Crud:
    def __init__(self):
        pass
    def find(sheet, phrase):
        try:
            a = sheet.find(phrase)
            return [a.row, a.col]
        except AttributeError:
            return 0 

