from flask import Flask , jsonify, request
app = Flask(__name__)

evn=[{
    "Event_name":"blood",
    "Event_id":"1",
    "Date": "2/5/2018",
    "Time": "9 pm",
    "Place": "delhi"

},{
    "Event_name":"HAck it!",
    "Event_id":"2",
    "Date": "2/8/2018",
    "Time": "9 pm",
    "Place": "delhi"
}]
people=[
    {
        "Intrested_events":"1",
        "name": "Bob",
        "email":"bob@gmail.com",
    },
    {
        "Intrested_events":"2",
        "name": "Tom",
        "email":"tom@gmail.com"
    }
]

# HOME PAGE
@app.route('/',methods=['GET'])
def show():
    return jsonify({"hi": "its working"})


# CREATE EVENTS
@app.route('/lang', methods=['POST'])
def test():
    details={

        'Event_name':request.json['Event_name'],
        'Event_id':request.json['Event_id'],
        'Date':request.json['Date'],
        'Time':request.json['Time'],
        'Place':request.json['Place']
    }
    todo.append(details)

    return jsonify({"v":evn})


#SHOW EVENT THAT WE HAVE CREATED
@app.route('/lang', methods=['GET'])
def test1():
   return jsonify({'Events': evn})


#CREATE PEOPLE LIST WITH ASSOCIATED EVENT ID
@app.route('/pop', methods=['POST'])
def check():
    pdetails={
        "name": request.json['name'],
        "Intrested_events":request.json['Intrested_events']
    }
    people.append(pdetails)
    return jsonify({'p': people})

#SHOWS LIST OF PEOPLE GOING IN A PARTICULAR EVENT ID
#SEARCH BY PASSING EVENT ID
@app.route('/pmatch/<int:id>', methods=['GET'])
def pshow(id):
    list1 = [x for x in people if x['Intrested_events'] == str(id)]
    return jsonify({'x': list1})



if __name__ == '__main__':
   app.run(debug=True, port=8080)

