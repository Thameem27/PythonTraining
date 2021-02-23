from flask import Flask, request
from flask_restful import reqparse, Api, Resource

app = Flask(__name__)
api = Api(app)


vegdata = [
        {
        "vegname" : "Cabbage",
        "Quantity" : "20",
        },
        {
        "vegname" : "Carrot",
        "Quantity" : "10",
        },
        {
        "vegname" : "Curry Leaves",
        "Quantity" : "5",
        },
        {
        "vegname" : "Tomato",
        "Quantity" : "50",
        },
        ]
         

class VegetableData(Resource):
    def get(self):
        return vegdata

class VegetableList(Resource):
    def get(self):
        return vegdata    
        
    def post(self):
        vegdict = {}
        vegdict["vegname"] = request.json["vegname"]
        vegdict["Quantity"] = request.json["Quantity"]
        vegdata.append(vegdict)
        return request.json    
class VegetableData(Resource):
 

    def get(self, veg_id):      
        for index in vegdata:
            if veg_id == index['vegname']:
                return index
        else:
            abort(404, message=f"{veg_id} is Not Available in the list ")   

    def delete(self, veg_id):
        for index,listItem in enumerate(vegdata):

            if veg_id == listItem["vegname"]:
                vegdata.pop(index)
                return veg_id + " Deleted"
        else:
            abort(404, message=f"{veg_id} is Not Available in the list")
            
            
    def put(self, veg_id):
        for index, listItem in enumerate(groceries):
            if veg_id == listItem['vegname']:
                listItem['quantity'] = request.json['quantity']
                return veg_id + ' is Updated'
        else:
            abort(404, message=f"{veg_id} is Not Available in the list")     
            
api.add_resource(VegetableList, '/vegetables')
api.add_resource(VegetableData, '/vegetables/<string:veg_id>')