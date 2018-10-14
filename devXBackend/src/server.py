
from flask import Flask, request, Response
import numpy as np
import os
from flask import Flask, flash, request, redirect, url_for,send_from_directory
from werkzeug.utils import secure_filename
import base64
import mean_pixel_value

UPLOAD_FOLDER = './'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/output")
def output():
	return "Hello World!"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 

@app.route('/upload/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

# route http posts to this method
@app.route('/upload', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
         # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        genre = request.form['genre']
        if genre == 'all':
                genre = 'chill'
        print(genre)
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            #filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'input_pic.jpg'))
            mean_pixel_value.main_input(genre)
            with open("output_pic.jpg", "rb") as imageFile:
                str = base64.b64encode(imageFile.read())
            return str
            #redirect(url_for('uploaded_file',
             #                       filename=filename))


if __name__ == "__main__":
	app.run()
