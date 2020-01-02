import os
from flask import Flask

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

@app.route('/')
def hello():
    return "Hello!"

@app.route('/<name>')
def hello_name(name):
    return f"Hello {name}!"

if __name__ == '__main__':
    app.run()
    print(os.environ['APP_SETTINGS'])