import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    r = requests.get("https://api.github.com")
    return {
        "message": "Hello from vulnerable Python app!",
        "github_status": r.status_code
    }

if __name__ == "__main__":
    app.run(debug=True)
