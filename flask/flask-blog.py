'''Flask that is a class is getting imported form flask'''
from flask import Flask, render_template
'''here we create an app variable using instance Flask and pass variable --name--'''
app = Flask(__name__)

'''route is a place were web app will open'''
'''
@app.route('/')
def hello_world():
    return '<h1>Home page</h1>' '''

   posts = [
   {
   'author': 'chaitanya'
   'title': 'Blog post 1'
   'content': 'first post content'
   'date_posted': 'march 29, 2020'
   },
{
	'author': 'chinuon'
   'title': 'Blog post 2'
   'content': 'second post content'
   'date_posted': 'march 30, 2020'
}
   ]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

'''makingdebug = true so to run the app in debut mode so tha tpage can update automatically'''
if __name__ == '__main__':
    app.run(debug=true)