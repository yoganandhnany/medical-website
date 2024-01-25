import pandas
import numpy
import os
from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
app.config['FREEZER_RELATIVE_URLS'] = True
freezer = Freezer(app)

@app.route('/')
def index():
    ppt_folder = os.path.join(app.static_folder, 'ppts')
    ppt_files = [f for f in os.listdir(ppt_folder) if f.endswith('.pdf')]
    return render_template('index.html', ppts=ppt_files)

if __name__ == '__main__':
    freezer.freeze()
    # app.run(debug=True)