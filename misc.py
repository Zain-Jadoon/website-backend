import hashlib
from crud import *

def hash_pass(passwd):
    hashed_string = hashlib.sha256(passwd.encode('utf-8')).hexdigest()
    return hashed_string

def createUser(acc, uname, pswd, bal, active):
    if Crud.find(acc, uname) != 0:
        return {"result":"Error: Username already Exists"}
    alen = len(acc.col_values(1))
    acc.update("A"+str(alen+1),uname)
    acc.update("B"+str(alen+1),str(hash_pass(pswd)))
    acc.update("C"+str(alen+1),str(bal))
    acc.update("D"+str(alen+1),str(active))
    return {"result":"User Created"} 