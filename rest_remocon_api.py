import os
import sys
sys.path.insert(0, "/usr/local/remocon/lib/")
import subprocess
import string
import random
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
#https://flask-restful.readthedocs.io/en/latest/quickstart.html

app = Flask(__name__)
api = Api(app)

users={}
queue_parser = reqparse.RequestParser()
queue_parser.add_argument('execcmd')
queue_parser.add_argument('user')
queue_parser.add_argument('key')
class queue(Resource):
    def get(self):
        try:
            node_free = len(subprocess.check_output("pbsnodes -l free", shell=True).strip().split("\n"))
        except:
            node_free = 0
        try:
            node_all = len(subprocess.check_output("pbsnodes -l all", shell=True).strip().split("\n"))
        except:
            node_all = 1
        return [node_all - node_free, node_all]

    def post(self):
        args = queue_parser.parse_args()
        user = args["user"]
        key = args["key"]
        if users[user] == key:
          cmd = "su -c \""+args["execcmd"]+"\" - "+user
          ret = subprocess.check_output(cmd, shell=True).strip()
          return ret
        else:
          return "Invalid User & Key"

users_parser = reqparse.RequestParser()
users_parser.add_argument('user')
class user_register(Resource):
    def post(self):
        args = users_parser.parse_args()
        user = args["user"]
        try:
            ret=subprocess.check_output("cat /etc/passwd | grep "+user, shell=True)
            ret=ret.strip()
        except:
            return {"message":"Invalid user","status":"fail"}
        else:
            ret = ret.split(":")
            usrid = ret[2]
            grid = ret[3]
            if user in users:
              key=users[user]
            else:
              key=randomStringDigits(10)
              users[user]=key
            return {"message":[usrid, grid, key],"status":"success"}

def randomStringDigits(stringLength=6):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

api.add_resource(user_register, '/user/register')
api.add_resource(queue, '/queue')
if __name__ == '__main__':
    app.run(debug=True)

