# CST 205 Section 2
# app.py

# has Flask and uploads the desired image to begin conversion

# Maria Loza

# 15 March 2017

# https://github.com/jantongiovanni/205Proj2/tree/maria

import os
import flask
from flask import request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory
import cairo_proj
import cairo
import shutil
import time

UPLOAD_FOLDER = 'static/uploads' #location that the desired photo will be saved
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg']) #only these formats will be allowed to upload

app = flask.Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 


def allowed_file(filename): #grabs the user's picture file name
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST']) #basic site
def index():
    
    if request.method == 'POST':
        cairo_proj.makeNewImg() #create a blank canvas
        newFile = cairo_proj.getNewFile() #gets the name of the new canvas file
        
        
        # if os.path.isfile("static/circlePacked/"+newFile):
        #     os.remove("static/circlePacked/"+newFile)
        
            
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
        if file and allowed_file(file.filename): #if the form has been properly completed
            if request.form['steps'] and request.form['count'] and request.form['radius'] and request.form['overlap']:
                # grabs info from form and sets it in cairo_proj
                newFile = cairo_proj.getNewFile()
                steps = int(request.form['steps'])
                cairo_proj.setSteps(steps)
                count = int(request.form['count'])
                cairo_proj.setCount(count)
                radius = float(request.form['radius'])
                cairo_proj.setRadius(radius)
                overlap = int(request.form['overlap'])
                cairo_proj.setOverlap(overlap)
                # saves the photo to the desired place
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                # # return redirect(url_for('uploaded_file', filename=filename))
                cairo_proj.imageSrc(UPLOAD_FOLDER+'/'+filename) #sends the desired image to be modified
                cairo_proj.main() #starts converting the image
                return redirect(url_for('uploaded_file', filename=filename, newFile=newFile)) #redirects to the new page
                # return flask.render_template("index.html", filename=filename, newFile=newFile)
            else:
                # in case the form isn't filled
                error = "Please fill out the form"
                return flask.render_template("index.html", error=error)
    return flask.render_template("index.html")
    
    

@app.route('/packed/<filename>/<newFile>')
def uploaded_file(filename, newFile):
    return flask.render_template("packed.html", filename=filename, newFile=newFile)

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)