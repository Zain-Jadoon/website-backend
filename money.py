import random
from crud import *
from user import *
class Money:
    def __init__(self):
        pass
    def genID(acc, code):
        if len(code) == 6:
            if Crud.find(acc, code) != 0:
                return Money.genId(acc, "")
            else:
                return code
        if len(code) == 2:
            code = code+ "-"

        num = random.randint(1, 35)
        if num <= 26:
            code = code + chr(ord('`')+num).upper()
        if num > 26:
            code = code + str(num - 26)

        return Money.genID(acc, code) 
