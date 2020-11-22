import flask
from flask import request
from flask_cors import CORS
import base64
from flask import render_template
import os


def get_frames(img_dir="app/data/imgs"):

    img_streams, img_local_path = return_img_stream(img_dir)
    dic = {'imgs': img_streams, 'pic_name': img_local_path}
    return dic


def return_img_stream(img_local_paths):
    img_streams = []
    paths = [img for img in os.listdir(img_local_paths) if '.jpg' in img]
    for img_local_path in paths:
        if '.jpg' in img_local_path:
            path = os.path.join(img_local_paths, img_local_path)
            with open(path, 'rb') as img_f:
                img_stream = img_f.read()
                img_stream = base64.b64encode(img_stream)
                img_stream = str(img_stream, "utf-8")
                img_streams.append(img_stream)
    return img_streams, paths


def get_img_stream(img_local_paths):
    img_streams = []
    paths = [img for img in os.listdir(img_local_paths) if '.jpg' in img]
    for img_local_path in paths:
        if '.jpg' in img_local_path:
            path = os.path.join(img_local_paths, img_local_path)
            with open(path, 'rb') as img_f:
                img_stream = img_f.read()
                img_stream = base64.b64encode(img_stream)
                img_stream = str(img_stream, "utf-8")
                img_streams.append(img_stream)
    return img_streams, paths