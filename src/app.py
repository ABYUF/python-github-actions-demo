from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Flask, Gunicorn, Nginx is successfully working, Welcome to CI/CD Pipeline, DevOps!"

if __name__ == '__main__':
    app.run()

