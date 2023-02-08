# import modules that we need in order to upload csv file using flask

from flask import Flask, render_template, request, session
import os
from werkzeug.utils import secure_filename

# *** Flask configuration

# Define folder to save uploaded files to process further
UPLOAD_FOLDER = os.path.join('staticFiles', 'uploads')

# Define allowed files (for this example I want only csv file)
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')
# Configure upload file path flask
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define secret key to enable session
app.secret_key = 'Supersecretkey'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=("POST", "GET"))
def uploadFile():
    if request.method == 'POST':
        # upload file flask
        uploaded_df = request.files['uploaded-file']

        # Extracting uploaded data file name
        data_filename = secure_filename(uploaded_df.filename)

        # flask upload file to database (defined uploaded folder in static path)
        uploaded_df.save(os.path.join(app.config['UPLOAD_FOLDER'], data_filename))

        # Storing uploaded file path in flask session
        session['uploaded_data_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], data_filename)
        return render_template('index2.html')