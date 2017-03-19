from flask import flask

app = Flask(__name__)
@app.route("/")

def get_news():
	return "no news is good"

if __name__ == '__main__':
	app.run(port=5000, debug=True)

