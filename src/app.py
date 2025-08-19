from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Flask is working, Welcome to CI/CD Pipeline, DevOps!"

if __name__ == '__main__':
    app.run()

