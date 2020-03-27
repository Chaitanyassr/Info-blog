'''Flask that is a class is getting imported form flask'''
from flask import Flask
'''here we create an app variable using instance Flask and pass variable --name--'''
app = Flask(__name__)

'''route is a place were web app will open'''
@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'

if __name__ == '__main__':
    app.run()