import json
import time
import threading
from flask import Flask
from flask_restful import Api, Resource, reqparse,request
import gspread
from money import *
from misc import *
from user import *
from flask_cors import CORS
from multiprocessing import Process
sa = gspread.service_account("zainbucks.json")
sh = sa.open("zain-bucks")
acc = sh.worksheet("acc")
_id = sh.worksheet("id")

app = Flask(__name__)
CORS(app)
api = Api(app)


class PrintMoney(Resource):
    def post(self):
        pass

class Transact(Resource): 
    def post(self):
        try: 
            data = json.loads(request.data)
            _from = data["from"]
            from_passwd = data["from_passwd"]
            to = data["to"]
            ammount = int(data["ammount"])
        except KeyError:
            return {"result": "Error: Invalid Request, Required data not specified"}
        try:
            if Crud.find(acc, _from) !=0 and Crud.find(acc, to) != 0:
                sender = User(acc, _from)
                reciever = User(acc, to)
                if sender.comparePswd(from_passwd):
                    if sender.bal >= ammount:
                        sender.increment(int(ammount) * -1)
                        reciever.increment(int(ammount))
                        return {"result": "Money Transfered"}
                    if int(sender.bal) <= ammount:
                        return {"result": "insufficient funds"}
                else:
                    return {"result":"password incorrect"}
            else:
                return {"result": "one or more users in request do not exist"}
        except gspread.exceptions.APIError:
            return{"result":"Server Error: Heavy Demand on servers, try again in a few secconds"}


def addResourses():
    api.add_resource(Transact,"/transact")
    api.add_resource(PrintMoney,"/print-money")
if __name__ == '__main__':
   addResourses()
   app.run(host='localhost', port=5000,debug=True)
