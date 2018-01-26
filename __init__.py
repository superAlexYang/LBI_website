from flask import (Flask, render_template, redirect,
                   url_for, request, make_response)
from file_management import getImagesLabellingList, writeNewRow
from options import GROUP_1
import time
import outfit_management as om

app = Flask(__name__)

group_1_count = 0

Group_1PATH = 'static/Pics/'

imageList = list()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/save_Group_1', methods=['POST'])
def save_Group_1():
    response = make_response(redirect(url_for('group_1')))
    labelledDict = dict(request.form.items())
    print(labelledDict)
    om.writeNewRow(dict(request.form.items()), 'Group_1')
    global group_1_count
    group_1_count += 1
    return response

@app.route('/group_1')
def group_1():
    global imageList
    if len(imageList) == 0:
        imageList = om.getImagesLabellingList()
    else:
        print("Images Left:", len(imageList)-group_1_count)

    return render_template('group_1.html',
        imageDict=imageList[group_1_count],
        options=GROUP_1)


app.run(debug=True, port=3000, host='0.0.0.0')
