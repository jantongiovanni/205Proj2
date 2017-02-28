import flask
import os

UPLOAD_FOLDER = '/static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = flask.Flask(__name__)

@app.route('/')
def index():
    #return "Hello, World"
    return flask.render_template("index.html")

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)