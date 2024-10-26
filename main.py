from flask import Flask
from flask import send_file
from flask import request
from flask import flash
from flask import redirect
from flask import jsonify
from flask import g
import uuid
import os
import datetime
import random
# from object_detection import object_detection
import rm_bg_main

app = Flask(__name__)
# UPLOAD_FOLDER = "files_reception/"
UPLOAD_FOLDER = "/tmp/"
CALCULATED_FOLDER = "calculated_images/"


def alphanumeric(number):
    """
    This function allows to generate an alphanumeric text

    :param number: int -- Number of characters in the expected text
    :return: str -- Text of *number* alphanumeric characters
    """
    return ''.join(random.choice('0123456789ABCDEF') for i in range(number))

@app.before_request
def before_request_func():
    execution_id = uuid.uuid4()
    g.start_time = datetime
    g.execution_id = execution_id

    print(g.execution_id, "ROUTE CALLED ", request.url)
@app.route("/version", methods=["GET"], strict_slashes=False)
def version():
    response_body = {
        "success": 1,
    }
    return jsonify(response_body)


@app.route('/rm_img_bg', methods=["POST"])
def rm_img_bg():

    # Start the timer to get the execution time at the end
    start_date = datetime.datetime.now()
    print(start_date)

    # Obtenir le fichier reçu de la requête POST
    if request.method == "POST":
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        print(file.filename)
        alphanumeric_filename = "test.png"
        print(alphanumeric_filename)
        file.save(os.path.join(UPLOAD_FOLDER, alphanumeric_filename))
        return rm_bg_main.main(os.path.join(UPLOAD_FOLDER, alphanumeric_filename))


@app.route('/bonjour/')
def bonjour():
    return 'Hello World\n'


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.config['MAX_CONTENT_LENGTH'] = 200 * 1024 * 1024
    app.run(host="0.0.0.0", port=8080)
