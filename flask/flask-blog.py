'''Flask that is a class is getting imported form flask'''
from flask import Flask
'''here we create an app variable using instance Flask and pass variable --name--'''
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()