from flask import Flask,jsonify,request

app = Flask(__name__)

stores = [{ "name": "store1",
             "items": [ "rice " , "wheat " , "bread"]
          },
          { "name": "store2",
             "items": [ "rice 2" , "wheat 2" , "bread2"]
          },{ "name": "store3",
             "items": [ "teach " , "deaf " , "bread"]
          }
]

@app.route('/')
def home():
    return "Hellllllo world"

@app.route('/store')
def showStores():
    return jsonify({ "stores": stores })


@app.route('/addstore',methods=['POST'])
def addstore():
    req_data = request.get_json()
    newStore = {
        "name": req_data['name'],
        "items" :[]
    }
    stores.append(newStore)
    return jsonify({'message': " You just hit a post request to add a store "})

app.run(port=8080)