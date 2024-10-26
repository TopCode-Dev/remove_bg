from flask import send_file
from flask import jsonify
from PIL import Image
from rembg import remove
import os

UPLOAD_FOLDER = "/tmp/"

ImgPath = 'data/barefeet1.jpeg'


def main(ImgPath, ):
    try:
        basedir = os.path.abspath(os.path.dirname(__file__))
        os.environ['U2NET_HOME'] = basedir + '/model'
        # os.environ['U2NET_HOME'] = 'src/model/u2net.onnx'
        out_folder = UPLOAD_FOLDER + "/output.png"
        image = Image.open(ImgPath)
        print("gets here-1" + basedir)
        output = remove(image)
        # imageBox = output.getbbox()
        print("gets hereA")
        # cropped = output.crop(imageBox)
        output.save(out_folder)

        return send_file(out_folder, mimetype='image/png')
    except Exception as e:
        # General exception handler for any other runtime errors
        return jsonify({"error": str(e)}), 500


