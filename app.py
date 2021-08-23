
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask CI/CD"

app.run(debug=False)