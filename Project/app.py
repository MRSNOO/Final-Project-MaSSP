from flask import Flask, request, render_template, url_for, redirect, send_from_directory, jsonify
import os

from mpl_toolkits.axes_grid1 import host_axes

import config
import time
import cv2
import numpy as np
from haze_removal import haze_removal
import try_lib
import json
from flask_cors import CORS
from copy_of_mtcnn_fix import FaceRecognizer


app = Flask(__name__)


@app.route('/', methods = ['GET','POST'])
def home():
  return render_template("index.html")



@app.route('/img_show/<path:filename>')
def img_show(filename):
    return send_from_directory(config.img_out_dir, filename)


@app.route("/handleUpload", methods=['POST'])
def handle_file_upload():
    print('received')
    print(request.files)
    
    new_name="xxx"
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':
            new_name = str(int(time.time())) + '.jpg'
            photo.save(os.path.join(config.img_dir, new_name))
            # time.sleep(1)
            de_haze(new_name) # solve problem
            face_recognize(new_name)
            time.sleep(1)
        else:
            print('nothoing')
    else:
        print('no file')
    return jsonify({'data': new_name})
    # return redirect(url_for('/home', filename=new_name))


def face_recognize(new_name):
  Detector = FaceRecognizer()
  for image in [config.img_dir + new_name]:
    img = Detector.img_load(str(image))
    Detector.search_face(img)

def de_haze(new_name):
    image = np.array(cv2.imread(config.img_dir + new_name))
    cv2.imwrite(config.img_out_dir + new_name, haze_removal(image))

if __name__ == '__main__':
  app.run(port=8000, debug=True)
