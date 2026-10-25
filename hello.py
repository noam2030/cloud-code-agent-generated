from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, world!"

if __name__ == '__main__':
    # Listen on all interfaces for Docker/cloud compatibility
    app.run(host='0.0.0.0', port=5000)
