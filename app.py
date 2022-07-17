from flask import Flask, render_template, send_from_directory, url_for
from flask import Flask, render_template, Response
app = Flask(__name__, static_folder='pdf')

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route('/pdf/<path:filename>', methods=['GET', 'POST'])
def download(filename):    
    return send_from_directory(directory='pdf', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
