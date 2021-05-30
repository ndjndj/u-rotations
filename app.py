from flask import Flask, render_template, request, make_response, jsonify
from flask_cors import CORS
from models.models import UName, RaceCalendar

app = Flask(__name__)


CORS(app)

@app.route('/')
def hello_world():
    message = "Hello World"

    return message

@app.route('/json-test')
def json_parse():
    u_names_data = UName.query.all()

    data = [
        {
            'id': u.u_id,
            'farm': u.u_farm_name,
            'name': u.u_name,
            'created_at': u.created_at,
            'updated_at': u.updated_at
        }
        for u in u_names_data
    ]

    print(data)

    return jsonify(data)

@app.route('/u-rotation')
def u_rotation():
    return render_template('rotation.html')

@app.route('/u-names')
def u_names():
    u_names_data = UName.query.all()
    return render_template("u-name.html", u_names=u_names_data)

@app.route('/u-race')
def u_race():
    race_data = RaceCalendar.query.all()
    return render_template("race-schedule.html", races=race_data)



if __name__ == '__main__':
    app.run(debug=True)
