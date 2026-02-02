from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "AutoDeploy CI/CD Pipeline with Docker & Jenkins is LIVE 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
