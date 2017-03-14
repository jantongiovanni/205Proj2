import os
import flask
from flask import request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory
import cairo_proj
import cairo
import shutil

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = flask.Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flask.flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flask.flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            if request.form['steps'] and request.form['count'] and request.form['radius']:
                newFile = cairo_proj.getNewFile()
                # my_file = Path("static/circlePacked"+newFile)
                if os.path.isfile("static/circlePacked/"+newFile):
                    os.remove("static/circlePacked/"+newFile)
                steps = request.form['steps']
                # cairo_proj.setSteps(steps)
                count = request.form['count']
                # cairo_proj.setCount(count)
                # radius = request.form['radius']
                # cairo_proj.setRadius(radius)
                print cairo_proj.NEW_COUNT
                # print cairo_proj
                # print steps
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                # # return redirect(url_for('uploaded_file', filename=filename))
                cairo_proj.imageSrc(UPLOAD_FOLDER+'/'+filename)
                cairo_proj.main()
                # shutil.move("out.png", "static/circlePacked/"+newFile)
                return flask.render_template("index.html", filename=filename, newFile=newFile)
            else:
                error = "Please fill out the form"
                return flask.render_template("index.html", error=error)
    return flask.render_template("index.html")
    
    

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)