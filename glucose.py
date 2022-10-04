from flask import Flask, jsonify, request

app = Flask(__name__)
glucose_information=[
    {
        "glucose_id" : "101977",
        "date" : "09/4/22",
        "glucose" : "100"
    },
     {
        "glucose_id" : "776688",
        "date" : "09/4/22",
        "glucose" : "113"
    }, 

        
    
    

]
@app.route('/glucose_information', methods=['GET'])
def displayglucose_information():
    return jsonify(glucose_information)

if __name__== '__main__':
    app.run()