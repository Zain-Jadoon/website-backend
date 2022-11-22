from misc import *
from crud import *
class User:

    def __init__(self, acc, uname):
        self.acc = acc
        self.uname = uname
        self.row = Crud.find(acc,uname)[0]
        self.pswd = acc.cell(self.row, 2).value
        self.bal = int(acc.cell(self.row,3).value)
        self.active = acc.cell(self.row,2).value
    def comparePswd(self, paswd):
        if hash_pass(paswd) == self.pswd:
            return True
        else:
            return False
    def increment(self, ammount):
        ammount = int(ammount)
        self.bal = int(self.bal) + int(ammount)
        self.acc.update_cell(self.row, 3, self.bal)

    