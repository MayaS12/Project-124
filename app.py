from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [{
 'id': 1,
 'contact': u'+91 9619293944',
 'name': u'Maya',
 'done': False
 },
 {
 'id': 2,
 'contact': u'+91 9769026000',
 'name': u'Nikhil',
 'done': False
 }
]


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/get_data", methods=["GET"])
def get_task():
    return jsonify({
        "data": contacts
    })

@app.route("/add_data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data"
        })
    contact = {
        "id": contacts[-1]["id"] +1,
        "contact": request.json["contact"],
        "name": request.json["name"],
        "done": False
    }
    contacts.append(contact)
    return jsonify({
        "status":"Success",
        "message":"Added task Successfully"
    })
    

if __name__ =="__main__":
    app.run(debug=True)

