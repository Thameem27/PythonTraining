from flask import Flask, request, render_template

app = Flask(__name__)

data = [
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
        
@app.route('/')
def index():
    return 'Welcome to the Grocery App.'
    
    
@app.route('/groceries/',methods=['GET'])
def veg():
    return jsonify(data)
    
@app.route('/groceries/<vegnam>', methods=['GET'])
def groceries(vegnam):
    #return render_template('GroceryList.html', data=vegnam) I wanted to achieve this in Jinja Template but couldnt succeed
   if request.method == 'GET':
        for veg in data:
            if vegnam == veg['vegname']:
                return veg
        else:
            return "This Vegetable is not in the list"