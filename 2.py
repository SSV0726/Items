from flask import Flask,jsonify,request
from flask_restful import Resource,Api
from security import authenticate,identity
from flask_jwt import JWT,jwt_required

app = Flask(__name__)
app.secret_key = " place the secret key here "
api = Api(app)

jwt = JWT(app,authenticate,identity)

items = []

class item(Resource):
    @jwt_required()
    def get(self,name):
        item = next(filter(lambda x: x['name']==name,items),None)
        return {"item returned": item},200 if item else 404
    
    @jwt_required()
    def post(self,name):
        data = request.get_json()
        check = next(filter(lambda x : x['name']==name,items ),None)
        print(" value of check is {}".format(check))
        if check :
            return {" message ": "A item with name '{}' already exists".format(name)},400
        
        item = { "name":name , "price": data['price']}
        items.append(item)
        return {'message': "price Updated"},200

class itemsList(Resource):
    @jwt_required()
    def get(self):
        return {'Items':items},200

api.add_resource(item,'/item/<string:name>')
api.add_resource(itemsList,'/items')

app.run(port=5555)
