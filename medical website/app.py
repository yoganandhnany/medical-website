import pandas
import numpy
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    ppt_folder = os.path.join(app.static_folder, 'PPTs')
    ppt_files = [f for f in os.listdir(ppt_folder) if f.endswith('.pdf')]
    return render_template('index.html', ppts=ppt_files)

if __name__ == '__main__':
    app.run(debug=True)