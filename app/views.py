from app import app

from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')


#@app.route('/upload-image', methods=["GET", "POST"])
#def upload_image():
#    return render_template('upload_image.html')


@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)